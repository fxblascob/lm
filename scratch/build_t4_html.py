import os

def generate_t4_page():
    doc = """<!DOCTYPE html>
<html lang="es" data-bs-theme="light">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>04. Acceso al DOM y BOM | JavaScript | LMSGI</title>
    <meta name="description" content="Tema 4: Modelo de objetos del navegador (BOM), temporizadores (setTimeout, setInterval), árbol del documento (DOM), querySelector, creación dinámica de nodos, inserción, borrado y manipulación de estilos CSS.">
    
    <!-- Bootstrap 5.3 CSS (CDN) -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <!-- Bootstrap Icons (CDN) -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">

    <style>
        body {
            background-color: #f8f9fa;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            font-family: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
            line-height: 1.7;
        }
        .content-card {
            background-color: #ffffff;
            border-radius: 1rem;
            border: 1px solid rgba(0, 0, 0, 0.08);
        }
        code, kbd, samp, pre {
            font-family: SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
        }
        .code-block {
            background-color: #1e1e2e;
            color: #cdd6f4;
            border-radius: 0.75rem;
            padding: 1.25rem;
            overflow-x: auto;
            font-size: 0.9rem;
            line-height: 1.5;
            border: 1px solid rgba(255, 255, 255, 0.1);
        }
        .code-block code {
            color: inherit;
        }
        .code-token-keyword { color: #cba6f7; font-weight: 600; }
        .code-token-string { color: #a6e3a1; }
        .code-token-number { color: #fab387; }
        .code-token-comment { color: #6c7086; font-style: italic; }
        .code-token-function { color: #89b4fa; }
        .code-token-tag { color: #f38ba8; }
        .code-token-attr { color: #f9e2af; }

        .table-custom {
            border-radius: 0.75rem;
            overflow: hidden;
            border: 1px solid rgba(0, 0, 0, 0.1);
        }
        .table-custom thead {
            background-color: #212529;
            color: #ffffff;
        }
        .exercise-card {
            transition: transform 0.2s ease, box-shadow 0.2s ease;
            border-radius: 0.85rem;
        }
        .exercise-card:hover {
            transform: translateY(-2px);
            box-shadow: 0 0.5rem 1.25rem rgba(0, 0, 0, 0.08) !important;
        }
        .sticky-summary {
            position: sticky;
            top: 5rem;
        }
    </style>
</head>
<body>

    <!-- 1. Barra de Navegación Superior Fija -->
    <header class="navbar navbar-expand-lg navbar-dark bg-dark sticky-top shadow-sm py-2">
        <div class="container-xl">
            <!-- Botón Hamburguesa Offcanvas -->
            <button class="btn btn-outline-light btn-sm me-2 d-flex align-items-center gap-2" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasNav" aria-controls="offcanvasNav" aria-label="Abrir temario">
                <i class="bi bi-list fs-5"></i>
                <span class="d-none d-sm-inline fw-semibold">Temario</span>
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
                <a class="btn btn-sm btn-warning text-dark fw-medium" href="../index.html">JavaScript</a>
                <a class="btn btn-sm btn-dark text-light-emphasis" href="../../php/index.html">PHP</a>
            </nav>

            <!-- Botón Rápido de Retorno -->
            <a href="../../index.html" class="btn btn-sm btn-outline-warning d-flex align-items-center gap-1">
                <i class="bi bi-house-door"></i>
                <span class="d-none d-sm-inline">Portada</span>
            </a>
        </div>
    </header>

    <!-- 2. Menú Lateral Offcanvas -->
    <div class="offcanvas offcanvas-start text-bg-dark" tabindex="-1" id="offcanvasNav" aria-labelledby="offcanvasNavLabel">
        <div class="offcanvas-header border-bottom border-secondary">
            <h5 class="offcanvas-title d-flex align-items-center gap-2" id="offcanvasNavLabel">
                <i class="bi bi-filetype-js text-warning"></i> Módulo JavaScript
            </h5>
            <button type="button" class="btn-close btn-close-white" data-bs-dismiss="offcanvas" aria-label="Cerrar"></button>
        </div>
        <div class="offcanvas-body p-3">
            <h6 class="text-uppercase text-secondary small fw-bold mb-2">Temario de JavaScript</h6>
            <div class="list-group list-group-flush mb-4">
                <a href="../index.html" class="list-group-item list-group-item-action bg-transparent text-light border-secondary d-flex align-items-center gap-2 py-2"><i class="bi bi-filetype-js text-warning"></i> 00. Introducción al Módulo</a>
                <a href="01_introduccion.html" class="list-group-item list-group-item-action bg-transparent text-light border-secondary d-flex align-items-center gap-2 py-2"><i class="bi bi-code-square text-warning"></i> 01. Introducción y Sintaxis</a>
                <a href="02_funciones.html" class="list-group-item list-group-item-action bg-transparent text-light border-secondary d-flex align-items-center gap-2 py-2"><i class="bi bi-braces text-warning"></i> 02. Funciones y Modularidad</a>
                <a href="03_arrays.html" class="list-group-item list-group-item-action bg-transparent text-light border-secondary d-flex align-items-center gap-2 py-2"><i class="bi bi-collection text-warning"></i> 03. Arrays y Objetos</a>
                <a href="04_dom.html" class="list-group-item list-group-item-action active bg-warning text-dark border-warning fw-semibold d-flex align-items-center gap-2 py-2"><i class="bi bi-diagram-3 text-dark"></i> 04. DOM y BOM</a>
                <a href="05_eventos.html" class="list-group-item list-group-item-action bg-transparent text-light border-secondary d-flex align-items-center gap-2 py-2"><i class="bi bi-lightning-charge text-warning"></i> 05. Gestión de Eventos</a>
                <a href="06_formularios.html" class="list-group-item list-group-item-action bg-transparent text-light border-secondary d-flex align-items-center gap-2 py-2"><i class="bi bi-ui-checks text-warning"></i> 06. Validación de Formularios</a>
                <a href="07_ejercicios.html" class="list-group-item list-group-item-action bg-transparent text-light border-secondary d-flex align-items-center gap-2 py-2"><i class="bi bi-pencil-square text-warning"></i> 07. Ejercicios Prácticos</a>
                <a href="07_ejercicios_r.html" class="list-group-item list-group-item-action bg-transparent text-light border-secondary d-flex align-items-center gap-2 py-2"><i class="bi bi-check2-circle text-warning"></i> 07. Ejercicios Resueltos</a>
            </div>

            <h6 class="text-uppercase text-secondary small fw-bold mb-2">Otros Módulos</h6>
            <div class="d-flex flex-column gap-1 small">
                <a href="../../html/index.html" class="text-light-emphasis text-decoration-none py-1"><i class="bi bi-filetype-html text-primary me-2"></i> Módulo HTML</a>
                <a href="../../css/index.html" class="text-light-emphasis text-decoration-none py-1"><i class="bi bi-filetype-css text-info me-2"></i> Módulo CSS</a>
                <a href="../../xml/index.html" class="text-light-emphasis text-decoration-none py-1"><i class="bi bi-filetype-xml text-success me-2"></i> Módulo XML</a>
                <a href="../../php/index.html" class="text-light-emphasis text-decoration-none py-1"><i class="bi bi-filetype-php text-danger me-2"></i> Módulo PHP</a>
            </div>

            <div class="mt-4 pt-3 border-top border-secondary text-center">
                <a href="../../index.html" class="btn btn-outline-warning btn-sm w-100">
                    <i class="bi bi-house-door me-1"></i> Ir al Menú Principal
                </a>
            </div>
        </div>
    </div>

    <!-- 3. Contenido Principal -->
    <main class="container-xl my-4 flex-grow-1">
        
        <!-- Breadcrumb de Navegación -->
        <nav aria-label="breadcrumb" class="mb-4">
            <ol class="breadcrumb bg-body-tertiary p-2 px-3 rounded-pill border small">
                <li class="breadcrumb-item"><a href="../../index.html" class="text-decoration-none text-secondary"><i class="bi bi-house-door me-1"></i>Inicio</a></li>
                <li class="breadcrumb-item"><a href="../index.html" class="text-decoration-none text-secondary">JavaScript</a></li>
                <li class="breadcrumb-item active text-dark fw-semibold" aria-current="page">04. DOM y BOM</li>
            </ol>
        </nav>

        <!-- Hero Header del Tema -->
        <div class="card bg-warning-subtle border-warning-subtle shadow-sm mb-4">
            <div class="card-body p-4 p-lg-5">
                <div class="d-flex flex-wrap align-items-center gap-2 mb-3">
                    <span class="badge text-bg-warning px-3 py-2 fs-6 fw-bold text-dark"><i class="bi bi-file-earmark-pdf me-1"></i> Manual Oficial: Tema 4</span>
                    <span class="badge bg-dark text-white px-3 py-2 fs-6">Teoría Completa & Ejercicios 4.1 - 4.6</span>
                </div>
                <h1 class="display-5 fw-bold text-dark mb-3">Tema 4: Acceso y Manipulación del DOM y BOM</h1>
                <p class="lead text-dark-emphasis mb-4">
                    Interacción con el entorno del navegador (BOM: objeto window, temporizadores setTimeout y setInterval) y control programático de la página web (DOM: árbol de nodos, selectores clásicos y modernos con querySelector/querySelectorAll, creación, clonación, inserción y borrado de elementos dinámicos, y manipulación en tiempo real de clases y estilos CSS).
                </p>
                
                <!-- Píldoras de Acceso Rápido a Secciones -->
                <div class="d-flex flex-wrap gap-2 pt-2 border-top border-warning-subtle">
                    <a href="#sec4-1" class="btn btn-sm btn-outline-dark bg-white rounded-pill"><i class="bi bi-hash"></i> 4.1 Introducción BOM y DOM</a>
                    <a href="#sec4-2" class="btn btn-sm btn-outline-dark bg-white rounded-pill"><i class="bi bi-hash"></i> 4.2 Elementos del BOM</a>
                    <a href="#sec4-2-1" class="btn btn-sm btn-outline-dark bg-white rounded-pill"><i class="bi bi-hash"></i> 4.2.1 Timeouts e Intervalos</a>
                    <a href="#sec4-3" class="btn btn-sm btn-outline-dark bg-white rounded-pill"><i class="bi bi-hash"></i> 4.3 Exploración del DOM</a>
                    <a href="#sec4-3-2" class="btn btn-sm btn-outline-dark bg-white rounded-pill"><i class="bi bi-hash"></i> 4.3.2 Query Selector</a>
                    <a href="#sec4-3-3" class="btn btn-sm btn-outline-dark bg-white rounded-pill"><i class="bi bi-hash"></i> 4.3.3 Manipulación (Crear y Borrar)</a>
                    <a href="#sec4-3-4" class="btn btn-sm btn-outline-dark bg-white rounded-pill"><i class="bi bi-hash"></i> 4.3.4 Atributos y Estilos CSS</a>
                    <a href="#sec-ejercicios" class="btn btn-sm btn-warning text-dark fw-bold rounded-pill"><i class="bi bi-pencil-square"></i> Ejercicios 4.1 a 4.6</a>
                </div>
            </div>
        </div>

        <div class="row g-4">
            
            <!-- Columna Principal de Contenido (9 cols en lg) -->
            <div class="col-lg-9 d-flex flex-column gap-4">

                <!-- 4.1 Introducción BOM y DOM -->
                <section id="sec4-1" class="card content-card shadow-sm p-4">
                    <div class="d-flex align-items-center gap-2 mb-3">
                        <span class="badge text-bg-warning fs-6">4.1</span>
                        <h2 class="h4 mb-0 fw-bold">Introducción: BOM y DOM</h2>
                    </div>
                    <p>
                        JavaScript se ejecuta normalmente incrustado dentro de un navegador sobre una página web. Esta arquitectura le permite interactuar directamente con dos modelos de objetos fundamentales:
                    </p>
                    <div class="row g-3 mb-3">
                        <div class="col-md-6">
                            <div class="p-3 border rounded bg-body-tertiary h-100">
                                <h6 class="fw-bold text-primary mb-1"><i class="bi bi-window me-1"></i> BOM (Browser Object Model)</h6>
                                <p class="small text-secondary mb-0">
                                    Representa el entorno del navegador propiamente dicho: dimensiones de la pantalla, barra de direcciones URL, historial de navegación, alertas y temporizadores asíncronos. Su objeto raíz es <code>window</code>.
                                </p>
                            </div>
                        </div>
                        <div class="col-md-6">
                            <div class="p-3 border rounded bg-body-tertiary h-100">
                                <h6 class="fw-bold text-success mb-1"><i class="bi bi-diagram-3 me-1"></i> DOM (Document Object Model)</h6>
                                <p class="small text-secondary mb-0">
                                    Representa la página HTML en sí como un árbol estructurado de nodos jerárquicos (etiquetas, atributos y textos). Permite inspeccionar, añadir, modificar o borrar elementos en caliente. Su objeto raíz es <code>document</code>.
                                </p>
                            </div>
                        </div>
                    </div>
                </section>

                <!-- 4.2 Elementos principales del BOM -->
                <section id="sec4-2" class="card content-card shadow-sm p-4">
                    <div class="d-flex align-items-center gap-2 mb-3">
                        <span class="badge text-bg-warning fs-6">4.2</span>
                        <h2 class="h4 mb-0 fw-bold">Elementos Principales del BOM (Objeto window)</h2>
                    </div>
                    <p>
                        El objeto global <code>window</code> engloba todas las APIs del navegador. De él cuelgan objetos especializados:
                    </p>
                    <div class="table-responsive table-custom mb-3">
                        <table class="table table-hover align-middle mb-0 small">
                            <thead>
                                <tr>
                                    <th>Subobjeto</th>
                                    <th>Finalidad</th>
                                    <th>Ejemplo de Código</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td><code>screen</code></td>
                                    <td>Dimensiones físicas y resolución de pantalla del usuario.</td>
                                    <td><code>console.log(screen.width + "x" + screen.height);</code></td>
                                </tr>
                                <tr>
                                    <td><code>location</code></td>
                                    <td>Consulta y redirección de la URL actual.</td>
                                    <td><code>location.href = "https://iessanvicente.com";</code></td>
                                </tr>
                                <tr>
                                    <td><code>history</code></td>
                                    <td>Pila de navegación hacia adelante o hacia atrás.</td>
                                    <td><code>history.back(); // Equivale al botón Atrás</code></td>
                                </tr>
                                <tr>
                                    <td><code>navigator</code></td>
                                    <td>Datos del navegador, idioma del sistema y capacidades.</td>
                                    <td><code>console.log(navigator.userAgent);</code></td>
                                </tr>
                                <tr>
                                    <td><code>document</code></td>
                                    <td>El contenido visual de la página web cargada.</td>
                                    <td><code>document.title = "Nuevo Título";</code></td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </section>

                <!-- 4.2.1 Uso de timeouts e intervalos -->
                <section id="sec4-2-1" class="card content-card shadow-sm p-4">
                    <div class="d-flex align-items-center gap-2 mb-3">
                        <span class="badge text-bg-warning fs-6">4.2.1</span>
                        <h2 class="h4 mb-0 fw-bold">Temporizadores Asíncronos: setTimeout y setInterval</h2>
                    </div>
                    <p>
                        Una de las utilidades más prácticas del BOM es programar ejecuciones temporizadas en milisegundos ($1 \text{ segundo} = 1000 \text{ ms}$):
                    </p>

                    <div class="row g-3 mb-3">
                        <div class="col-md-6">
                            <div class="p-3 border rounded bg-white h-100">
                                <h6 class="fw-bold text-primary mb-1">setTimeout (Ejecución Única)</h6>
                                <p class="small text-secondary mb-2">Ejecuta la función indicada <strong>una sola vez</strong> tras el retardo:</p>
                                <div class="code-block p-2">
<pre class="m-0"><code><span class="code-token-function">setTimeout</span>(() =&gt; {
    <span class="code-token-function">console</span>.<span class="code-token-function">log</span>(<span class="code-token-string">"Pasaron 3 segundos"</span>);
}, <span class="code-token-number">3000</span>);</code></pre>
                                </div>
                            </div>
                        </div>
                        <div class="col-md-6">
                            <div class="p-3 border rounded bg-white h-100">
                                <h6 class="fw-bold text-success mb-1">setInterval (Ejecución Periódica)</h6>
                                <p class="small text-secondary mb-2">Repite la ejecución <strong>indefinidamente</strong> cada intervalo de tiempo:</p>
                                <div class="code-block p-2">
<pre class="m-0"><code><span class="code-token-keyword">let</span> id = <span class="code-token-function">setInterval</span>(() =&gt; {
    <span class="code-token-function">console</span>.<span class="code-token-function">log</span>(<span class="code-token-keyword">new</span> <span class="code-token-function">Date</span>());
}, <span class="code-token-number">5000</span>);</code></pre>
                                </div>
                            </div>
                        </div>
                    </div>

                    <h4 class="h6 fw-bold text-dark mt-3">Cancelación de Temporizadores (clearTimeout / clearInterval)</h4>
                    <p class="small">
                        Tanto <code>setTimeout</code> como <code>setInterval</code> devuelven un identificador numérico único (<code>id</code>). Para detenerlos, se utiliza <code>clearTimeout(id)</code> o <code>clearInterval(id)</code>:
                    </p>
                    <div class="code-block">
<pre class="m-0"><code><span class="code-token-comment">// Inicia un reloj cada 5 segundos y lo cancela automáticamente tras 20 segundos:</span>
<span class="code-token-keyword">let</span> idReloj = <span class="code-token-function">setInterval</span>(() =&gt; <span class="code-token-function">console</span>.<span class="code-token-function">log</span>(<span class="code-token-keyword">new</span> <span class="code-token-function">Date</span>()), <span class="code-token-number">5000</span>);
<span class="code-token-function">setTimeout</span>(() =&gt; <span class="code-token-function">clearInterval</span>(idReloj), <span class="code-token-number">20000</span>);</code></pre>
                    </div>
                </section>

                <!-- 4.3 Uso del DOM -->
                <section id="sec4-3" class="card content-card shadow-sm p-4">
                    <div class="d-flex align-items-center gap-2 mb-3">
                        <span class="badge text-bg-warning fs-6">4.3</span>
                        <h2 class="h4 mb-0 fw-bold">Exploración del Árbol DOM</h2>
                    </div>
                    <p>
                        El DOM estructura la página como un árbol de nodos que podemos recorrer hacia arriba (padres), hacia abajo (hijos) o hacia los lados (hermanos):
                    </p>

                    <div class="table-responsive table-custom mb-3">
                        <table class="table table-hover align-middle mb-0 small">
                            <thead>
                                <tr>
                                    <th>Propiedad / Método</th>
                                    <th>Elemento Obtenido</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr><td><code>document.getElementById("miId")</code></td><td>El único elemento con dicho atributo <code>id</code>.</td></tr>
                                <tr><td><code>document.getElementsByClassName("clase")</code></td><td>Colección HTMLCollection de elementos con esa clase.</td></tr>
                                <tr><td><code>document.getElementsByTagName("p")</code></td><td>Colección HTMLCollection de todos los párrafos.</td></tr>
                                <tr><td><code>element.parentNode</code></td><td>El nodo padre directo del elemento actual.</td></tr>
                                <tr><td><code>element.children</code></td><td>Colección de elementos hijos inmediatos.</td></tr>
                                <tr><td><code>element.nextElementSibling</code></td><td>El siguiente elemento hermano en el mismo nivel.</td></tr>
                                <tr><td><code>element.textContent</code></td><td>El texto plano puro del elemento (sin etiquetas).</td></tr>
                                <tr><td><code>element.innerHTML</code></td><td>El contenido HTML interno (renderiza subetiquetas).</td></tr>
                            </tbody>
                        </table>
                    </div>

                    <!-- Tarjeta del Ejercicio 4.1 -->
                    <div class="card exercise-card border-warning bg-warning-subtle shadow-sm p-3 mt-3">
                        <div class="d-flex align-items-center justify-content-between mb-2">
                            <h4 class="h6 fw-bold text-dark mb-0"><i class="bi bi-pencil-square me-1"></i> Ejercicio 4.1: Exploración Clásica del DOM</h4>
                            <span class="badge bg-warning text-dark border border-dark-subtle">Ejercicio Oficial</span>
                        </div>
                        <p class="small text-dark-emphasis mb-2">
                            En <code>01_pruebaDOM_js.html</code>, a partir de un texto con enlaces distribuido en tres párrafos, mostrar mediante <code>alert()</code>:
                        </p>
                        <ol class="small text-dark-emphasis mb-3 ps-3">
                            <li>El número total de enlaces (<code>&lt;a&gt;</code>) existentes en toda la página.</li>
                            <li>La dirección a la que apunta el primer enlace (propiedad <code>href</code>).</li>
                            <li>El número de enlaces situados exclusivamente dentro del tercer párrafo (<code>id="p3"</code>).</li>
                        </ol>
                        <div class="d-flex flex-wrap gap-2">
                            <a href="../material/ejercicios/aprendizaje/t4_01_pruebaDOM_js.html" target="_blank" class="btn btn-sm btn-dark"><i class="bi bi-play-circle me-1"></i> Probar Solución</a>
                            <a href="07_ejercicios_r.html#ej_4_1" class="btn btn-sm btn-outline-dark"><i class="bi bi-code-slash me-1"></i> Ver Código Resuelto</a>
                        </div>
                    </div>
                </section>

                <!-- 4.3.2 Query Selector -->
                <section id="sec4-3-2" class="card content-card shadow-sm p-4">
                    <div class="d-flex align-items-center gap-2 mb-3">
                        <span class="badge text-bg-warning fs-6">4.3.2</span>
                        <h2 class="h4 mb-0 fw-bold">Selectores Modernos: querySelector y querySelectorAll</h2>
                    </div>
                    <p>
                        Inspirados en la sintaxis de selectores CSS (popularizada por jQuery), los métodos <code>querySelector</code> y <code>querySelectorAll</code> ofrecen la forma más potente y versátil de localizar elementos:
                    </p>
                    <div class="code-block mb-3">
<pre class="m-0"><code><span class="code-token-comment">// Devuelve el PRIMER elemento que encaje con el selector CSS:</span>
<span class="code-token-keyword">let</span> primerEnlace = <span class="code-token-function">document</span>.<span class="code-token-function">querySelector</span>(<span class="code-token-string">"a"</span>);
<span class="code-token-keyword">let</span> tarjeta = <span class="code-token-function">document</span>.<span class="code-token-function">querySelector</span>(<span class="code-token-string">".card"</span>);
<span class="code-token-keyword">let</span> botonPrincipal = <span class="code-token-function">document</span>.<span class="code-token-function">querySelector</span>(<span class="code-token-string">"#btnSubmit"</span>);
<span class="code-token-keyword">let</span> parrafoAnidado = <span class="code-token-function">document</span>.<span class="code-token-function">querySelector</span>(<span class="code-token-string">"div.contenido &gt; p"</span>);

<span class="code-token-comment">// Devuelve una NodeList estática con TODOS los elementos coincidentes:</span>
<span class="code-token-keyword">let</span> todosEnlaces = <span class="code-token-function">document</span>.<span class="code-token-function">querySelectorAll</span>(<span class="code-token-string">"p a"</span>);

<span class="code-token-comment">// NodeList admite directamente el método .forEach():</span>
todosEnlaces.<span class="code-token-function">forEach</span>(enlace =&gt; {
    <span class="code-token-function">console</span>.<span class="code-token-function">log</span>(enlace.href);
});</code></pre>
                    </div>

                    <!-- Tarjeta del Ejercicio 4.2 -->
                    <div class="card exercise-card border-warning bg-warning-subtle shadow-sm p-3">
                        <h4 class="h6 fw-bold text-dark mb-1"><i class="bi bi-pencil-square me-1"></i> Ejercicio 4.2: Resolución con querySelector</h4>
                        <p class="small text-dark-emphasis mb-2">
                            Crear <code>02_pruebaDOM2_js.html</code> y resolver exactamente las mismas consultas del Ejercicio 4.1 utilizando exclusivamente <code>querySelector</code> y <code>querySelectorAll</code> con selectores CSS compuestos (por ejemplo <code>#p3 a</code>).
                        </p>
                        <div class="d-flex gap-2">
                            <a href="../material/ejercicios/aprendizaje/t4_02_pruebaDOM2_js.html" target="_blank" class="btn btn-sm btn-dark"><i class="bi bi-play-circle me-1"></i> Probar</a>
                            <a href="07_ejercicios_r.html#ej_4_2" class="btn btn-sm btn-outline-dark"><i class="bi bi-code-slash"></i> Solución</a>
                        </div>
                    </div>
                </section>

                <!-- 4.3.3 Manipulación del DOM -->
                <section id="sec4-3-3" class="card content-card shadow-sm p-4">
                    <div class="d-flex align-items-center gap-2 mb-3">
                        <span class="badge text-bg-warning fs-6">4.3.3</span>
                        <h2 class="h4 mb-0 fw-bold">Manipulación Dinámica: Crear, Insertar y Borrar Nodos</h2>
                    </div>
                    <p>
                        Para alterar el árbol visual en caliente sin recargar la página:
                    </p>

                    <h4 class="h6 fw-bold text-dark mt-3">1. Creación e Inserción de Elementos</h4>
                    <p class="small">
                        El proceso estándar consta de cuatro pasos:
                    </p>
                    <div class="code-block mb-3">
<pre class="m-0"><code><span class="code-token-comment">// 1. Crear el nuevo elemento en memoria:</span>
<span class="code-token-keyword">let</span> nuevoParrafo = <span class="code-token-function">document</span>.<span class="code-token-function">createElement</span>(<span class="code-token-string">"p"</span>);

<span class="code-token-comment">// 2. Asignarle contenido textual o HTML:</span>
nuevoParrafo.textContent = <span class="code-token-string">"Este es un párrafo generado dinámicamente."</span>;

<span class="code-token-comment">// 3. Insertarlo al final del contenedor padre:</span>
<span class="code-token-function">document</span>.body.<span class="code-token-function">appendChild</span>(nuevoParrafo);

<span class="code-token-comment">// Alternativa: Insertar delante de otro nodo de referencia:</span>
<span class="code-token-keyword">let</span> referencia = <span class="code-token-function">document</span>.<span class="code-token-function">getElementById</span>(<span class="code-token-string">"p3"</span>);
<span class="code-token-function">document</span>.body.<span class="code-token-function">insertBefore</span>(nuevoParrafo, referencia);</code></pre>
                    </div>

                    <h4 class="h6 fw-bold text-dark mt-3">2. Borrado de Nodos</h4>
                    <p class="small">
                        Para eliminar un elemento se localiza su nodo padre y se invoca <code>removeChild</code>, o se llama directamente a <code>element.remove()</code> en navegadores modernos:
                    </p>
                    <div class="code-block mb-3">
<pre class="m-0"><code><span class="code-token-keyword">let</span> elemento = <span class="code-token-function">document</span>.<span class="code-token-function">getElementById</span>(<span class="code-token-string">"div1"</span>);
<span class="code-token-comment">// Sintaxis tradicional:</span>
elemento.parentNode.<span class="code-token-function">removeChild</span>(elemento);

<span class="code-token-comment">// Sintaxis moderna directa:</span>
elemento.<span class="code-token-function">remove</span>();</code></pre>
                    </div>

                    <!-- Tarjetas de Ejercicios 4.3 y 4.4 -->
                    <div class="row g-3">
                        <div class="col-md-6">
                            <div class="card exercise-card border-warning bg-warning-subtle shadow-sm p-3 h-100">
                                <h4 class="h6 fw-bold text-dark mb-1"><i class="bi bi-pencil-square me-1"></i> Ejercicio 4.3: Creación y Borrado con Botones</h4>
                                <p class="small text-dark-emphasis mb-2">
                                    En <code>03_prueba_DOM_js.html</code>, añadir dos botones: <em>"Nuevo párrafo"</em> (ejecuta <code>nuevoParrafo()</code> que añade un <code>&lt;p&gt;</code> al final) y <em>"Borrar segundo párrafo"</em> (ejecuta <code>borrarSegundoParrafo()</code>).
                                </p>
                                <div class="d-flex gap-2 mt-auto">
                                    <a href="../material/ejercicios/aprendizaje/t4_03_pruebaDOM2_js.html" target="_blank" class="btn btn-sm btn-dark flex-grow-1"><i class="bi bi-play me-1"></i> Probar</a>
                                    <a href="07_ejercicios_r.html#ej_4_3" class="btn btn-sm btn-outline-dark"><i class="bi bi-code-slash"></i> Solución</a>
                                </div>
                            </div>
                        </div>
                        <div class="col-md-6">
                            <div class="card exercise-card border-warning bg-warning-subtle shadow-sm p-3 h-100">
                                <h4 class="h6 fw-bold text-dark mb-1"><i class="bi bi-pencil-square me-1"></i> Ejercicio 4.4: Modificación de Estilos CSS</h4>
                                <p class="small text-dark-emphasis mb-2">
                                    En <code>04_pruebaDOM.html</code>, modificar los estilos en caliente mediante JavaScript: cambiar el fondo del primer párrafo a color amarillo (<code>style.backgroundColor = "yellow"</code>) y ocultar el segundo párrafo (<code>style.display = "none"</code>).
                                </p>
                                <div class="d-flex gap-2 mt-auto">
                                    <a href="../material/ejercicios/aprendizaje/t4_04_pruebaDOM2_js.html" target="_blank" class="btn btn-sm btn-dark flex-grow-1"><i class="bi bi-play me-1"></i> Probar</a>
                                    <a href="07_ejercicios_r.html#ej_4_4" class="btn btn-sm btn-outline-dark"><i class="bi bi-code-slash"></i> Solución</a>
                                </div>
                            </div>
                        </div>
                    </div>
                </section>

                <!-- 4.3.4 Atributos y Estilos CSS -->
                <section id="sec4-3-4" class="card content-card shadow-sm p-4">
                    <div class="d-flex align-items-center gap-2 mb-3">
                        <span class="badge text-bg-warning fs-6">4.3.4</span>
                        <h2 class="h4 mb-0 fw-bold">Manipulación de Atributos y Estilos CSS</h2>
                    </div>
                    <p>
                        Para alterar propiedades CSS, accedemos al objeto <code>element.style</code>. Las propiedades que en CSS llevan guion (kebab-case como <code>background-color</code>) se escriben en JavaScript en camelCase (<code>backgroundColor</code>):
                    </p>
                    <div class="code-block mb-3">
<pre class="m-0"><code><span class="code-token-keyword">let</span> caja = <span class="code-token-function">document</span>.<span class="code-token-function">getElementById</span>(<span class="code-token-string">"caja"</span>);
caja.style.width = <span class="code-token-string">"50%"</span>;
caja.style.backgroundColor = <span class="code-token-string">"#ffc107"</span>;
caja.style.display = <span class="code-token-string">"block"</span>;</code></pre>
                    </div>

                    <h4 class="h6 fw-bold text-dark mt-3">Manipulación de Clases CSS con classList</h4>
                    <p class="small">
                        La mejor práctica no es inyectar estilos inline, sino alternar clases predefinidas mediante la API <code>classList</code>:
                    </p>
                    <div class="code-block mb-3">
<pre class="m-0"><code><span class="code-token-comment">// Métodos de classList:</span>
caja.classList.<span class="code-token-function">add</span>(<span class="code-token-string">"alert"</span>, <span class="code-token-string">"alert-success"</span>);  <span class="code-token-comment">// Añade clases</span>
caja.classList.<span class="code-token-function">remove</span>(<span class="code-token-string">"d-none"</span>);                 <span class="code-token-comment">// Elimina una clase</span>
caja.classList.<span class="code-token-function">toggle</span>(<span class="code-token-string">"activo"</span>);                 <span class="code-token-comment">// Conmuta la clase</span>
<span class="code-token-keyword">let</span> tiene = caja.classList.<span class="code-token-function">contains</span>(<span class="code-token-string">"activo"</span>);  <span class="code-token-comment">// Comprueba si existe</span></code></pre>
                    </div>
                </section>

                <!-- SECCIÓN OFICIAL DE EJERCICIOS DEL TEMA 4 (4.5 y 4.6) -->
                <section id="sec-ejercicios" class="card content-card shadow-sm p-4">
                    <div class="d-flex align-items-center justify-content-between flex-wrap gap-2 mb-3">
                        <div class="d-flex align-items-center gap-2">
                            <span class="badge text-bg-warning fs-6"><i class="bi bi-pencil-square"></i></span>
                            <h2 class="h4 mb-0 fw-bold">Boletín Oficial de Ejercicios del Tema 4 (6 Ejercicios)</h2>
                        </div>
                        <a href="07_ejercicios.html" class="btn btn-sm btn-outline-warning text-dark fw-semibold"><i class="bi bi-collection me-1"></i> Catálogo Global</a>
                    </div>
                    <p class="text-secondary small mb-4">
                        Ejercicios interactivos del Tema 4 para completar:
                    </p>

                    <div class="row g-3">
                        
                        <!-- Ejercicio 4.5 -->
                        <div class="col-md-6">
                            <div class="card h-100 border exercise-card shadow-sm">
                                <div class="card-header bg-dark text-white d-flex justify-content-between align-items-center py-2">
                                    <span class="fw-bold small">Ejercicio 4.5</span>
                                    <span class="badge text-bg-warning text-dark">05_pruebaDOM.html</span>
                                </div>
                                <div class="card-body p-3 d-flex flex-column justify-content-between">
                                    <p class="small text-secondary mb-3">
                                        Mostrar texto completo oculto ("Seguir leyendo...") al pulsar sobre un enlace y ocultar el propio enlace mediante <code>muestra()</code>.
                                    </p>
                                    <div class="d-flex gap-2">
                                        <a href="../material/ejercicios/aprendizaje/t4_05_pruebaDOM_js.html" target="_blank" class="btn btn-sm btn-dark flex-grow-1"><i class="bi bi-play me-1"></i> Probar</a>
                                        <a href="07_ejercicios_r.html#ej_4_5" class="btn btn-sm btn-outline-dark"><i class="bi bi-code-slash"></i> Solución</a>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- Ejercicio 4.6 -->
                        <div class="col-md-6">
                            <div class="card h-100 border exercise-card shadow-sm">
                                <div class="card-header bg-dark text-white d-flex justify-content-between align-items-center py-2">
                                    <span class="fw-bold small">Ejercicio 4.6</span>
                                    <span class="badge text-bg-warning text-dark">06_pruebaDOM.html</span>
                                </div>
                                <div class="card-body p-3 d-flex flex-column justify-content-between">
                                    <p class="small text-secondary mb-3">
                                        Añadir dinámicamente nuevos elementos <code>&lt;li&gt;</code> numerados a una lista existente cada vez que se pulsa un botón con la función <code>anyade()</code>.
                                    </p>
                                    <div class="d-flex gap-2">
                                        <a href="../material/ejercicios/aprendizaje/t4_06_pruebaDOM_js.html" target="_blank" class="btn btn-sm btn-dark flex-grow-1"><i class="bi bi-play me-1"></i> Probar</a>
                                        <a href="07_ejercicios_r.html#ej_4_6" class="btn btn-sm btn-outline-dark"><i class="bi bi-code-slash"></i> Solución</a>
                                    </div>
                                </div>
                            </div>
                        </div>

                    </div>
                </section>

                <!-- Paginación Inferior -->
                <nav class="d-flex justify-content-between align-items-center mt-2 pt-3 border-top" aria-label="Navegación de temas">
                    <a href="03_arrays.html" class="btn btn-outline-secondary d-flex align-items-center gap-2">
                        <i class="bi bi-arrow-left"></i>
                        <span>Tema 3: Arrays y Objetos</span>
                    </a>
                    <a href="05_eventos.html" class="btn btn-warning text-dark fw-bold d-flex align-items-center gap-2">
                        <span>Tema 5: Gestión de Eventos</span>
                        <i class="bi bi-arrow-right"></i>
                    </a>
                </nav>

            </div>

            <!-- Columna Lateral Derecha (3 cols en lg): Índice Rápido Flotante -->
            <div class="col-lg-3 d-none d-lg-block">
                <div class="sticky-summary">
                    <div class="card border content-card shadow-sm p-3">
                        <h6 class="fw-bold text-uppercase text-secondary small mb-3">
                            <i class="bi bi-bookmark me-1"></i> En esta página
                        </h6>
                        <nav class="nav flex-column small gap-1">
                            <a class="nav-link px-2 py-1 text-secondary text-truncate" href="#sec4-1"><i class="bi bi-chevron-right me-1"></i> 4.1 BOM y DOM</a>
                            <a class="nav-link px-2 py-1 text-secondary text-truncate" href="#sec4-2"><i class="bi bi-chevron-right me-1"></i> 4.2 Elementos BOM</a>
                            <a class="nav-link px-2 py-1 text-secondary text-truncate" href="#sec4-2-1"><i class="bi bi-chevron-right me-1"></i> 4.2.1 Timeouts & Intervalos</a>
                            <a class="nav-link px-2 py-1 text-secondary text-truncate" href="#sec4-3"><i class="bi bi-chevron-right me-1"></i> 4.3 Árbol DOM</a>
                            <a class="nav-link px-2 py-1 text-secondary text-truncate" href="#sec4-3-2"><i class="bi bi-chevron-right me-1"></i> 4.3.2 Query Selector</a>
                            <a class="nav-link px-2 py-1 text-secondary text-truncate" href="#sec4-3-3"><i class="bi bi-chevron-right me-1"></i> 4.3.3 Crear y Borrar</a>
                            <a class="nav-link px-2 py-1 text-secondary text-truncate" href="#sec4-3-4"><i class="bi bi-chevron-right me-1"></i> 4.3.4 Atributos y CSS</a>
                            <a class="nav-link px-2 py-1 text-warning fw-bold text-truncate" href="#sec-ejercicios"><i class="bi bi-pencil-square me-1"></i> Ejercicios 4.1 - 4.6</a>
                        </nav>
                        
                        <div class="border-top mt-3 pt-3">
                            <a href="../material/t4_dom.pdf" target="_blank" class="btn btn-outline-danger btn-sm w-100 d-flex align-items-center justify-content-center gap-1">
                                <i class="bi bi-filetype-pdf"></i> Ver PDF Original
                            </a>
                        </div>
                    </div>
                </div>
            </div>

        </div>

    </main>

    <!-- 4. Pie de Página Común -->
    <footer class="bg-dark text-white-50 py-4 mt-auto border-top border-secondary">
        <div class="container-xl d-flex flex-wrap justify-content-between align-items-center gap-3">
            <div class="d-flex align-items-center gap-2">
                <img src="../../imagenes/logo.jpg" alt="Logo" width="28" height="28" class="rounded object-fit-cover">
                <span class="text-light fw-semibold">LMSGI</span>
                <span class="small">&copy; Lenguajes de Marcas y Sistemas de Gestión de Información</span>
            </div>
            <div class="small">
                <span>Diseñado con <strong>Bootstrap 5.3</strong> &bull; Temario Web Oficial</span>
            </div>
        </div>
    </footer>

    <!-- Bootstrap 5.3 JS Bundle (CDN) -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>

</body>
</html>
"""
    with open("javascript/archivos/04_dom.html", "w", encoding="utf-8") as f:
        f.write(doc)
    print("04_dom.html generated successfully! Length:", len(doc))

if __name__ == '__main__':
    generate_t4_page()
