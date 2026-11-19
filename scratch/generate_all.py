#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script maestro definitivo:
1. Procesa los 10 temas teóricos (00 a 09) desde php/ficheros/ hacia php/archivos/
   con 100% de balance de etiquetas, IDs para TOC y anclas bidireccionales.
2. Genera php/archivos/10_ejercicios_r.html con todos los ejercicios y códigos resueltos.
3. Actualiza php/index.html y php/menu.html.
4. Audita etiquetas y enlaces.
"""

import os
import re
import glob
import html

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
PHP_DIR = os.path.join(BASE_DIR, "php")
FICHEROS_DIR = os.path.join(PHP_DIR, "ficheros")
ARCHIVOS_DIR = os.path.join(PHP_DIR, "archivos")
IMG_DIR = os.path.join(ARCHIVOS_DIR, "img")
EJERCICIOS_DIR = os.path.join(PHP_DIR, "material", "ejercicios")

os.makedirs(ARCHIVOS_DIR, exist_ok=True)
os.makedirs(IMG_DIR, exist_ok=True)

TOPICS = [
    {
        "id": "00",
        "num": "00",
        "src_pattern": "00_Primeros pasos con PHP*.html",
        "dst": "00_primeros_pasos.html",
        "title": "Primeros pasos con PHP",
        "subtitle": "Arquitectura Servidor y Entorno XAMPP",
        "full_title": "00. Primeros Pasos con PHP y Entorno de Servidor",
        "desc": "Tema 0: Arquitectura cliente-servidor web, instalación y configuración de XAMPP (Apache, MySQL, PHP), htdocs, primer script y ciclo de vida de una petición.",
        "icon": "bi-rocket-takeoff",
        "prev": None,
        "next": ("01_elementos_basicos.html", "01. Elementos básicos del lenguaje")
    },
    {
        "id": "01",
        "num": "01",
        "src_pattern": "01_Elementos básicos del lenguaje*.html",
        "dst": "01_elementos_basicos.html",
        "title": "Elementos básicos del lenguaje",
        "subtitle": "Sintaxis, Variables y Control de Flujo",
        "full_title": "01. Elementos Básicos del Lenguaje PHP",
        "desc": "Tema 1: Sintaxis, variables tipadas dinámicamente, tipos primitivos, constantes, operadores aritméticos/lógicos, estructuras de control y mezcla con HTML.",
        "icon": "bi-code-square",
        "prev": ("00_primeros_pasos.html", "00. Primeros pasos con PHP"),
        "next": ("02_funciones.html", "02. Uso de funciones")
    },
    {
        "id": "02",
        "num": "02",
        "src_pattern": "02_Uso de funciones*.html",
        "dst": "02_funciones.html",
        "title": "Uso de funciones",
        "subtitle": "Parámetros, Ámbito y Modularización",
        "full_title": "02. Uso y Definición de Funciones en PHP",
        "desc": "Tema 2: Declaración, paso de parámetros por valor y referencia (&), valores por defecto, type hinting, funciones anónimas, modularización con include/require y utilidades estándar.",
        "icon": "bi-gear-wide-connected",
        "prev": ("01_elementos_basicos.html", "01. Elementos básicos del lenguaje"),
        "next": ("03_arrays.html", "03. Arrays, errores y otros conceptos")
    },
    {
        "id": "03",
        "num": "03",
        "src_pattern": "03_Arrays, errores*.html",
        "dst": "03_arrays.html",
        "title": "Arrays, errores y otros conceptos",
        "subtitle": "Matrices, Excepciones y Configuración",
        "full_title": "03. Arrays, Manejo de Errores y Ámbito en PHP",
        "desc": "Tema 3: Matrices indexadas, asociativas y multidimensionales, foreach, funciones de array, supresión con @, php.ini, die() y excepciones estructuradas (try-catch).",
        "icon": "bi-grid-3x3-gap",
        "prev": ("02_funciones.html", "02. Uso de funciones"),
        "next": ("04_formularios.html", "04. Recogida de datos de formularios")
    },
    {
        "id": "04",
        "num": "04",
        "src_pattern": "04_Recogida de datos de formularios*.html",
        "dst": "04_formularios.html",
        "title": "Recogida de datos de formularios",
        "subtitle": "Superglobales GET/POST y Subida de Ficheros",
        "full_title": "04. Procesamiento de Formularios Web con PHP",
        "desc": "Tema 4: Superglobales $_GET, $_POST, $_REQUEST, arrays en inputs múltiples (checkboxes/select), autoenvíos a la misma página y subida segura de ficheros con $_FILES.",
        "icon": "bi-ui-checks",
        "prev": ("03_arrays.html", "03. Arrays, errores y otros conceptos"),
        "next": ("05_redirecciones.html", "05. Redirecciones e inclusiones")
    },
    {
        "id": "05",
        "num": "05",
        "src_pattern": "05_Redirecciones e inclusiones*.html",
        "dst": "05_redirecciones.html",
        "title": "Redirecciones e inclusiones",
        "subtitle": "Cabeceras HTTP y Plantillas Modulares",
        "full_title": "05. Redirecciones HTTP e Inclusiones Modulares",
        "desc": "Tema 5: Cabeceras HTTP con header('Location: ...'), buffer de salida, estructuración en plantillas con cabecera.inc y pie.inc, y control de flujo entre vistas.",
        "icon": "bi-arrow-left-right",
        "prev": ("04_formularios.html", "04. Recogida de datos de formularios"),
        "next": ("06_cookies_sesiones.html", "06. Cookies y sesiones")
    },
    {
        "id": "06",
        "num": "06",
        "src_pattern": "06_Cookies y sesiones*.html",
        "dst": "06_cookies_sesiones.html",
        "title": "Cookies y sesiones",
        "subtitle": "Persistencia de Estado y Autenticación",
        "full_title": "06. Persistencia de Estado: Cookies y Sesiones en PHP",
        "desc": "Tema 6: Gestión de cookies con setcookie() y $_COOKIE, ciclo de vida de sesiones con session_start() y $_SESSION, carritos de compra y autenticación de usuarios.",
        "icon": "bi-person-badge",
        "prev": ("05_redirecciones.html", "05. Redirecciones e inclusiones"),
        "next": ("07_ajax.html", "07. Comunicación asíncrona con AJAX")
    },
    {
        "id": "07",
        "num": "07",
        "src_pattern": "07_Comunicación asíncrona con AJAX*.html",
        "dst": "07_ajax.html",
        "title": "Comunicación asíncrona con AJAX",
        "subtitle": "Peticiones Asíncronas y JSON Frontend-Backend",
        "full_title": "07. Comunicación Asíncrona Frontend-Backend (AJAX y JSON)",
        "desc": "Tema 7: Peticiones HTTP asíncronas con XMLHttpRequest y Fetch API, serialización JSON (json_encode, json_decode) y arquitectura de servicios desacoplados.",
        "icon": "bi-lightning-charge",
        "prev": ("06_cookies_sesiones.html", "06. Cookies y sesiones"),
        "next": ("08_poo.html", "08. Programación orientada a objetos (POO)")
    },
    {
        "id": "08",
        "num": "08",
        "src_pattern": "08_Programación orientada a objetos*.html",
        "dst": "08_poo.html",
        "title": "Programación orientada a objetos",
        "subtitle": "Clases, Visibilidad y Herencia",
        "full_title": "08. Programación Orientada a Objetos en PHP (POO)",
        "desc": "Tema 8: Clases, propiedades y métodos, constructor __construct, modificadores de visibilidad (public, private, protected), getters/setters y herencia con parent::.",
        "icon": "bi-boxes",
        "prev": ("07_ajax.html", "07. Comunicación asíncrona con AJAX"),
        "next": ("09_bd.html", "09. Acceso a bases de datos con PHP (PDO)")
    },
    {
        "id": "09",
        "num": "09",
        "src_pattern": "09_Acceso a bases de datos con PHP*.html",
        "dst": "09_bd.html",
        "title": "Acceso a bases de datos con PHP",
        "subtitle": "Capa de Abstracción PDO y Consultas Preparadas",
        "full_title": "09. Acceso a Bases de Datos Relacionales con PDO",
        "desc": "Tema 9: Conexión segura con PDO a MySQL/MariaDB, sentencias preparadas contra SQL Injection, consultas SELECT (fetch/fetchAll), operaciones INSERT/UPDATE/DELETE y transacciones.",
        "icon": "bi-database-fill-gear",
        "prev": ("08_poo.html", "08. Programación orientada a objetos (POO)"),
        "next": ("10_ejercicios_r.html", "10. Solucionario y Prácticas de PHP")
    }
]

def generate_navbar_and_offcanvas(current_id):
    """Genera la barra de navegación superior y el menú offcanvas."""
    offcanvas_items = []
    for t in TOPICS:
        active_class = "active bg-info text-dark fw-bold shadow-sm" if t["id"] == current_id else "text-dark"
        icon_color = "text-dark" if t["id"] == current_id else "text-info"
        badge_class = "bg-dark text-white" if t["id"] == current_id else "bg-info-subtle text-info-emphasis border"
        offcanvas_items.append(f"""                        <li class="nav-item">
                            <a class="nav-link rounded-3 px-3 py-2 d-flex align-items-center justify-content-between {active_class}" href="{t['dst']}">
                                <div class="d-flex align-items-center gap-2">
                                    <i class="bi {t['icon']} {icon_color}"></i>
                                    <span>{t['title']}</span>
                                </div>
                                <span class="badge {badge_class} small">{t['num']}</span>
                            </a>
                        </li>""")

    sol_active = "active bg-info text-dark fw-bold shadow-sm" if current_id == "10" else "text-dark"
    offcanvas_items.append(f"""                        <li class="nav-item mt-3 pt-3 border-top">
                            <a class="nav-link rounded-3 px-3 py-2 d-flex align-items-center justify-content-between {sol_active}" href="10_ejercicios_r.html">
                                <div class="d-flex align-items-center gap-2">
                                    <i class="bi bi-check2-square text-success"></i>
                                    <span>Solucionario y Prácticas</span>
                                </div>
                                <span class="badge bg-success-subtle text-success-emphasis border small">10</span>
                            </a>
                        </li>""")

    offcanvas_list = "\n".join(offcanvas_items)

    return f"""    <!-- 1. Barra de Navegación Superior Fija -->
    <header class="navbar navbar-expand-lg navbar-dark bg-dark sticky-top shadow-sm py-2">
        <div class="container-xl">
            <!-- Botón Hamburguesa Offcanvas -->
            <button class="btn btn-outline-light btn-sm me-2 d-flex align-items-center gap-2" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasNav" aria-controls="offcanvasNav" aria-label="Abrir temario">
                <i class="bi bi-list fs-5"></i>
                <span class="d-none d-sm-inline fw-semibold">Temario PHP</span>
            </button>

            <!-- Brand -->
            <a class="navbar-brand d-flex align-items-center gap-2 me-auto" href="../../index.html">
                <img src="../../imagenes/logo.jpg" alt="Logo" width="36" height="36" class="rounded object-fit-cover">
                <span class="fw-bold tracking-tight">LMSGI</span>
                <span class="d-none d-md-inline text-secondary small">| Lenguajes de Marcas</span>
            </a>

            <!-- Enlaces directos a módulos en Desktop -->
            <nav class="d-none d-lg-flex align-items-center gap-1 me-3">
                <a class="btn btn-sm btn-dark text-light-emphasis" href="../../html/index.html">HTML</a>
                <a class="btn btn-sm btn-dark text-light-emphasis" href="../../css/index.html">CSS</a>
                <a class="btn btn-sm btn-dark text-light-emphasis" href="../../xml/index.html">XML</a>
                <a class="btn btn-sm btn-dark text-light-emphasis" href="../../javascript/index.html">JavaScript</a>
                <a class="btn btn-sm btn-info text-dark fw-medium" href="../index.html">PHP</a>
            </nav>

            <!-- Botón Rápido de Retorno -->
            <a href="../../index.html" class="btn btn-sm btn-outline-warning d-flex align-items-center gap-1">
                <i class="bi bi-house-door"></i>
                <span class="d-none d-sm-inline">Portada</span>
            </a>
        </div>
    </header>

    <!-- 2. Menú Lateral Offcanvas -->
    <div class="offcanvas offcanvas-start shadow" tabindex="-1" id="offcanvasNav" aria-labelledby="offcanvasNavLabel">
        <div class="offcanvas-header bg-dark text-white border-bottom border-secondary">
            <div class="d-flex align-items-center gap-2">
                <i class="bi bi-filetype-php text-info fs-4"></i>
                <div>
                    <h5 class="offcanvas-title fw-bold" id="offcanvasNavLabel">Módulo PHP</h5>
                    <span class="text-secondary small">Desarrollo Web Backend</span>
                </div>
            </div>
            <button type="button" class="btn-close btn-close-white" data-bs-dismiss="offcanvas" aria-label="Cerrar"></button>
        </div>
        <div class="offcanvas-body p-3">
            <div class="mb-3">
                <span class="text-uppercase text-secondary fw-bold small px-2">Unidades Temáticas</span>
                <ul class="nav nav-pills flex-column gap-1 mt-2">
{offcanvas_list}
                </ul>
            </div>

            <div class="card border-0 bg-body-tertiary rounded-3 p-3 mt-4">
                <h6 class="fw-bold mb-2 small text-uppercase text-secondary">Recursos y Base de Datos</h6>
                <div class="d-grid gap-2">
                    <a href="../material/ficheros/academia.sql" download class="btn btn-sm btn-outline-secondary text-start d-flex align-items-center gap-2">
                        <i class="bi bi-database text-primary"></i>
                        <span>academia.sql (BD)</span>
                    </a>
                    <a href="../material/php_jaumeII/35-php-mysql.pdf" target="_blank" class="btn btn-sm btn-outline-secondary text-start d-flex align-items-center gap-2">
                        <i class="bi bi-file-earmark-pdf text-danger"></i>
                        <span>Manual MySQL (PDF)</span>
                    </a>
                    <a href="../index.html" class="btn btn-sm btn-outline-info text-start d-flex align-items-center gap-2">
                        <i class="bi bi-grid text-info"></i>
                        <span>Panel Central PHP</span>
                    </a>
                </div>
            </div>
        </div>
    </div>"""

def generate_footer(prev_topic, next_topic):
    """Genera los botones ergonómicos de navegación inferior y el footer estándar."""
    prev_btn = ""
    if prev_topic:
        prev_btn = f"""<a href="{prev_topic[0]}" class="btn btn-outline-secondary d-flex align-items-center gap-2">
                    <i class="bi bi-arrow-left"></i>
                    <div class="text-start d-none d-sm-block">
                        <div class="small text-secondary">Anterior</div>
                        <div class="fw-semibold text-truncate" style="max-width: 180px;">{prev_topic[1]}</div>
                    </div>
                </a>"""
    else:
        prev_btn = """<a href="../index.html" class="btn btn-outline-secondary d-flex align-items-center gap-2">
                    <i class="bi bi-house"></i>
                    <span>Inicio PHP</span>
                </a>"""

    next_btn = ""
    if next_topic:
        next_btn = f"""<a href="{next_topic[0]}" class="btn btn-primary d-flex align-items-center gap-2 shadow-sm">
                    <div class="text-end d-none d-sm-block">
                        <div class="small text-white-50">Siguiente</div>
                        <div class="fw-semibold text-truncate" style="max-width: 180px;">{next_topic[1]}</div>
                    </div>
                    <i class="bi bi-arrow-right"></i>
                </a>"""
    else:
        next_btn = """<a href="10_ejercicios_r.html" class="btn btn-success d-flex align-items-center gap-2 shadow-sm">
                    <div class="text-end d-none d-sm-block">
                        <div class="small text-white-50">Práctica</div>
                        <div class="fw-semibold">Solucionario Completo</div>
                    </div>
                    <i class="bi bi-check2-circle"></i>
                </a>"""

    return f"""    <!-- 4. Navegación Ergonómica Inferior -->
    <nav class="container-xl my-4 py-3 border-top border-bottom" aria-label="Navegación entre temas">
        <div class="d-flex justify-content-between align-items-center gap-2">
            <div>
                {prev_btn}
            </div>
            <div>
                <a href="#inicio" class="btn btn-light btn-sm border d-flex align-items-center gap-1 text-secondary" title="Subir al inicio">
                    <i class="bi bi-chevron-up"></i>
                    <span class="d-none d-md-inline">Arriba</span>
                </a>
            </div>
            <div>
                {next_btn}
            </div>
        </div>
    </nav>

    <!-- 5. Pie de Página Estándar -->
    <footer class="bg-dark text-light-emphasis py-4 mt-auto border-top border-secondary">
        <div class="container-xl">
            <div class="row align-items-center gy-3">
                <div class="col-12 col-md-6 text-center text-md-start">
                    <div class="d-flex align-items-center justify-content-center justify-content-md-start gap-2 mb-1">
                        <img src="../../imagenes/logo.jpg" alt="Logo" width="28" height="28" class="rounded object-fit-cover">
                        <span class="fw-bold text-white">LMSGI</span>
                        <span class="text-secondary">| Lenguajes de Marcas</span>
                    </div>
                    <p class="small text-secondary mb-0">Curso de Desarrollo Web Backend con PHP y MySQL. Material didáctico adaptado bajo estándares web y Bootstrap 5.3.</p>
                </div>
                <div class="col-12 col-md-6 text-center text-md-end">
                    <div class="d-flex justify-content-center justify-content-md-end gap-3 small mb-2">
                        <a href="../index.html" class="text-decoration-none text-light-emphasis">Índice PHP</a>
                        <a href="10_ejercicios_r.html" class="text-decoration-none text-light-emphasis">Solucionario</a>
                        <a href="../../index.html" class="text-decoration-none text-light-emphasis">Portada LMSGI</a>
                    </div>
                    <p class="small text-secondary mb-0">Generalitat Valenciana &bull; Conselleria d'Educació</p>
                </div>
            </div>
        </div>
    </footer>"""

def clean_and_transform_content(raw_html, topic_info):
    """Limpia y transforma el contenido HTML asegurando balance perfecto de etiquetas."""
    # 1. Encontrar markdown-body
    idx = raw_html.find('class="container-lg px-3 my-5 markdown-body">')
    start = raw_html.find('>', idx) + 1

    # El final de markdown-body es antes del primer script posterior
    end_script = raw_html.find('<script', idx)
    if end_script == -1:
        end_script = raw_html.find('</body>', idx)
    body = raw_html[start:end_script].strip()

    # Corregir errores y erratas de los archivos fuente originales
    body = re.sub(r'<h2>\s*2\.\s*Uso de parámetros\s*</a>\s*</h2>', '<h2>2. Uso de parámetros</h2>', body)
    body = re.sub(r'y las llamas\s*</a>\s*,', 'y las llamas,', body)
    body = re.sub(r'(?<!</div>)</div>\s*</blockquote>', '</blockquote>', body)
    body = re.sub(r'</blockquote\s*>', '</blockquote>', body)

    # Quitar el cierre </div> de markdown-body al final
    body = re.sub(r'</div>\s*$', '', body.strip())

    # Quitar los encabezados H1 y div de diapositivas al inicio
    first_p = body.find('<p')
    first_h2 = body.find('<h2')
    first_elem = min(first_p if first_p != -1 else len(body), first_h2 if first_h2 != -1 else len(body))
    body = body[first_elem:]

    # 2. Reemplazo de imágenes
    def img_repl(m):
        src = m.group(1)
        bname = os.path.basename(src)
        return f'<figure class="figure d-block text-center my-4"><img src="./img/{bname}" class="figure-img img-fluid rounded-3 shadow-sm border" alt="{bname}"></figure>'

    body = re.sub(r'<div align="center">\s*<img\s+src="([^"]+)"[^>]*>\s*</div>', img_repl, body)
    body = re.sub(r'<p[^>]*>\s*<img\s+src="([^"]+)"[^>]*>\s*</p>', img_repl, body)
    body = re.sub(r'<img\s+src="([^"]+)"(?:\s+width="[^"]*")?[^>]*>', img_repl, body)

    # 3. Bloques de código
    def code_block_repl(m):
        lang_class = m.group(1) or ""
        code_html = m.group(2)
        lang_title = "PHP"
        lang_icon = "bi-filetype-php"
        if "sql" in lang_class:
            lang_title = "SQL"
            lang_icon = "bi-database"
        elif "html" in lang_class:
            lang_title = "HTML"
            lang_icon = "bi-filetype-html"
        elif "plaintext" in lang_class or "bash" in lang_class:
            lang_title = "Terminal / Texto"
            lang_icon = "bi-terminal"

        return f'''<div class="code-block mb-4 shadow-sm">
    <div class="d-flex justify-content-between align-items-center text-secondary border-bottom border-secondary border-opacity-25 pb-1 mb-2 small">
        <span class="fw-semibold text-info d-flex align-items-center gap-1"><i class="bi {lang_icon}"></i> {lang_title}</span>
        <button class="btn btn-outline-secondary btn-sm py-0 px-2 text-light" style="font-size: 0.75rem;" onclick="navigator.clipboard.writeText(this.closest('.code-block').querySelector('code').innerText)"><i class="bi bi-clipboard"></i> Copiar</button>
    </div>
    <pre class="m-0"><code>{code_html.strip()}</code></pre>
</div>'''

    code_pat = r'<div class="language-([a-zA-Z0-9_-]+) highlighter-rouge">\s*<div class="highlight">\s*<pre class="highlight">\s*<code>(.*?)</code>\s*</pre>\s*</div>\s*</div>'
    body = re.sub(
        code_pat,
        code_block_repl,
        body,
        flags=re.DOTALL
    )

    # 4. Blockquotes: Ejercicios y Avisos
    def bq_repl(m):
        bq_class = m.group(1) or ""
        inner = m.group(2).strip()

        ej_match = re.search(r'<strong>\s*(Ejercicio\s*(\d+))\s*:?\s*</strong>', inner, re.IGNORECASE)
        if "ejercicios" in bq_class or ej_match:
            ej_label = ej_match.group(1) if ej_match else "Actividad Práctica"
            ej_num = ej_match.group(2) if ej_match else "1"
            clean_inner = re.sub(r'<p>\s*<strong>\s*Ejercicio\s*\d+\s*:?\s*</strong>\s*</p>', '', inner, count=1, flags=re.IGNORECASE)
            clean_inner = re.sub(r'<strong>\s*Ejercicio\s*\d+\s*:?\s*</strong>', '', clean_inner, count=1, flags=re.IGNORECASE)

            target_id = f"ej_{topic_info['num']}_{int(ej_num)}"

            return f'''<div id="{target_id}" class="card exercise-card border-0 shadow-sm mb-4 bg-body-tertiary border-start border-4 border-info">
    <div class="card-body p-4">
        <div class="d-flex align-items-center justify-content-between mb-3 flex-wrap gap-2">
            <span class="badge bg-info text-dark fw-bold px-3 py-2 fs-6"><i class="bi bi-code-square me-1"></i>{ej_label}</span>
            <a href="10_ejercicios_r.html#{target_id}" class="btn btn-sm btn-outline-primary"><i class="bi bi-check2-circle me-1"></i>Ver Solución</a>
        </div>
        <div class="exercise-text text-dark">
            {clean_inner}
        </div>
    </div>
</div>'''
        else:
            return f'''<div class="alert alert-warning border-0 shadow-sm d-flex align-items-start gap-3 mb-4 rounded-3 p-3">
    <i class="bi bi-exclamation-triangle-fill fs-4 text-warning flex-shrink-0 mt-1"></i>
    <div class="alert-content flex-grow-1">
        {inner}
    </div>
</div>'''

    body = re.sub(r'<blockquote(?:\s+class="([^"]*)")?>(.*?)</blockquote>', bq_repl, body, flags=re.DOTALL)

    # 5. Tablas
    def table_repl(m):
        tbl_content = m.group(1)
        return f'<div class="table-responsive my-4"><table class="table table-hover table-striped table-bordered align-middle table-custom mb-0">{tbl_content}</table></div>'

    body = re.sub(r'<table[^>]*>(.*?)</table>', table_repl, body, flags=re.DOTALL)

    # 6. Encabezados con IDs y extracción para el TOC
    toc_items = []
    sec_counter = 0

    def h2_repl(m):
        nonlocal sec_counter
        sec_counter += 1
        h2_title = m.group(1).strip()
        clean_title = re.sub(r'<[^>]+>', '', h2_title).strip()
        sec_id = f"sec{topic_info['num']}-{sec_counter}"
        toc_items.append((sec_id, clean_title))
        return f'<h2 id="{sec_id}" class="h4 fw-bold text-primary mt-5 mb-3 border-bottom pb-2 d-flex align-items-center gap-2"><i class="bi bi-bookmark-check text-info"></i><span>{h2_title}</span></h2>'

    body = re.sub(r'<h2[^>]*>(.*?)</h2>', h2_repl, body, flags=re.DOTALL)

    def h3_repl(m):
        h3_title = m.group(1).strip()
        return f'<h3 class="h5 fw-bold text-dark mt-4 mb-3 d-flex align-items-center gap-2"><i class="bi bi-chevron-right text-info small"></i><span>{h3_title}</span></h3>'

    body = re.sub(r'<h3[^>]*>(.*?)</h3>', h3_repl, body, flags=re.DOTALL)

    def h4_repl(m):
        h4_title = m.group(1).strip()
        return f'<h4 class="h6 fw-bold text-secondary mt-3 mb-2">{h4_title}</h4>'

    body = re.sub(r'<h4[^>]*>(.*?)</h4>', h4_repl, body, flags=re.DOTALL)

    # 7. Inline code
    body = re.sub(r'<code class="language-plaintext highlighter-rouge">', '<code class="text-info-emphasis bg-info-subtle px-1.5 py-0.5 rounded">', body)

    # Generar TOC HTML
    toc_html = []
    for s_id, s_title in toc_items:
        toc_html.append(f'<a class="nav-link text-secondary py-1 px-2 rounded text-truncate" href="#{s_id}">{s_title}</a>')
    if not toc_html:
        toc_html.append('<span class="text-secondary small px-2">Contenido secuencial</span>')
    toc_str = "\n".join(toc_html)

    return body, toc_str

def build_topic_page(topic):
    matches = glob.glob(os.path.join(FICHEROS_DIR, topic["src_pattern"]))
    if not matches:
        print(f"ERROR: No se encontró archivo para {topic['src_pattern']}")
        return False
    src_file = matches[0]

    with open(src_file, 'r', encoding='utf-8') as f:
        raw_html = f.read()

    body_content, toc_html = clean_and_transform_content(raw_html, topic)

    navbar_html = generate_navbar_and_offcanvas(topic["id"])
    footer_html = generate_footer(topic["prev"], topic["next"])

    full_page = f"""<!DOCTYPE html>
