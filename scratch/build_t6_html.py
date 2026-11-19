import os

def generate_t6_page():
    doc = """<!DOCTYPE html>
<html lang="es" data-bs-theme="light">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>06. Validación de Formularios | JavaScript | LMSGI</title>
    <meta name="description" content="Tema 6: Validación en el cliente con JavaScript y HTML5: acceso a controles (input, radio, checkbox, select), expresiones regulares (RegEx), interceptación del evento submit con preventDefault, Constraint Validation API y estilos CSS con Bootstrap 5.">
    
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
                <a href="04_dom.html" class="list-group-item list-group-item-action bg-transparent text-light border-secondary d-flex align-items-center gap-2 py-2"><i class="bi bi-diagram-3 text-warning"></i> 04. DOM y BOM</a>
                <a href="05_eventos.html" class="list-group-item list-group-item-action bg-transparent text-light border-secondary d-flex align-items-center gap-2 py-2"><i class="bi bi-lightning-charge text-warning"></i> 05. Gestión de Eventos</a>
                <a href="06_formularios.html" class="list-group-item list-group-item-action active bg-warning text-dark border-warning fw-semibold d-flex align-items-center gap-2 py-2"><i class="bi bi-ui-checks text-dark"></i> 06. Validación de Formularios</a>
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
                <li class="breadcrumb-item active text-dark fw-semibold" aria-current="page">06. Validación de Formularios</li>
            </ol>
        </nav>

        <!-- Hero Header del Tema -->
        <div class="card bg-warning-subtle border-warning-subtle shadow-sm mb-4">
            <div class="card-body p-4 p-lg-5">
                <div class="d-flex flex-wrap align-items-center gap-2 mb-3">
                    <span class="badge text-bg-warning px-3 py-2 fs-6 fw-bold text-dark"><i class="bi bi-file-earmark-pdf me-1"></i> Manual Oficial: Tema 6</span>
                    <span class="badge bg-dark text-white px-3 py-2 fs-6">Teoría Completa & Ejercicios 6.1 - 6.3</span>
                </div>
                <h1 class="display-5 fw-bold text-dark mb-3">Tema 6: Validación de Formularios en el Cliente</h1>
                <p class="lead text-dark-emphasis mb-4">
                    Control de integridad de datos en el navegador antes del envío al servidor: acceso a controles mediante nombres o ID, comprobación de campos de texto, casillas de verificación (checkbox), grupos de radio y listas desplegables (select), expresiones regulares avanzadas (RegEx), interceptación de envíos con preventDefault, la API nativa Constraint Validation de HTML5 (setCustomValidity, validity object) y feedback visual con pseudo-clases CSS y Bootstrap 5.
                </p>
                
                <!-- Píldoras de Acceso Rápido a Secciones -->
                <div class="d-flex flex-wrap gap-2 pt-2 border-top border-warning-subtle">
                    <a href="#sec6-1" class="btn btn-sm btn-outline-dark bg-white rounded-pill"><i class="bi bi-hash"></i> 6.1 Validación Tradicional</a>
                    <a href="#sec6-1-1" class="btn btn-sm btn-outline-dark bg-white rounded-pill"><i class="bi bi-hash"></i> 6.1.1 Acceso a Datos</a>
                    <a href="#sec6-1-2" class="btn btn-sm btn-outline-dark bg-white rounded-pill"><i class="bi bi-hash"></i> 6.1.2 Consulta de Valores</a>
                    <a href="#sec6-1-3" class="btn btn-sm btn-outline-dark bg-white rounded-pill"><i class="bi bi-hash"></i> 6.1.3 Expresiones Regulares</a>
                    <a href="#sec6-1-4" class="btn btn-sm btn-outline-dark bg-white rounded-pill"><i class="bi bi-hash"></i> 6.1.4 Validación Global y submit</a>
                    <a href="#sec6-2" class="btn btn-sm btn-outline-dark bg-white rounded-pill"><i class="bi bi-hash"></i> 6.2 Validación con HTML5</a>
                    <a href="#sec6-2-2" class="btn btn-sm btn-outline-dark bg-white rounded-pill"><i class="bi bi-hash"></i> 6.2.2 Mensajes Personalizados</a>
                    <a href="#sec6-2-3" class="btn btn-sm btn-outline-dark bg-white rounded-pill"><i class="bi bi-hash"></i> 6.2.3 CSS y Bootstrap 5</a>
                    <a href="#sec-ejercicios" class="btn btn-sm btn-warning text-dark fw-bold rounded-pill"><i class="bi bi-pencil-square"></i> Ejercicios 6.1 a 6.3</a>
                </div>
            </div>
        </div>

        <div class="row g-4">
            
            <!-- Columna Principal de Contenido (9 cols en lg) -->
            <div class="col-lg-9 d-flex flex-column gap-4">

                <!-- 6.1 Validación tradicional de formularios -->
                <section id="sec6-1" class="card content-card shadow-sm p-4">
                    <div class="d-flex align-items-center gap-2 mb-3">
                        <span class="badge text-bg-warning fs-6">6.1</span>
                        <h2 class="h4 mb-0 fw-bold">Validación Tradicional en el Cliente</h2>
                    </div>
                    <p>
                        Una de las razones históricas fundamentales que motivaron la creación de JavaScript fue la necesidad de <strong>validar la información de los formularios directamente en el navegador</strong> antes de enviarla a través de la red al servidor.
                    </p>
                    <p>
                        Al validar en el cliente evitamos enviar peticiones erróneas que sobrecarguen el backend, ahorramos ancho de banda y ofrecemos una respuesta instantánea al usuario sin recargar la página.
                    </p>
                    <div class="alert alert-info border-0 shadow-sm d-flex align-items-start gap-2 mb-0 small">
                        <i class="bi bi-info-circle-fill fs-5 text-info flex-shrink-0 mt-1"></i>
                        <div>
                            <strong>Regla de oro de seguridad web:</strong> La validación en el cliente con JavaScript y HTML5 está orientada a la <em>experiencia de usuario (UX)</em>. Sin embargo, un usuario malintencionado puede saltársela fácilmente desactivando JavaScript o enviando peticiones directas vía cURL/Postman. Por tanto, <strong>todo dato debe ser revalidado obligatoriamente en el servidor (backend)</strong> antes de guardarlo en base de datos.
                        </div>
                    </div>
                </section>

                <!-- 6.1.1 Acceso a los datos del formulario -->
                <section id="sec6-1-1" class="card content-card shadow-sm p-4">
                    <div class="d-flex align-items-center gap-2 mb-3">
                        <span class="badge text-bg-warning fs-6">6.1.1</span>
                        <h2 class="h4 mb-0 fw-bold">Acceso a los Datos del Formulario</h2>
                    </div>
                    <p>
                        Existen dos formas estándar de acceder a los controles de un formulario desde JavaScript:
                    </p>
                    <div class="row g-3 mb-3">
                        <div class="col-md-6">
                            <div class="p-3 border rounded bg-body-tertiary h-100">
                                <h6 class="fw-bold text-primary mb-1">1. Mediante atributos name</h6>
                                <p class="small text-secondary mb-2">Acceso directo a través de la jerarquía de propiedades del objeto <code>document</code>:</p>
                                <div class="code-block p-2">
<pre class="m-0"><code><span class="code-token-keyword">let</span> f = <span class="code-token-function">document</span>.miFormulario;
<span class="code-token-keyword">let</span> inputEmail = f.email;</code></pre>
                                </div>
                            </div>
                        </div>
                        <div class="col-md-6">
                            <div class="p-3 border rounded bg-body-tertiary h-100">
                                <h6 class="fw-bold text-success mb-1">2. Mediante getElementById o querySelector</h6>
                                <p class="small text-secondary mb-2">Acceso unificado por identificador único del elemento en el DOM:</p>
                                <div class="code-block p-2">
<pre class="m-0"><code><span class="code-token-keyword">let</span> inputEmail = <span class="code-token-function">document</span>.<span class="code-token-function">getElementById</span>(<span class="code-token-string">"email"</span>);
<span class="code-token-comment">// O bien: document.querySelector("#email");</span></code></pre>
                                </div>
                            </div>
                        </div>
                    </div>
                </section>

                <!-- 6.1.2 Consulta y comprobación de valores -->
                <section id="sec6-1-2" class="card content-card shadow-sm p-4">
                    <div class="d-flex align-items-center gap-2 mb-3">
                        <span class="badge text-bg-warning fs-6">6.1.2</span>
                        <h2 class="h4 mb-0 fw-bold">Consulta y Comprobación de Valores según el Tipo de Control</h2>
                    </div>
                    <p>
                        Cada elemento interactivo presenta peculiaridades para leer su estado:
                    </p>

                    <!-- Campos de texto estándar -->
                    <div class="border rounded p-3 mb-3 bg-body-tertiary">
                        <h6 class="fw-bold text-dark">Campos de Texto (text, email, password, textarea)</h6>
                        <p class="small mb-2">Se consulta la propiedad <code>.value</code> (cadena de texto) para verificar si está vacía o nula:</p>
                        <div class="code-block">
<pre class="m-0"><code><span class="code-token-keyword">let</span> campo = <span class="code-token-function">document</span>.miForm.login;
<span class="code-token-keyword">if</span> (campo.value.<span class="code-token-function">trim</span>() === <span class="code-token-string">""</span>) {
    <span class="code-token-function">alert</span>(<span class="code-token-string">"El login es obligatorio."</span>);
}</code></pre>
                        </div>
                    </div>

                    <!-- Checkbox y Radio -->
                    <div class="border rounded p-3 mb-3 bg-body-tertiary">
                        <h6 class="fw-bold text-dark">Casillas Checkbox y Botones de Radio</h6>
                        <p class="small mb-2">
                            Disponen de la propiedad booleana <code>.checked</code> (indica <code>true</code> si está marcada). En grupos de radio con el mismo nombre, se recorre la colección:
                        </p>
                        <div class="code-block">
<pre class="m-0"><code><span class="code-token-comment">// Checkbox individual:</span>
<span class="code-token-keyword">if</span> (<span class="code-token-function">document</span>.miForm.casado.checked) {
    <span class="code-token-function">console</span>.<span class="code-token-function">log</span>(<span class="code-token-string">"Estado civil: Casado"</span>);
}

<span class="code-token-comment">// Grupo de radio buttons con el mismo name:</span>
<span class="code-token-keyword">let</span> radios = <span class="code-token-function">document</span>.miForm.horario;
<span class="code-token-keyword">for</span> (<span class="code-token-keyword">let</span> r <span class="code-token-keyword">of</span> radios) {
    <span class="code-token-keyword">if</span> (r.checked) {
        <span class="code-token-function">console</span>.<span class="code-token-function">log</span>(<span class="code-token-string">"Horario seleccionado: "</span> + r.value);
    }
}</code></pre>
                        </div>
                    </div>

                    <!-- Listas desplegables Select -->
                    <div class="border rounded p-3 mb-4 bg-body-tertiary">
                        <h6 class="fw-bold text-dark">Listas Desplegables (&lt;select&gt;)</h6>
                        <p class="small mb-2">
                            Se utiliza la propiedad <code>.selectedIndex</code> (índice numérico de la opción elegida) o directamente <code>select.value</code>:
                        </p>
                        <div class="code-block">
<pre class="m-0"><code><span class="code-token-keyword">let</span> combo = <span class="code-token-function">document</span>.<span class="code-token-function">getElementById</span>(<span class="code-token-string">"operador"</span>);
<span class="code-token-keyword">if</span> (combo.selectedIndex === <span class="code-token-number">0</span>) {
    <span class="code-token-function">alert</span>(<span class="code-token-string">"Debe seleccionar un operador válido."</span>);
} <span class="code-token-keyword">else</span> {
    <span class="code-token-keyword">let</span> opcionElegida = combo.options[combo.selectedIndex];
    <span class="code-token-function">console</span>.<span class="code-token-function">log</span>(opcionElegida.text + <span class="code-token-string">" -&gt; "</span> + opcionElegida.value);
}</code></pre>
                        </div>
                    </div>

                    <!-- Tarjeta del Ejercicio 6.1 -->
                    <div class="card exercise-card border-warning bg-warning-subtle shadow-sm p-3">
                        <div class="d-flex align-items-center justify-content-between mb-2">
                            <h4 class="h6 fw-bold text-dark mb-0"><i class="bi bi-pencil-square me-1"></i> Ejercicio 6.1: Lectura Integral de Controles de Formulario</h4>
                            <span class="badge bg-warning text-dark border border-dark-subtle">Ejercicio Oficial</span>
                        </div>
                        <p class="small text-dark-emphasis mb-2">
                            En <code>01_form_js.html</code>, crear un formulario con campos de texto (login), número (nhijos), checkbox (info), radio buttons (horario: Mañana, Tarde, Noche) y lista select (operador: Movil1, Taronje, Hablafone, Roigo).
                        </p>
                        <p class="small text-dark-emphasis mb-2">
                            Al pulsar un botón normal (tipo button) llamado Enviar, ejecutar <code>mostrarInformacion()</code> para volcar en un <code>&lt;div id="salida"&gt;</code> cada una de las opciones seleccionadas, rellenando con <code>0</code> los hijos si quedó vacío.
                        </p>
                        <div class="d-flex gap-2">
                            <a href="../material/ejercicios/aprendizaje/t6_01_form_js.html" target="_blank" class="btn btn-sm btn-dark flex-grow-1"><i class="bi bi-play-circle me-1"></i> Probar Solución</a>
                            <a href="07_ejercicios_r.html#ej_6_1" class="btn btn-sm btn-outline-dark"><i class="bi bi-code-slash me-1"></i> Ver Código Resuelto</a>
                        </div>
                    </div>
                </section>

                <!-- 6.1.3 Expresiones regulares -->
                <section id="sec6-1-3" class="card content-card shadow-sm p-4">
                    <div class="d-flex align-items-center gap-2 mb-3">
                        <span class="badge text-bg-warning fs-6">6.1.3</span>
                        <h2 class="h4 mb-0 fw-bold">Validación de Patrones con Expresiones Regulares (RegEx)</h2>
                    </div>
                    <p>
                        Las <strong>expresiones regulares</strong> definen patrones de coincidencia de caracteres. En JavaScript se delimitan entre barras diagonales <code>/patrón/</code> y se evalúan mediante el método <code>patron.test(cadena)</code>:
                    </p>

                    <div class="table-responsive table-custom mb-4">
                        <table class="table table-hover align-middle mb-0 small">
                            <thead>
                                <tr>
                                    <th>Símbolo</th>
                                    <th>Significado</th>
                                    <th>Ejemplo</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr><td><code>^</code> / <code>$</code></td><td>Inicio / Fin de la cadena</td><td><code>/^...$/</code> (coincidencia exacta completa)</td></tr>
                                <tr><td><code>\\d</code> / <code>\\D</code></td><td>Cualquier dígito numérico <code>[0-9]</code> / No dígito</td><td><code>/\\d{4}/</code> (exactamente 4 dígitos)</td></tr>
                                <tr><td><code>\\w</code> / <code>\\W</code></td><td>Carácter alfanumérico y guion bajo <code>[A-Za-z0-9_]</code> / No alfanumérico</td><td><code>/\\w+/</code> (palabra alfanumérica)</td></tr>
                                <tr><td><code>{n}</code> / <code>{min,max}</code></td><td>Exactamente $n$ veces / Rango de repeticiones</td><td><code>/\\d{8,10}/</code> (entre 8 y 10 números)</td></tr>
                                <tr><td><code>+</code> / <code>*</code> / <code>?</code></td><td>Una o más veces / Cero o más / Opcional (0 o 1 vez)</td><td><code>/https?:/</code> (http o https)</td></tr>
                                <tr><td><code>[A-Z]</code></td><td>Rango de caracteres entre mayúsculas</td><td><code>/^[A-Z]{3}$/</code> (tres letras mayúsculas)</td></tr>
                            </tbody>
                        </table>
                    </div>

                    <h5 class="h6 fw-bold text-dark">Patrones Comunes de Validación</h5>
                    <div class="code-block mb-3">
<pre class="m-0"><code><span class="code-token-comment">// 1. DNI español (8 dígitos y 1 letra mayúscula):</span>
<span class="code-token-keyword">let</span> regexDni = <span class="code-token-string">/^\d{8}[A-Z]$/</span>;
<span class="code-token-keyword">if</span> (!regexDni.<span class="code-token-function">test</span>(dni)) <span class="code-token-function">alert</span>(<span class="code-token-string">"DNI incorrecto."</span>);

<span class="code-token-comment">// 2. Código postal español (exactamente 5 dígitos):</span>
<span class="code-token-keyword">let</span> regexCP = <span class="code-token-string">/^\d{5}$/</span>;

<span class="code-token-comment">// 3. Teléfono (9 dígitos comenzando por 6, 7, 8 o 9):</span>
<span class="code-token-keyword">let</span> regexTel = <span class="code-token-string">/^[6789]\d{8}$/</span>;

<span class="code-token-comment">// 4. Correo electrónico estándar:</span>
<span class="code-token-keyword">let</span> regexEmail = <span class="code-token-string">/^[\w.-]+@([\w-]+\.)+[\w-]{2,4}$/</span>;</code></pre>
                    </div>
                </section>

                <!-- 6.1.4 Validación global y submit -->
                <section id="sec6-1-4" class="card content-card shadow-sm p-4">
                    <div class="d-flex align-items-center gap-2 mb-3">
                        <span class="badge text-bg-warning fs-6">6.1.4</span>
                        <h2 class="h4 mb-0 fw-bold">Interceptación del Envío Global (Evento submit)</h2>
                    </div>
                    <p>
                        Para validar todo el formulario en bloque antes de enviarlo, escuchamos el evento <code>submit</code> sobre la etiqueta <code>&lt;form&gt;</code>. Si detectamos cualquier error, invocamos <code>e.preventDefault()</code> para cancelar el envío y detener la petición:
                    </p>
                    <div class="code-block mb-3">
<pre class="m-0"><code><span class="code-token-keyword">let</span> formulario = <span class="code-token-function">document</span>.<span class="code-token-function">getElementById</span>(<span class="code-token-string">"miFormulario"</span>);

formulario.<span class="code-token-function">addEventListener</span>(<span class="code-token-string">"submit"</span>, <span class="code-token-keyword">function</span>(e) {
    <span class="code-token-keyword">let</span> login = <span class="code-token-function">document</span>.<span class="code-token-function">getElementById</span>(<span class="code-token-string">"login"</span>);
    
    <span class="code-token-keyword">if</span> (login.value.<span class="code-token-function">trim</span>() === <span class="code-token-string">""</span>) {
        <span class="code-token-comment">// ¡Cancelamos el envío del formulario al servidor!:</span>
        e.<span class="code-token-function">preventDefault</span>();
        <span class="code-token-function">alert</span>(<span class="code-token-string">"Error: Debe rellenar el campo login antes de enviar."</span>);
        login.<span class="code-token-function">focus</span>();
    }
});</code></pre>
                    </div>

                    <!-- Tarjeta del Ejercicio 6.2 -->
                    <div class="card exercise-card border-warning bg-warning-subtle shadow-sm p-3">
                        <h4 class="h6 fw-bold text-dark mb-1"><i class="bi bi-pencil-square me-1"></i> Ejercicio 6.2: Validación Global de Envío con preventDefault</h4>
                        <p class="small text-dark-emphasis mb-2">
                            En <code>02_form_js.html</code>, interceptar el envío del formulario anterior con <code>submit</code>: verificar que el login esté relleno, el horario seleccionado y el operador elegido no sea el primer valor por defecto. Si algo falla, cancelar el envío con <code>e.preventDefault()</code> y notificar los errores.
                        </p>
                        <div class="d-flex gap-2">
                            <a href="../material/ejercicios/aprendizaje/t6_02_form_js.html" target="_blank" class="btn btn-sm btn-dark"><i class="bi bi-play me-1"></i> Probar Solución</a>
                            <a href="07_ejercicios_r.html#ej_6_2" class="btn btn-sm btn-outline-dark"><i class="bi bi-code-slash"></i> Solución</a>
                        </div>
                    </div>
                </section>

                <!-- 6.2 Validación combinada con HTML5 -->
                <section id="sec6-2" class="card content-card shadow-sm p-4">
                    <div class="d-flex align-items-center gap-2 mb-3">
                        <span class="badge text-bg-warning fs-6">6.2</span>
                        <h2 class="h4 mb-0 fw-bold">Validación Nativa HTML5 y Constraint Validation API</h2>
                    </div>
                    <p>
                        HTML5 incorpora validación declarativa mediante atributos en los campos (<code>required</code>, <code>minlength</code>, <code>maxlength</code>, <code>pattern</code>, <code>type="email"</code>).
                    </p>
                    <p>
                        La <strong>Constraint Validation API</strong> de JavaScript permite enlazar con dicha validación nativa a través de métodos y propiedades de los inputs:
                    </p>

                    <h4 class="h6 fw-bold text-dark mt-3">Personalizar Mensajes con setCustomValidity()</h4>
                    <p class="small">
                        Podemos sustituir las alertas invasivas por los globos nativos del navegador o mensajes integrados:
                    </p>
                    <div class="code-block mb-3">
<pre class="m-0"><code><span class="code-token-keyword">let</span> pass1 = <span class="code-token-function">document</span>.<span class="code-token-function">getElementById</span>(<span class="code-token-string">"pass1"</span>);
<span class="code-token-keyword">let</span> pass2 = <span class="code-token-function">document</span>.<span class="code-token-function">getElementById</span>(<span class="code-token-string">"pass2"</span>);

<span class="code-token-keyword">function</span> <span class="code-token-function">validarCoincidenciaPassword</span>() {
    <span class="code-token-keyword">if</span> (pass1.value !== pass2.value) {
        pass2.<span class="code-token-function">setCustomValidity</span>(<span class="code-token-string">"Las contraseñas introducidas no coinciden."</span>);
    } <span class="code-token-keyword">else</span> {
        pass2.<span class="code-token-function">setCustomValidity</span>(<span class="code-token-string">""</span>); <span class="code-token-comment">// Cadena vacía indica que es válido</span>
    }
}
pass1.<span class="code-token-function">addEventListener</span>(<span class="code-token-string">"input"</span>, validarCoincidenciaPassword);
pass2.<span class="code-token-function">addEventListener</span>(<span class="code-token-string">"input"</span>, validarCoincidenciaPassword);</code></pre>
                    </div>

                    <h4 class="h6 fw-bold text-dark mt-3">El Objeto input.validity</h4>
                    <p class="small">
                        Permite inspeccionar exactamente qué restricción ha fallado:
                    </p>
                    <ul class="small ps-3 mb-3">
                        <li><code>validity.valueMissing</code>: <code>true</code> si un campo con <code>required</code> está en blanco.</li>
                        <li><code>validity.typeMismatch</code>: <code>true</code> si el formato no coincide (ej. email inválido en <code>type="email"</code>).</li>
                        <li><code>validity.patternMismatch</code>: <code>true</code> si no encaja con la RegEx del atributo <code>pattern</code>.</li>
                        <li><code>validity.valid</code>: <code>true</code> si cumple todas las restricciones.</li>
                    </ul>

                    <!-- Tarjeta del Ejercicio 6.3 -->
                    <div class="card exercise-card border-warning bg-warning-subtle shadow-sm p-3">
                        <h4 class="h6 fw-bold text-dark mb-1"><i class="bi bi-pencil-square me-1"></i> Ejercicio 6.3: Formulario con Validación HTML5 y Estilos CSS</h4>
                        <p class="small text-dark-emphasis mb-2">
                            En <code>03_form_js.html</code>, formulario <code>form3</code> con: login obligatorio, dos contraseñas obligatorias de al menos 8 caracteres con letras y dígitos que deben coincidir exactamente, y campo email obligatorio.
                        </p>
                        <p class="small text-dark-emphasis mb-2">
                            Configurar mensajes personalizados con <code>setCustomValidity()</code> (sin alertas popups) y marcar en rojo los campos con error, restableciendo el fondo a blanco en cuanto el usuario vuelva a teclear (<code>input</code>).
                        </p>
                        <div class="d-flex gap-2">
                            <a href="../material/ejercicios/aprendizaje/t6_03_form_js.html" target="_blank" class="btn btn-sm btn-dark"><i class="bi bi-play me-1"></i> Probar Solución</a>
                            <a href="07_ejercicios_r.html#ej_6_3" class="btn btn-sm btn-outline-dark"><i class="bi bi-code-slash"></i> Solución</a>
                        </div>
                    </div>
                </section>

                <!-- 6.2.3 CSS y Bootstrap 5 en validación -->
                <section id="sec6-2-3" class="card content-card shadow-sm p-4">
                    <div class="d-flex align-items-center gap-2 mb-3">
                        <span class="badge text-bg-warning fs-6">6.2.3</span>
                        <h2 class="h4 mb-0 fw-bold">Estilos CSS y Clases Nativas de Bootstrap 5</h2>
                    </div>
                    <p>
                        En CSS disponemos de las pseudo-clases <code>:required</code>, <code>:valid</code> e <code>:invalid</code>.
                    </p>
                    <p>
                        Sin embargo, en interfaces modernas con **Bootstrap 5.3**, la pauta ergonómica recomendada es añadir el atributo <code>novalidate</code> al formulario y gestionar las clases nativas de estado:
                    </p>
                    <div class="code-block mb-3">
<pre class="m-0"><code><span class="code-token-comment">// En Bootstrap 5, alternamos las clases nativas de validación:</span>
<span class="code-token-keyword">if</span> (input.checkValidity()) {
    input.classList.<span class="code-token-function">remove</span>(<span class="code-token-string">"is-invalid"</span>);
    input.classList.<span class="code-token-function">add</span>(<span class="code-token-string">"is-valid"</span>);
} <span class="code-token-keyword">else</span> {
    input.classList.<span class="code-token-function">remove</span>(<span class="code-token-string">"is-valid"</span>);
    input.classList.<span class="code-token-function">add</span>(<span class="code-token-string">"is-invalid"</span>);
}</code></pre>
                    </div>
                    <div class="alert alert-success border-0 small mb-0">
                        <i class="bi bi-check-circle me-1"></i> <strong>Contenedores de feedback de Bootstrap:</strong> Junto a cada control podemos situar <code>&lt;div class="invalid-feedback"&gt;Mensaje de error claro&lt;/div&gt;</code> para una experiencia visual limpia, accesible y ergonómica.
                    </div>
                </section>

                <!-- SECCIÓN OFICIAL DE EJERCICIOS DEL TEMA 6 -->
                <section id="sec-ejercicios" class="card content-card shadow-sm p-4">
                    <div class="d-flex align-items-center justify-content-between flex-wrap gap-2 mb-3">
                        <div class="d-flex align-items-center gap-2">
                            <span class="badge text-bg-warning fs-6"><i class="bi bi-pencil-square"></i></span>
                            <h2 class="h4 mb-0 fw-bold">Boletín Oficial de Ejercicios del Tema 6</h2>
                        </div>
                        <a href="07_ejercicios.html" class="btn btn-sm btn-outline-warning text-dark fw-semibold"><i class="bi bi-collection me-1"></i> Catálogo Global</a>
                    </div>
                    <p class="text-secondary small mb-4">
                        Colección oficial de ejercicios prácticos de validación de formularios:
                    </p>

                    <div class="row g-3">
                        
                        <!-- Ejercicio 6.1 -->
                        <div class="col-md-4">
                            <div class="card h-100 border exercise-card shadow-sm">
                                <div class="card-header bg-dark text-white d-flex justify-content-between align-items-center py-2">
                                    <span class="fw-bold small">Ejercicio 6.1</span>
                                    <span class="badge text-bg-warning text-dark">01_form_js.html</span>
                                </div>
                                <div class="card-body p-3 d-flex flex-column justify-content-between">
                                    <p class="small text-secondary mb-3">
                                        Acceso a todos los controles básicos de formulario: input de texto, numérico, checkbox, grupo de radio buttons y lista select.
                                    </p>
                                    <div class="d-flex gap-2">
                                        <a href="../material/ejercicios/aprendizaje/t6_01_form_js.html" target="_blank" class="btn btn-sm btn-dark flex-grow-1"><i class="bi bi-play me-1"></i> Probar</a>
                                        <a href="07_ejercicios_r.html#ej_6_1" class="btn btn-sm btn-outline-dark"><i class="bi bi-code-slash"></i> Solución</a>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- Ejercicio 6.2 -->
                        <div class="col-md-4">
                            <div class="card h-100 border exercise-card shadow-sm">
                                <div class="card-header bg-dark text-white d-flex justify-content-between align-items-center py-2">
                                    <span class="fw-bold small">Ejercicio 6.2</span>
                                    <span class="badge text-bg-warning text-dark">02_form_js.html</span>
                                </div>
                                <div class="card-body p-3 d-flex flex-column justify-content-between">
                                    <p class="small text-secondary mb-3">
                                        Interceptación de envío con el evento <code>submit</code> y cancelación controlada mediante <code>e.preventDefault()</code> ante datos incompletos.
                                    </p>
                                    <div class="d-flex gap-2">
                                        <a href="../material/ejercicios/aprendizaje/t6_02_form_js.html" target="_blank" class="btn btn-sm btn-dark flex-grow-1"><i class="bi bi-play me-1"></i> Probar</a>
                                        <a href="07_ejercicios_r.html#ej_6_2" class="btn btn-sm btn-outline-dark"><i class="bi bi-code-slash"></i> Solución</a>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- Ejercicio 6.3 -->
                        <div class="col-md-4">
                            <div class="card h-100 border exercise-card shadow-sm">
                                <div class="card-header bg-dark text-white d-flex justify-content-between align-items-center py-2">
                                    <span class="fw-bold small">Ejercicio 6.3</span>
                                    <span class="badge text-bg-warning text-dark">03_form_js.html</span>
                                </div>
                                <div class="card-body p-3 d-flex flex-column justify-content-between">
                                    <p class="small text-secondary mb-3">
                                        Integración con HTML5 y Constraint Validation: validación de contraseñas dobles y mensajes custom con <code>setCustomValidity()</code>.
                                    </p>
                                    <div class="d-flex gap-2">
                                        <a href="../material/ejercicios/aprendizaje/t6_03_form_js.html" target="_blank" class="btn btn-sm btn-dark flex-grow-1"><i class="bi bi-play me-1"></i> Probar</a>
                                        <a href="07_ejercicios_r.html#ej_6_3" class="btn btn-sm btn-outline-dark"><i class="bi bi-code-slash"></i> Solución</a>
                                    </div>
                                </div>
                            </div>
                        </div>

                    </div>
                </section>

                <!-- Paginación Inferior -->
                <nav class="d-flex justify-content-between align-items-center mt-2 pt-3 border-top" aria-label="Navegación de temas">
                    <a href="05_eventos.html" class="btn btn-outline-secondary d-flex align-items-center gap-2">
                        <i class="bi bi-arrow-left"></i>
                        <span>Tema 5: Gestión de Eventos</span>
                    </a>
                    <a href="07_ejercicios.html" class="btn btn-warning text-dark fw-bold d-flex align-items-center gap-2">
                        <span>Catálogo de Ejercicios Prácticos</span>
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
                            <a class="nav-link px-2 py-1 text-secondary text-truncate" href="#sec6-1"><i class="bi bi-chevron-right me-1"></i> 6.1 Validación Tradicional</a>
                            <a class="nav-link px-2 py-1 text-secondary text-truncate" href="#sec6-1-1"><i class="bi bi-chevron-right me-1"></i> 6.1.1 Acceso Controles</a>
                            <a class="nav-link px-2 py-1 text-secondary text-truncate" href="#sec6-1-2"><i class="bi bi-chevron-right me-1"></i> 6.1.2 Consulta Valores</a>
                            <a class="nav-link px-2 py-1 text-secondary text-truncate" href="#sec6-1-3"><i class="bi bi-chevron-right me-1"></i> 6.1.3 Expresiones RegEx</a>
                            <a class="nav-link px-2 py-1 text-secondary text-truncate" href="#sec6-1-4"><i class="bi bi-chevron-right me-1"></i> 6.1.4 Envío y submit</a>
                            <a class="nav-link px-2 py-1 text-secondary text-truncate" href="#sec6-2"><i class="bi bi-chevron-right me-1"></i> 6.2 Validación HTML5</a>
                            <a class="nav-link px-2 py-1 text-secondary text-truncate" href="#sec6-2-2"><i class="bi bi-chevron-right me-1"></i> 6.2.2 Custom Validity</a>
                            <a class="nav-link px-2 py-1 text-secondary text-truncate" href="#sec6-2-3"><i class="bi bi-chevron-right me-1"></i> 6.2.3 CSS y Bootstrap 5</a>
                            <a class="nav-link px-2 py-1 text-warning fw-bold text-truncate" href="#sec-ejercicios"><i class="bi bi-pencil-square me-1"></i> Ejercicios 6.1 - 6.3</a>
                        </nav>
                        
                        <div class="border-top mt-3 pt-3">
                            <a href="../material/t6_formularios.pdf" target="_blank" class="btn btn-outline-danger btn-sm w-100 d-flex align-items-center justify-content-center gap-1">
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
    with open("javascript/archivos/06_formularios.html", "w", encoding="utf-8") as f:
        f.write(doc)
    print("06_formularios.html generated successfully! Length:", len(doc))

if __name__ == '__main__':
    generate_t6_page()
