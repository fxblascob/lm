import zlib, re, sys

def extract_pdf_text(pdf_path):
    with open(pdf_path, 'rb') as f:
        content = f.read()

    streams = re.findall(b'stream[\r\n]+(.*?)[\r\n]+endstream', content, re.DOTALL)
    pages_text = []

    for s in streams:
        try:
            data = zlib.decompress(s).decode('latin1', errors='ignore')
            # Look for BT ... ET blocks
            bt_blocks = re.findall(r'BT\s+(.*?)\s+ET', data, re.DOTALL)
            for bt in bt_blocks:
                # Find (string) Tj or ' or "
                items = re.findall(r'\(((?:[^()\\]|\\.)*)\)\s*(?:Tj|\'|")', bt)
                # Find [...] TJ
                array_items = re.findall(r'\[(.*?)\]\s*TJ', bt, re.DOTALL)
                for arr in array_items:
                    parts = re.findall(r'\(((?:[^()\\]|\\.)*)\)', arr)
                    if parts:
                        items.append("".join(parts))
                if items:
                    line = " ".join(items)
                    # replace escapes
                    line = line.replace('\\(', '(').replace('\\)', ')').replace('\\n', '\n').replace('\\r', '\r').replace('\\t', '\t')
                    pages_text.append(line)
        except Exception as e:
            pass

    return "\n".join(pages_text)

if __name__ == '__main__':
    text = extract_pdf_text(sys.argv[1])
    print(f"Total lines: {len(text.splitlines())}")
    print(f"Total chars: {len(text)}")
    with open(sys.argv[1] + ".txt", "w", encoding="utf-8") as out:
        out.write(text)
    print(f"Saved to {sys.argv[1]}.txt")