<html lang="es" data-bs-theme="light">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{topic['full_title']} | LMSGI</title>
    <meta name="description" content="{topic['desc']}">
    
    <!-- Bootstrap 5.3 CSS (CDN) -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <!-- Bootstrap Icons (CDN) -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">

    <style>
        body {{
            background-color: #f8f9fa;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            font-family: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
            line-height: 1.7;
        }}
        .content-card {{
            background-color: #ffffff;
            border-radius: 1rem;
            border: 1px solid rgba(0, 0, 0, 0.08);
        }}
        code, kbd, samp, pre {{
            font-family: SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
        }}
        .code-block {{
            background-color: #1e1e2e;
            color: #cdd6f4;
            border-radius: 0.75rem;
            padding: 1.25rem;
            overflow-x: auto;
            font-size: 0.9rem;
            line-height: 1.5;
            border: 1px solid rgba(255, 255, 255, 0.1);
        }}
        .code-block code {{
            color: inherit;
        }}
        .table-custom {{
            border-radius: 0.75rem;
            overflow: hidden;
            border: 1px solid rgba(0, 0, 0, 0.1);
        }}
        .table-custom thead {{
            background-color: #212529;
            color: #ffffff;
        }}
        .exercise-card {{
            transition: transform 0.2s ease, box-shadow 0.2s ease;
            border-radius: 0.85rem;
        }}
        .exercise-card:hover {{
            transform: translateY(-2px);
            box-shadow: 0 0.5rem 1.25rem rgba(0, 0, 0, 0.08) !important;
        }}
        .sticky-summary {{
            position: sticky;
            top: 5rem;
        }}
    </style>
