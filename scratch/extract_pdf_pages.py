import zlib, re, sys

def decompress_stream(data):
    try:
        return zlib.decompress(data)
    except Exception:
        pass
    try:
        return zlib.decompress(data.strip())
    except Exception:
        pass
    try:
        d = zlib.decompressobj()
        return d.decompress(data)
    except Exception:
        pass
    return None

def parse_cmap(cmap_str):
    mapping = {}
    codespace_len = 2
    csr = re.search(r'begincodespacerange(.*?)endcodespacerange', cmap_str, re.DOTALL)
    if csr:
        m = re.search(r'<([0-9A-Fa-f]+)>\s*<([0-9A-Fa-f]+)>', csr.group(1))
        if m:
            codespace_len = len(m.group(1))

    # 1. Parse ONLY within beginbfchar ... endbfchar
    for bfc in re.finditer(r'beginbfchar(.*?)endbfchar', cmap_str, re.DOTALL):
        chunk = bfc.group(1)
        for m in re.finditer(r'<([0-9A-Fa-f]+)>\s*<([0-9A-Fa-f]+)>', chunk):
            src_hex = m.group(1)
            dst_hex = m.group(2)
            if len(src_hex) == codespace_len:
                src = int(src_hex, 16)
                chars = ''.join(chr(int(dst_hex[i:i+4], 16)) for i in range(0, len(dst_hex), 4))
                mapping[src] = chars

    # 2. Parse ONLY within beginbfrange ... endbfrange
    for bfr in re.finditer(r'beginbfrange(.*?)endbfrange', cmap_str, re.DOTALL):
        chunk = bfr.group(1)
        # Check arrays first: <start> <end> [ ... ]
        for m in re.finditer(r'<([0-9A-Fa-f]+)>\s*<([0-9A-Fa-f]+)>\s*\[(.*?)\]', chunk, re.DOTALL):
            start = int(m.group(1), 16)
            dests = re.findall(r'<([0-9A-Fa-f]+)>', m.group(3))
            for i, d in enumerate(dests):
                chars = ''.join(chr(int(d[j:j+4], 16)) for j in range(0, len(d), 4))
                mapping[start + i] = chars
        # Check 3-arg range: <start> <end> <dest_start>
        for m in re.finditer(r'<([0-9A-Fa-f]+)>\s*<([0-9A-Fa-f]+)>\s*<([0-9A-Fa-f]+)>', chunk):
            start = int(m.group(1), 16)
            end = int(m.group(2), 16)
            dest = int(m.group(3), 16)
            for i in range(end - start + 1):
                mapping[start + i] = chr(dest + i)

    return codespace_len, mapping