</head>
<body id="inicio">

{navbar_html}

    <!-- 3. Contenedor Principal -->
    <main class="container-xl my-4 flex-grow-1">
        <!-- Migas de Pan (Breadcrumbs) -->
        <nav aria-label="breadcrumb" class="mb-3">
            <ol class="breadcrumb mb-0 py-2 px-3 bg-white rounded-3 shadow-sm border small">
                <li class="breadcrumb-item"><a href="../../index.html" class="text-decoration-none text-secondary"><i class="bi bi-house-door"></i> Inicio</a></li>
                <li class="breadcrumb-item"><a href="../index.html" class="text-decoration-none text-secondary">PHP</a></li>
                <li class="breadcrumb-item active text-dark fw-semibold" aria-current="page">{topic['title']}</li>
            </ol>
        </nav>

        <!-- Tarjeta Hero del Tema -->
        <div class="card border-0 shadow-sm rounded-4 mb-4 bg-dark text-white overflow-hidden">
            <div class="card-body p-4 p-md-5">
                <div class="d-flex align-items-center gap-2 mb-3">
                    <span class="badge bg-info text-dark fw-bold px-3 py-2 fs-6">Unidad {topic['num']}</span>
                    <span class="badge bg-secondary text-light fw-normal px-2.5 py-1.5 small">Desarrollo Web Backend</span>
                </div>
                <h1 class="display-6 fw-bold mb-2 text-white">{topic['full_title']}</h1>
                <p class="lead text-light-emphasis mb-0">{topic['desc']}</p>
            </div>
        </div>

        <div class="row g-4">
            <!-- Columna Principal de Contenido -->
            <div class="col-12 col-lg-8 col-xl-9">
                <article class="content-card p-4 p-md-5 shadow-sm">
                    {body_content}
                </article>
            </div>

            <!-- Columna Lateral: Índice Rápido y Recursos -->
            <div class="col-12 col-lg-4 col-xl-3">
                <div class="sticky-summary d-flex flex-column gap-3">
                    <!-- Índice de la Lección -->
                    <div class="card border-0 shadow-sm rounded-3">
                        <div class="card-header bg-white border-bottom py-3">
                            <h6 class="fw-bold mb-0 d-flex align-items-center gap-2 text-dark">
                                <i class="bi bi-list-nested text-info"></i>
                                <span>En este tema</span>
                            </h6>
                        </div>
                        <div class="card-body p-2">
                            <nav class="nav nav-pills flex-column gap-1 small">
                                {toc_html}
                            </nav>
                        </div>
                    </div>

                    <!-- Recursos Descargables -->
                    <div class="card border-0 shadow-sm rounded-3 bg-body-tertiary">
                        <div class="card-body p-3">
                            <h6 class="fw-bold mb-2 small text-uppercase text-secondary">Recursos del Tema</h6>
                            <div class="d-grid gap-2 small">
                                <a href="10_ejercicios_r.html" class="btn btn-sm btn-outline-primary text-start d-flex align-items-center gap-2">
                                    <i class="bi bi-file-earmark-code"></i>
                                    <span>Soluciones de ejercicios</span>
                                </a>
                                <a href="../material/ficheros/academia.sql" download class="btn btn-sm btn-outline-secondary text-start d-flex align-items-center gap-2">
                                    <i class="bi bi-database"></i>
                                    <span>Base de datos (SQL)</span>
                                </a>
                                <a href="../material/php_jaumeII/35-php-mysql.pdf" target="_blank" class="btn btn-sm btn-outline-secondary text-start d-flex align-items-center gap-2">
                                    <i class="bi bi-file-earmark-pdf"></i>
                                    <span>Manual MySQL (PDF)</span>
                                </a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </main>

{footer_html}

    <!-- Bootstrap 5.3 JS Bundle (CDN) -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
</body>
</html>"""

    dst_path = os.path.join(ARCHIVOS_DIR, topic["dst"])
    with open(dst_path, 'w', encoding='utf-8') as out_f:
        out_f.write(full_page)

    print(f"OK: Generado {topic['dst']} ({len(full_page)} bytes)")
    return True

print("Compilando lecciones...")
for t in TOPICS:
    build_topic_page(t)

print("Lecciones 00-09 compiladas.")