def extract_pdf(pdf_path):
    with open(pdf_path, 'rb') as f:
        pdf = f.read()

    objects = {}
    for m in re.finditer(rb'(\d+)\s+0\s+obj\b(.*?)endobj', pdf, re.DOTALL):
        obj_id = int(m.group(1))
        objects[obj_id] = m.group(2)

    global_fonts = {}
    for obj_id, body in objects.items():
        font_matches = re.findall(rb'/(F\d+)\s+(\d+)\s+0\s+R', body)
        for fname, fid in font_matches:
            fname_str = "/" + fname.decode()
            fid = int(fid)
            fobj = objects.get(fid, b'')
            tu = re.search(rb'/ToUnicode\s+(\d+)\s+0\s+R', fobj)
            if tu:
                tu_id = int(tu.group(1))
                cmap_obj = objects.get(tu_id, b'')
                sm = re.search(rb'stream[\r\n]+(.*?)[\r\n]+endstream', cmap_obj, re.DOTALL)
                if sm:
                    decomp = decompress_stream(sm.group(1))
                    if decomp:
                        cmap_str = decomp.decode('latin1', 'ignore')
                        global_fonts[fname_str] = parse_cmap(cmap_str)

    pages = []
    for obj_id, body in objects.items():
        if re.search(rb'/Type\s*/Page\b', body) and not re.search(rb'/Type\s*/Pages\b', body):
            pages.append((obj_id, body))

    kids = []
    for obj_id, body in objects.items():
        if re.search(rb'/Type\s*/Pages\b', body):
            km = re.findall(rb'(\d+)\s+0\s+R', body)
            for k in km:
                kid_id = int(k)
                if kid_id in [p[0] for p in pages] and kid_id not in kids:
                    kids.append(kid_id)

    if kids and len(kids) == len(pages):
        ordered_pages = [(kid_id, objects[kid_id]) for kid_id in kids]
    else:
        ordered_pages = sorted(pages, key=lambda x: x[0])

    print(f"Total pages: {len(ordered_pages)}. Fonts resolved: {len(global_fonts)}")

    page_texts = []

    for page_idx, (page_id, page_body) in enumerate(ordered_pages):
        content_matches = re.findall(rb'/Contents\s+(\d+)\s+0\s+R', page_body)
        if not content_matches:
            arr_match = re.search(rb'/Contents\s*\[(.*?)\]', page_body, re.DOTALL)
            if arr_match:
                content_matches = re.findall(rb'(\d+)\s+0\s+R', arr_match.group(1))

        # We want to extract text elements with their Y position to sort them properly
        # Each BT block typically has (x, y) coordinates from Td / Tm
        text_elements = [] # list of (y, x, text)

        for cid in content_matches:
            c_obj = objects.get(int(cid), b'')
            sm = re.search(rb'stream[\r\n]+(.*?)[\r\n]+endstream', c_obj, re.DOTALL)
            if sm:
                c_decomp = decompress_stream(sm.group(1))
                if not c_decomp:
                    continue

                for bt_match in re.finditer(rb'BT\s+(.*?)\s+ET', c_decomp, re.DOTALL):
                    bt_chunk = bt_match.group(1)
                    
                    # Track font, x, y
                    current_font = None
                    cur_x = 0.0
                    cur_y = 0.0
                    
                    # Split into instructions or tokenize
                    # Instructions:
                    # 107.4 691.089 Td
                    # /F1 36 Tf
                    # [...] TJ or <...> Tj or (...) Tj
                    # T*
                    tokens = re.finditer(rb'(-?[\d\.]+)\s+(-?[\d\.]+)\s+Td|/(\w+)\s+[\d\.]+\s+Tf|\[(.*?)\]\s*TJ|<([0-9A-Fa-f]+)>\s*Tj|\(((?:[^()\\]|\\.)*)\)\s*Tj|\bT\*\b', bt_chunk, re.DOTALL)
                    
                    bt_texts = []
                    
                    for tok in tokens:
                        if tok.group(1): # Td
                            cur_x += float(tok.group(1))
                            cur_y += float(tok.group(2))
                        elif tok.group(3): # Tf
                            current_font = "/" + tok.group(3).decode()
                        elif tok.group(4): # [...] TJ
                            font_info = global_fonts.get(current_font)
                            c_len, cmap = font_info if font_info else (2, {})
                            raw_arr = tok.group(4)
                            # In TJ, can have hex strings or numbers: <0102>-1<03>
                            # Numbers < -150 often mean word space if space isn't in cmap
                            parts = re.finditer(rb'<([0-9A-Fa-f]+)>|(-?\d+)', raw_arr)
                            chunk = ""
                            for p in parts:
                                if p.group(1):
                                    hx_str = p.group(1).decode()
                                    for i in range(0, len(hx_str), c_len):
                                        cid_val = int(hx_str[i:i+c_len], 16)
                                        chunk += cmap.get(cid_val, "")
                                elif p.group(2):
                                    val = int(p.group(2))
                                    # Large kerning usually indicates space
                                    if val < -250 and not chunk.endswith(" "):
                                        chunk += " "
                            if chunk:
                                bt_texts.append(chunk)
                        elif tok.group(5): # <...> Tj
                            font_info = global_fonts.get(current_font)
                            c_len, cmap = font_info if font_info else (2, {})
                            hx_str = tok.group(5).decode()
                            chunk = ""
                            for i in range(0, len(hx_str), c_len):
                                cid_val = int(hx_str[i:i+c_len], 16)
                                chunk += cmap.get(cid_val, "")
                            if chunk:
                                bt_texts.append(chunk)
                        elif tok.group(6): # (...) Tj
                            bt_texts.append(tok.group(6).decode('latin1', 'ignore'))
                        elif tok.group(0) == b'T*':
                            cur_y -= 12.0 # approx line height
                    
                    if bt_texts:
                        combined = "".join(bt_texts)
                        if combined.strip():
                            text_elements.append((cur_y, cur_x, combined))

        # Sort elements by Y descending (top to bottom), then X ascending (left to right)
        # In PDF, Y=0 is bottom, Y=842 is top!
        # Group lines with similar Y (within 3pt)
        text_elements.sort(key=lambda item: (-item[0], item[1]))

        # Group lines
        lines = []
        if text_elements:
            current_line_y = text_elements[0][0]
            current_line_parts = []
            
            for y, x, text in text_elements:
                if abs(y - current_line_y) < 4.0:
                    current_line_parts.append(text)
                else:
                    line_str = " ".join(current_line_parts).strip()
                    # Collapse multiple spaces
                    line_str = re.sub(r'[ \t]+', ' ', line_str)
                    if line_str:
                        lines.append(line_str)
                    current_line_y = y
                    current_line_parts = [text]
                    
            if current_line_parts:
                line_str = " ".join(current_line_parts).strip()
                line_str = re.sub(r'[ \t]+', ' ', line_str)
                if line_str:
                    lines.append(line_str)

        page_texts.append(f"=== PÁGINA {page_idx + 1} ===\n" + "\n".join(lines))

    return "\n\n".join(page_texts)

if __name__ == '__main__':
    result = extract_pdf(sys.argv[1])
    out_file = sys.argv[1].replace(".pdf", "_extracted.txt")
    with open(out_file, "w", encoding="utf-8") as out:
        out.write(result)
    print(f"Extracted to {out_file}, length: {len(result)} chars")
