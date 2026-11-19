import os

def generate_t2_page():
    doc = """<!DOCTYPE html>
<html lang="es" data-bs-theme="light">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>02. Funciones y Modularidad | JavaScript | LMSGI</title>
    <meta name="description" content="Tema 2: Definición de funciones, parámetros, valores por defecto, tipo de retorno, ámbito de variables, funciones predefinidas (Strings, Math, Date) y arrow functions.">
    
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
                <a href="02_funciones.html" class="list-group-item list-group-item-action active bg-warning text-dark border-warning fw-semibold d-flex align-items-center gap-2 py-2"><i class="bi bi-braces text-dark"></i> 02. Funciones y Modularidad</a>
                <a href="03_arrays.html" class="list-group-item list-group-item-action bg-transparent text-light border-secondary d-flex align-items-center gap-2 py-2"><i class="bi bi-collection text-warning"></i> 03. Arrays y Objetos</a>
                <a href="04_dom.html" class="list-group-item list-group-item-action bg-transparent text-light border-secondary d-flex align-items-center gap-2 py-2"><i class="bi bi-diagram-3 text-warning"></i> 04. DOM y BOM</a>
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
                <li class="breadcrumb-item active text-dark fw-semibold" aria-current="page">02. Funciones y Modularidad</li>
            </ol>
        </nav>

        <!-- Hero Header del Tema -->
        <div class="card bg-warning-subtle border-warning-subtle shadow-sm mb-4">
            <div class="card-body p-4 p-lg-5">
                <div class="d-flex flex-wrap align-items-center gap-2 mb-3">
                    <span class="badge text-bg-warning px-3 py-2 fs-6 fw-bold text-dark"><i class="bi bi-file-earmark-pdf me-1"></i> Manual Oficial: Tema 2</span>
                    <span class="badge bg-dark text-white px-3 py-2 fs-6">Teoría Completa & Ejercicios 2.1 - 2.10</span>
                </div>
                <h1 class="display-5 fw-bold text-dark mb-3">Tema 2: Funciones y Modularidad</h1>
                <p class="lead text-dark-emphasis mb-4">
                    Estructuración modular de aplicaciones en JavaScript: creación de funciones, paso de argumentos, valores predeterminados en ES6, retornos de datos, ámbito de variables (local vs global), modo estricto, métodos predefinidos (String, Math, Date), funciones anónimas, expresiones lambda (arrow functions) y carga de múltiples archivos externos.
                </p>
                
                <!-- Píldoras de Acceso Rápido a Secciones -->
                <div class="d-flex flex-wrap gap-2 pt-2 border-top border-warning-subtle">
                    <a href="#sec2-1" class="btn btn-sm btn-outline-dark bg-white rounded-pill"><i class="bi bi-hash"></i> 2.1 Definición de Funciones</a>
                    <a href="#sec2-1-1" class="btn btn-sm btn-outline-dark bg-white rounded-pill"><i class="bi bi-hash"></i> 2.1.1 Parámetros</a>
                    <a href="#sec2-1-2" class="btn btn-sm btn-outline-dark bg-white rounded-pill"><i class="bi bi-hash"></i> 2.1.2 Parámetros por Defecto</a>
                    <a href="#sec2-1-3" class="btn btn-sm btn-outline-dark bg-white rounded-pill"><i class="bi bi-hash"></i> 2.1.3 Tipo de Retorno</a>
                    <a href="#sec2-1-4" class="btn btn-sm btn-outline-dark bg-white rounded-pill"><i class="bi bi-hash"></i> 2.1.4 Ámbito y Modo Estricto</a>
                    <a href="#sec2-2" class="btn btn-sm btn-outline-dark bg-white rounded-pill"><i class="bi bi-hash"></i> 2.2 Funciones Útiles (String, Math, Date)</a>
                    <a href="#sec2-3" class="btn btn-sm btn-outline-dark bg-white rounded-pill"><i class="bi bi-hash"></i> 2.3 Opciones Avanzadas (Lambdas)</a>
                    <a href="#sec-ejercicios" class="btn btn-sm btn-warning text-dark fw-bold rounded-pill"><i class="bi bi-pencil-square"></i> Ejercicios 2.1 a 2.10</a>
                </div>
            </div>
        </div>

        <div class="row g-4">
            
            <!-- Columna Principal de Contenido (9 cols en lg) -->
            <div class="col-lg-9 d-flex flex-column gap-4">

                <!-- 2.1 Definición de funciones -->
                <section id="sec2-1" class="card content-card shadow-sm p-4">
                    <div class="d-flex align-items-center gap-2 mb-3">
                        <span class="badge text-bg-warning fs-6">2.1</span>
                        <h2 class="h4 mb-0 fw-bold">Definición de Funciones</h2>
                    </div>
                    <p>
                        Si colocamos cualquier instrucción JavaScript suelta en una página, se ejecutará nada más cargar el documento, y habitualmente no es lo deseado. Lo natural es que el código se active o responda a medida que el usuario realiza acciones (por ejemplo, pulsar un botón, validar un formulario o seleccionar un menú).
                    </p>
                    <p>
                        Para evitar la ejecución inmediata, estructurar la lógica en bloques reutilizables y mantener un código limpio, utilizamos <strong>funciones</strong>. Una función es un fragmento de código con nombre que podemos invocar en cualquier momento tantas veces como sea necesario.
                    </p>
                    <p>
                        Se crean con la palabra reservada <code>function</code>, seguida del identificador y un par de paréntesis <code>()</code>. Entre llaves <code>{ ... }</code> se colocan las sentencias que forman su cuerpo:
                    </p>
                    <div class="code-block mb-3">
<pre class="m-0"><code><span class="code-token-keyword">function</span> <span class="code-token-function">sumaVariables</span>() {
    <span class="code-token-keyword">let</span> num1 = <span class="code-token-number">2</span>;
    <span class="code-token-keyword">let</span> num2 = <span class="code-token-number">6</span>;
    <span class="code-token-keyword">let</span> suma = num1 + num2;
    <span class="code-token-function">alert</span>(<span class="code-token-string">"El resultado de la suma es "</span> + suma);
}</code></pre>
                    </div>
                    <p>
                        Para activar este bloque cuando el usuario interactúa (por ejemplo al hacer clic sobre un párrafo de texto), se vincula la llamada entre paréntesis:
                    </p>
                    <div class="code-block mb-3">
<pre class="m-0"><code><span class="code-token-tag">&lt;p</span> <span class="code-token-attr">onclick=</span><span class="code-token-string">"sumaVariables()"</span><span class="code-token-tag">&gt;</span>Haz clic aquí para sumar variables<span class="code-token-tag">&lt;/p&gt;</span></code></pre>
                    </div>
                    <div class="alert alert-info border-0 shadow-sm d-flex align-items-start gap-2 mb-0 small">
                        <i class="bi bi-info-circle-fill fs-5 text-info flex-shrink-0 mt-1"></i>
                        <div>
                            <strong>Hoisting de funciones:</strong> En JavaScript tradicional con declaraciones <code>function</code>, el orden en el que se definen las funciones es indiferente: el motor las eleva (hoisting) en la fase de análisis, por lo que pueden invocarse antes o después de la línea donde están declaradas.
                        </div>
                    </div>
                </section>

                <!-- 2.1.1 Uso de parámetros -->
                <section id="sec2-1-1" class="card content-card shadow-sm p-4">
                    <div class="d-flex align-items-center gap-2 mb-3">
                        <span class="badge text-bg-warning fs-6">2.1.1</span>
                        <h2 class="h4 mb-0 fw-bold">Uso de Parámetros</h2>
                    </div>
                    <p>
                        Entre los paréntesis de una función podemos definir, separados por comas, variables denominadas <strong>parámetros</strong>. Estos reciben valores (argumentos) desde el punto donde se invoca la función para trabajar dinámicamente con ellos:
                    </p>
                    <div class="code-block mb-3">
<pre class="m-0"><code><span class="code-token-keyword">function</span> <span class="code-token-function">sumaDatos</span>(num1, num2) {
    <span class="code-token-keyword">let</span> suma = num1 + num2;
    <span class="code-token-function">alert</span>(<span class="code-token-string">"El resultado de la suma es "</span> + suma);
}</code></pre>
                    </div>
                    <p>
                        Al llamarla, le pasamos los datos concretos que se asignarán en orden a <code>num1</code> y <code>num2</code>:
                    </p>
                    <div class="code-block mb-3">
<pre class="m-0"><code><span class="code-token-comment">// Invocación con argumentos 3 y 5:</span>
<span class="code-token-function">sumaDatos</span>(<span class="code-token-number">3</span>, <span class="code-token-number">5</span>); <span class="code-token-comment">// Muestra 8</span></code></pre>
                    </div>
                    <div class="alert alert-light border small mb-0">
                        <strong>Nomenclatura Camel Case:</strong> En JavaScript es convención estándar que tanto los nombres de funciones como de variables comiencen en minúscula y cada palabra sucesiva inicie en mayúscula (ejemplo: <code>sumaDatos</code>, <code>calcularPrecioTotal</code>, <code>nombreUsuario</code>).
                    </div>

                    <!-- Tarjeta del Ejercicio 2.1 -->
                    <div class="card exercise-card border-warning bg-warning-subtle shadow-sm p-3 mt-4">
                        <div class="d-flex align-items-center justify-content-between mb-2">
                            <h4 class="h6 fw-bold text-dark mb-0"><i class="bi bi-pencil-square me-1"></i> Ejercicio 2.1: Cuatro Operaciones Básicas con Parámetros</h4>
                            <span class="badge bg-warning text-dark border border-dark-subtle">Ejercicio Oficial</span>
                        </div>
                        <p class="small text-dark-emphasis mb-2">
                            Crear un documento llamado <code>01_operaciones_funcion_js.html</code> con cuatro párrafos en HTML: <em>"Suma"</em>, <em>"Resta"</em>, <em>"Multiplicación"</em> y <em>"División"</em>.
                        </p>
                        <ul class="small text-dark-emphasis mb-3 ps-3">
                            <li>Definir cuatro funciones (<code>sumar</code>, <code>restar</code>, <code>multiplicar</code>, <code>dividir</code>) que reciban dos números como parámetro.</li>
                            <li>Vincular cada párrafo mediante <code>onclick</code> para que al pulsar se llame a la función correspondiente pasándole los números deseados.</li>
                        </ul>
                        <div class="d-flex flex-wrap gap-2">
                            <a href="../material/ejercicios/aprendizaje/t2_01_operaciones_funcion_js.html" target="_blank" class="btn btn-sm btn-dark"><i class="bi bi-play-circle me-1"></i> Probar Solución</a>
                            <a href="07_ejercicios_r.html#ej_2_1" class="btn btn-sm btn-outline-dark"><i class="bi bi-code-slash me-1"></i> Ver Código Resuelto</a>
                        </div>
                    </div>
                </section>

                <!-- 2.1.2 Parámetros por defecto -->
                <section id="sec2-1-2" class="card content-card shadow-sm p-4">
                    <div class="d-flex align-items-center gap-2 mb-3">
                        <span class="badge text-bg-warning fs-6">2.1.2</span>
                        <h2 class="h4 mb-0 fw-bold">Número de Parámetros y Parámetros por Defecto</h2>
                    </div>
                    <p>
                        JavaScript es muy flexible en el paso de argumentos:
                    </p>
                    <ul>
                        <li>Si llamamos a una función con <strong>menos argumentos</strong> de los declarados, los parámetros ausentes toman el valor <code>undefined</code>.</li>
                        <li>Si enviamos <strong>argumentos de más</strong>, el intérprete no da error y simplemente descarta los sobrantes (accesibles internamente mediante el objeto <code>arguments</code> o el operador rest <code>...args</code>).</li>
                    </ul>
                    <p>
                        A partir del estándar ECMAScript 2015 (ES6), podemos establecer <strong>valores predeterminados</strong> directamente en la cabecera de la función:
                    </p>
                    <div class="code-block mb-3">
<pre class="m-0"><code><span class="code-token-keyword">function</span> <span class="code-token-function">sumaDatos</span>(num1, num2 = <span class="code-token-number">0</span>) {
    <span class="code-token-keyword">let</span> suma = num1 + num2;
    <span class="code-token-function">alert</span>(<span class="code-token-string">"El resultado de la suma es "</span> + suma);
}

<span class="code-token-function">sumaDatos</span>(<span class="code-token-number">3</span>, <span class="code-token-number">2</span>); <span class="code-token-comment">// Resultado: 5 (num2 toma 2)</span>
<span class="code-token-function">sumaDatos</span>(<span class="code-token-number">3</span>);    <span class="code-token-comment">// Resultado: 3 (num2 adopta automáticamente el valor por defecto 0)</span></code></pre>
                    </div>
                    <div class="alert alert-warning border-0 p-3 small mb-0">
                        <strong>Regla de diseño:</strong> Los parámetros con valores por defecto deben colocarse siempre <strong>al final de la lista</strong> de parámetros, para no alterar la correspondencia de los argumentos obligatorios.
                    </div>
                </section>

                <!-- 2.1.3 Tipo de retorno -->
                <section id="sec2-1-3" class="card content-card shadow-sm p-4">
                    <div class="d-flex align-items-center gap-2 mb-3">
                        <span class="badge text-bg-warning fs-6">2.1.3</span>
                        <h2 class="h4 mb-0 fw-bold">Tipo de Retorno (Sentencia return)</h2>
                    </div>
                    <p>
                        En la mayoría de los casos no deseamos que la función muestre directamente una alerta, sino que <strong>calcule y devuelva un resultado</strong> para almacenarlo en una variable o encadenarlo en otras operaciones matemáticas:
                    </p>
                    <div class="code-block mb-3">
<pre class="m-0"><code><span class="code-token-keyword">function</span> <span class="code-token-function">calcularPrecioTotal</span>(precio, iva = <span class="code-token-number">21</span>) {
    <span class="code-token-keyword">let</span> total = precio + (precio * iva / <span class="code-token-number">100</span>);
    <span class="code-token-keyword">return</span> total; <span class="code-token-comment">// Devuelve el valor calculado</span>
}

<span class="code-token-keyword">let</span> factura = <span class="code-token-function">calcularPrecioTotal</span>(<span class="code-token-number">100</span>);
<span class="code-token-function">console</span>.<span class="code-token-function">log</span>(<span class="code-token-string">"Importe total con IVA: "</span> + factura); <span class="code-token-comment">// 121</span></code></pre>
                    </div>
                    <p class="small text-secondary mb-0">
                        La sentencia <code>return</code> interrumpe de inmediato la ejecución de la función y devuelve el valor especificado al punto de llamada. Si una función no incluye <code>return</code>, devuelve implícitamente <code>undefined</code>.
                    </p>

                    <!-- Tarjetas de Ejercicios 2.2 y 2.3 -->
                    <div class="row g-3 mt-3">
                        <div class="col-md-6">
                            <div class="card exercise-card border-warning bg-warning-subtle shadow-sm p-3 h-100">
                                <h4 class="h6 fw-bold text-dark mb-1"><i class="bi bi-pencil-square me-1"></i> Ejercicio 2.2: Cálculo de Precios con IVA</h4>
                                <p class="small text-dark-emphasis mb-2">
                                    Página <code>02_calcular_precio_js.html</code> con función <code>calcularPrecio(producto, precio, iva)</code> con valores por defecto <em>"Producto genérico"</em>, <code>100</code> y <code>21</code>. Validar que precio e IVA sean números e imprimir por consola.
                                </p>
                                <div class="d-flex gap-2 mt-auto">
                                    <a href="../material/ejercicios/aprendizaje/t2_02_calcular_precio_js.html" target="_blank" class="btn btn-sm btn-dark flex-grow-1"><i class="bi bi-play me-1"></i> Probar</a>
                                    <a href="07_ejercicios_r.html#ej_2_2" class="btn btn-sm btn-outline-dark"><i class="bi bi-code-slash"></i> Solución</a>
                                </div>
                            </div>
                        </div>
                        <div class="col-md-6">
                            <div class="card exercise-card border-warning bg-warning-subtle shadow-sm p-3 h-100">
                                <h4 class="h6 fw-bold text-dark mb-1"><i class="bi bi-pencil-square me-1"></i> Ejercicio 2.3: Tabla de Multiplicar Dinámica</h4>
                                <p class="small text-dark-emphasis mb-2">
                                    Página <code>03_tabla_multiplicar_js.html</code> que solicita un número del 1 al 10 en bucle hasta ser válido y, mediante una función, escribe la tabla en el HTML como lista no ordenada (<code>&lt;ul&gt;</code>).
                                </p>
                                <div class="d-flex gap-2 mt-auto">
                                    <a href="../material/ejercicios/aprendizaje/t2_03_tabla_multiplicar_js.html" target="_blank" class="btn btn-sm btn-dark flex-grow-1"><i class="bi bi-play me-1"></i> Probar</a>
                                    <a href="07_ejercicios_r.html#ej_2_3" class="btn btn-sm btn-outline-dark"><i class="bi bi-code-slash"></i> Solución</a>
                                </div>
                            </div>
                        </div>
                    </div>
                </section>

                <!-- 2.1.4 Variables locales y globales -->
                <section id="sec2-1-4" class="card content-card shadow-sm p-4">
                    <div class="d-flex align-items-center gap-2 mb-3">
                        <span class="badge text-bg-warning fs-6">2.1.4</span>
                        <h2 class="h4 mb-0 fw-bold">Variables Locales, Globales y Modo Estricto</h2>
                    </div>
                    <p>
                        El <strong>ámbito (scope)</strong> define en qué regiones del código es accesible una variable:
                    </p>
                    <div class="row g-3 mb-3">
                        <div class="col-md-6">
                            <div class="p-3 border rounded bg-body-tertiary h-100">
                                <h6 class="fw-bold text-primary mb-1">Variables Locales (Block Scope)</h6>
                                <p class="small text-secondary mb-0">
                                    Una variable declarada con <code>let</code> o <code>const</code> dentro de una función o bloque <code>{ ... }</code> solo existe dentro de dicho bloque. Fuera de él, no es accesible. Si coincide de nombre con una variable global, la local prevalece (sombreado).
                                </p>
                            </div>
                        </div>
                        <div class="col-md-6">
                            <div class="p-3 border rounded bg-body-tertiary h-100">
                                <h6 class="fw-bold text-success mb-1">Variables Globales</h6>
                                <p class="small text-secondary mb-0">
                                    Una variable declarada en el cuerpo principal del script (fuera de cualquier función) es global y accesible por todas las funciones de la página.
                                </p>
                            </div>
                        </div>
                    </div>

                    <div class="alert alert-dark border-0 p-3 small mb-0">
                        <h6 class="fw-bold mb-1"><i class="bi bi-code-slash me-1"></i> Modo Estricto ('use strict')</h6>
                        <p class="mb-2">
                            Si en JavaScript estándar asignamos un valor a una variable que nunca fue declarada con <code>let</code>, <code>const</code> o <code>var</code>, el motor crea automáticamente una variable global, lo que provoca fugas de memoria y errores sutiles. Para evitarlo, activamos el modo estricto al inicio del archivo:
                        </p>
                        <div class="code-block m-0">
<pre class="m-0"><code><span class="code-token-string">'use strict'</span>;

numero = <span class="code-token-number">10</span>; <span class="code-token-comment">// ¡ReferenceError! En modo estricto obliga a usar let o const</span></code></pre>
                        </div>
                    </div>
                </section>

                <!-- 2.2 Algunas funciones útiles -->
                <section id="sec2-2" class="card content-card shadow-sm p-4">
                    <div class="d-flex align-items-center gap-2 mb-3">
                        <span class="badge text-bg-warning fs-6">2.2</span>
                        <h2 class="h4 mb-0 fw-bold">Funciones Predefinidas Útiles (Strings, Math, Date)</h2>
                    </div>
                    <p>
                        JavaScript proporciona métodos y utilidades integrados para simplificar las tareas cotidianas sobre textos, números y fechas:
                    </p>

                    <!-- 2.2.1 Textos -->
                    <h3 class="h5 fw-bold text-dark mt-3 mb-2">2.2.1 Manejo de Cadenas de Texto (String)</h3>
                    <div class="table-responsive table-custom mb-3">
                        <table class="table table-hover align-middle mb-0 small">
                            <thead>
                                <tr>
                                    <th>Propiedad / Método</th>
                                    <th>Descripción</th>
                                    <th>Ejemplo</th>
                                    <th>Resultado</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr><td><code>texto.length</code></td><td>Número de caracteres</td><td><code>"Hola".length</code></td><td><code>4</code></td></tr>
                                <tr><td><code>texto[i]</code> / <code>charAt(i)</code></td><td>Carácter en la posición indicada (inicia en 0)</td><td><code>"Hola".charAt(1)</code></td><td><code>"o"</code></td></tr>
                                <tr><td><code>indexOf(sub)</code></td><td>Posición de la subcadena (-1 si no está)</td><td><code>"Hola buenas".indexOf("buenas")</code></td><td><code>5</code></td></tr>
                                <tr><td><code>includes(sub)</code></td><td>Comprueba si el texto contiene la subcadena</td><td><code>"Hola".includes("ol")</code></td><td><code>true</code></td></tr>
                                <tr><td><code>startsWith()</code> / <code>endsWith()</code></td><td>Verifica el inicio o final de la cadena</td><td><code>"foto.jpg".endsWith(".jpg")</code></td><td><code>true</code></td></tr>
                                <tr><td><code>toUpperCase()</code> / <code>toLowerCase()</code></td><td>Convierte a mayúsculas o minúsculas</td><td><code>"Hola".toUpperCase()</code></td><td><code>"HOLA"</code></td></tr>
                                <tr><td><code>replace(viejo, nuevo)</code></td><td>Reemplaza la primera coincidencia</td><td><code>"Hola bu".replace("bu", "BU")</code></td><td><code>"Hola BU"</code></td></tr>
                                <tr><td><code>substring(inicio, fin)</code></td><td>Extrae entre dos índices (fin no incluido)</td><td><code>"Hola buenas".substring(5, 7)</code></td><td><code>"bu"</code></td></tr>
                                <tr><td><code>slice(inicio, fin)</code></td><td>Permite índices negativos desde el final</td><td><code>"archivo.pdf".slice(-3)</code></td><td><code>"pdf"</code></td></tr>
                                <tr><td><code>split(separador)</code></td><td>Parte la cadena y devuelve un Array</td><td><code>"1,2,3".split(",")</code></td><td><code>["1", "2", "3"]</code></td></tr>
                                <tr><td><code>trim()</code></td><td>Elimina espacios en blanco al inicio y al final</td><td><code>"  test  ".trim()</code></td><td><code>"test"</code></td></tr>
                            </tbody>
                        </table>
                    </div>

                    <!-- Tarjeta del Ejercicio 2.4 -->
                    <div class="card exercise-card border-warning bg-warning-subtle shadow-sm p-3 mb-4">
                        <h4 class="h6 fw-bold text-dark mb-1"><i class="bi bi-pencil-square me-1"></i> Ejercicio 2.4: Manipulación Avanzada de Cadenas</h4>
                        <p class="small text-dark-emphasis mb-2">
                            Página <code>04_ejercicio_strings_js.html</code> con tres funciones:
                        </p>
                        <ol class="small text-dark-emphasis mb-3 ps-3">
                            <li>Eliminar de un texto $t_1$ todas las apariciones de $t_2$.</li>
                            <li>Comprobar si el nombre de un archivo corresponde a una imagen JPG o PNG (usando <code>endsWith()</code> o <code>slice()</code>).</li>
                            <li>Validar si una matrícula es válida (compuesta por 4 dígitos y 3 letras mayúsculas).</li>
                        </ol>
                        <div class="d-flex gap-2">
                            <a href="../material/ejercicios/aprendizaje/t2_04_ejercicio_strings_js.html" target="_blank" class="btn btn-sm btn-dark"><i class="bi bi-play me-1"></i> Probar</a>
                            <a href="07_ejercicios_r.html#ej_2_4" class="btn btn-sm btn-outline-dark"><i class="bi bi-code-slash"></i> Solución</a>
                        </div>
                    </div>

                    <!-- 2.2.2 Matemáticas -->
                    <h3 class="h5 fw-bold text-dark mt-4 mb-2">2.2.2 Funciones Matemáticas (Objeto Math)</h3>
                    <div class="table-responsive table-custom mb-3">
                        <table class="table table-hover align-middle mb-0 small">
                            <thead>
                                <tr>
                                    <th>Constante / Método</th>
                                    <th>Operación</th>
                                    <th>Ejemplo</th>
                                    <th>Resultado</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr><td><code>Math.PI</code> / <code>Math.E</code></td><td>Constantes $\pi$ y $e$</td><td><code>Math.PI</code></td><td><code>3.14159265...</code></td></tr>
                                <tr><td><code>Math.round(x)</code></td><td>Redondeo al entero más próximo</td><td><code>Math.round(4.6)</code></td><td><code>5</code></td></tr>
                                <tr><td><code>Math.floor(x)</code> / <code>Math.ceil(x)</code></td><td>Aproxima por abajo / por arriba</td><td><code>Math.ceil(3.12)</code></td><td><code>4</code></td></tr>
                                <tr><td><code>Math.min(...)</code> / <code>Math.max(...)</code></td><td>Valor mínimo / máximo</td><td><code>Math.min(2, 6, 1, 7)</code></td><td><code>1</code></td></tr>
                                <tr><td><code>Math.pow(base, exp)</code></td><td>Potencia ($b^e$)</td><td><code>Math.pow(3, 2)</code></td><td><code>9</code></td></tr>
                                <tr><td><code>Math.abs(x)</code></td><td>Valor absoluto ($|x|$)</td><td><code>Math.abs(-3)</code></td><td><code>3</code></td></tr>
                                <tr><td><code>Math.sqrt(x)</code></td><td>Raíz cuadrada ($\sqrt{x}$)</td><td><code>Math.sqrt(16)</code></td><td><code>4</code></td></tr>
                                <tr><td><code>Math.random()</code></td><td>Número aleatorio en $[0, 1)$</td><td><code>Math.floor(Math.random() * 10) + 1</code></td><td>Entero entre 1 y 10</td></tr>
                            </tbody>
                        </table>
                    </div>

                    <!-- 2.2.3 Fechas -->
                    <h3 class="h5 fw-bold text-dark mt-4 mb-2">2.2.3 Gestión de Fechas (Objeto Date)</h3>
                    <div class="code-block mb-3">
<pre class="m-0"><code><span class="code-token-keyword">let</span> fechaActual = <span class="code-token-keyword">new</span> <span class="code-token-function">Date</span>();                      <span class="code-token-comment">// Fecha y hora exactas del sistema</span>
<span class="code-token-keyword">let</span> fechaEspecifica = <span class="code-token-keyword">new</span> <span class="code-token-function">Date</span>(<span class="code-token-number">2026</span>, <span class="code-token-number">3</span>, <span class="code-token-number">4</span>);          <span class="code-token-comment">// 4 de abril (mes 3, enero es 0)</span>
<span class="code-token-keyword">let</span> fechaIso = <span class="code-token-keyword">new</span> <span class="code-token-function">Date</span>(<span class="code-token-string">"2026-04-04"</span>);              <span class="code-token-comment">// A partir de cadena ISO</span>
<span class="code-token-keyword">let</span> milisegundos = <span class="code-token-function">Date</span>.<span class="code-token-function">now</span>();                       <span class="code-token-comment">// Milisegundos transcurridos desde 01/01/1970</span>
<span class="code-token-keyword">let</span> formateada = fechaEspecifica.<span class="code-token-function">toLocaleDateString</span>(); <span class="code-token-comment">// Formato local: "4/4/2026"</span></code></pre>
                    </div>
                </section>

                <!-- 2.3 Opciones avanzadas con funciones -->
                <section id="sec2-3" class="card content-card shadow-sm p-4">
                    <div class="d-flex align-items-center gap-2 mb-3">
                        <span class="badge text-bg-warning fs-6">2.3</span>
                        <h2 class="h4 mb-0 fw-bold">Opciones Avanzadas: Funciones Anónimas y Arrow Functions</h2>
                    </div>

                    <!-- 2.3.1 Funciones anónimas -->
                    <div class="border rounded p-3 mb-4 bg-body-tertiary">
                        <h3 class="h5 fw-bold text-dark mb-2">2.3.1 Funciones Anónimas</h3>
                        <p class="small mb-2">
                            Son funciones que carecen de nombre identificador. Habitualmente se asignan a una variable o se pasan como argumento inmediato a callbacks:
                        </p>
                        <div class="code-block">
<pre class="m-0"><code><span class="code-token-keyword">let</span> suma = <span class="code-token-keyword">function</span>(n1, n2) {
    <span class="code-token-keyword">return</span> n1 + n2;
};

<span class="code-token-function">console</span>.<span class="code-token-function">log</span>(<span class="code-token-function">suma</span>(<span class="code-token-number">4</span>, <span class="code-token-number">3</span>)); <span class="code-token-comment">// 7</span></code></pre>
                        </div>
                    </div>

                    <!-- 2.3.2 Funciones lambda o arrow functions -->
                    <div class="border rounded p-3 mb-4 bg-body-tertiary">
                        <div class="d-flex align-items-center gap-2 mb-2">
                            <h3 class="h5 fw-bold text-dark mb-0">2.3.2 Funciones Lambda o Arrow Functions (=>)</h3>
                            <span class="badge bg-primary">ES2015+</span>
                        </div>
                        <p class="small mb-2">
                            Proporcionan una sintaxis compacta y limpia utilizando la flecha <code>=&gt;</code>:
                        </p>
                        <div class="code-block mb-3">
<pre class="m-0"><code><span class="code-token-comment">// Sintaxis con bloque:</span>
<span class="code-token-keyword">let</span> suma = (n1, n2) =&gt; {
    <span class="code-token-keyword">return</span> n1 + n2;
};

<span class="code-token-comment">// Retorno implícito directo (omitiendo llaves y palabra return):</span>
<span class="code-token-keyword">let</span> sumaCompacta = (n1, n2) =&gt; n1 + n2;

<span class="code-token-comment">// Si tiene un único parámetro, se pueden omitir los paréntesis:</span>
<span class="code-token-keyword">let</span> cuadrado = x =&gt; x * x;</code></pre>
                        </div>

                        <!-- Tarjeta del Ejercicio 2.5 -->
                        <div class="card exercise-card border-warning bg-warning-subtle shadow-sm p-3">
                            <h4 class="h6 fw-bold text-dark mb-1"><i class="bi bi-pencil-square me-1"></i> Ejercicio 2.5: Reescribir con Funciones Flecha</h4>
                            <p class="small text-dark-emphasis mb-2">
                                Crear la página <code>05_ejercicio_lambdas_js.html</code> repitiendo las funciones de cadenas del Ejercicio 2.4 pero implementadas obligatoriamente como funciones lambda (arrow functions).
                            </p>
                            <div class="d-flex gap-2">
                                <a href="../material/ejercicios/aprendizaje/t2_05_ejercicio_lambdas_js.html" target="_blank" class="btn btn-sm btn-dark"><i class="bi bi-play me-1"></i> Probar</a>
                                <a href="07_ejercicios_r.html#ej_2_5" class="btn btn-sm btn-outline-dark"><i class="bi bi-code-slash"></i> Solución</a>
                            </div>
                        </div>
                    </div>

                    <!-- 2.3.3 Cargar diversos archivos fuente -->
                    <div class="border rounded p-3 bg-body-tertiary">
                        <h3 class="h5 fw-bold text-dark mb-2">2.3.3 Carga de Múltiples Archivos Fuente</h3>
                        <p class="small mb-2">
                            En proyectos grandes es una buena práctica modularizar el código dividiéndolo en varios archivos independientes:
                        </p>
                        <div class="code-block mb-3">
<pre class="m-0"><code><span class="code-token-tag">&lt;script</span> <span class="code-token-attr">src=</span><span class="code-token-string">"utilidades.js"</span><span class="code-token-tag">&gt;&lt;/script&gt;</span>
<span class="code-token-tag">&lt;script</span> <span class="code-token-attr">src=</span><span class="code-token-string">"validaciones.js"</span><span class="code-token-tag">&gt;&lt;/script&gt;</span>
<span class="code-token-tag">&lt;script</span> <span class="code-token-attr">src=</span><span class="code-token-string">"aplicacion.js"</span><span class="code-token-tag">&gt;&lt;/script&gt;</span></code></pre>
                        </div>
                        <div class="alert alert-warning border-0 p-2 small mb-0">
                            <strong>Conflicto de nombres:</strong> Si dos archivos definen una función con el mismo nombre, <strong>prevalece siempre la del último script cargado</strong> en el documento HTML.
                        </div>
                    </div>
                </section>

                <!-- SECCIÓN OFICIAL DE EJERCICIOS DEL TEMA 2 (2.6 a 2.10) -->
                <section id="sec-ejercicios" class="card content-card shadow-sm p-4">
                    <div class="d-flex align-items-center justify-content-between flex-wrap gap-2 mb-3">
                        <div class="d-flex align-items-center gap-2">
                            <span class="badge text-bg-warning fs-6"><i class="bi bi-pencil-square"></i></span>
                            <h2 class="h4 mb-0 fw-bold">Boletín Oficial de Ejercicios del Tema 2 (10 Ejercicios)</h2>
                        </div>
                        <a href="07_ejercicios.html" class="btn btn-sm btn-outline-warning text-dark fw-semibold"><i class="bi bi-collection me-1"></i> Catálogo Global</a>
                    </div>
                    <p class="text-secondary small mb-4">
                        Ejercicios del 2.6 al 2.10 planteados en el manual oficial del Tema 2:
                    </p>

                    <div class="row g-3">
                        
                        <!-- Ejercicio 2.6 -->
                        <div class="col-md-6">
                            <div class="card h-100 border exercise-card shadow-sm">
                                <div class="card-header bg-dark text-white d-flex justify-content-between align-items-center py-2">
                                    <span class="fw-bold small">Ejercicio 2.6</span>
                                    <span class="badge text-bg-warning text-dark">06_par_impar_js.html</span>
                                </div>
                                <div class="card-body p-3 d-flex flex-column justify-content-between">
                                    <p class="small text-secondary mb-3">
                                        Función <code>esParImpar(n)</code> que determina si un número entero es par o impar devolviendo <em>"N es par"</em> o <em>"N es impar"</em>.
                                    </p>
                                    <div class="d-flex gap-2">
                                        <a href="../material/ejercicios/aprendizaje/t2_06_par_impar3_1.html" target="_blank" class="btn btn-sm btn-dark flex-grow-1"><i class="bi bi-play me-1"></i> Probar</a>
                                        <a href="07_ejercicios_r.html#ej_2_6" class="btn btn-sm btn-outline-dark"><i class="bi bi-code-slash"></i> Solución</a>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- Ejercicio 2.7 -->
                        <div class="col-md-6">
                            <div class="card h-100 border exercise-card shadow-sm">
                                <div class="card-header bg-dark text-white d-flex justify-content-between align-items-center py-2">
                                    <span class="fw-bold small">Ejercicio 2.7</span>
                                    <span class="badge text-bg-warning text-dark">07_mayus_minus_js.html</span>
                                </div>
                                <div class="card-body p-3 d-flex flex-column justify-content-between">
                                    <p class="small text-secondary mb-3">
                                        Función que analiza una cadena e informa si está formada exclusivamente por mayúsculas, solo por minúsculas o por una mezcla de ambas.
                                    </p>
                                    <div class="d-flex gap-2">
                                        <a href="../material/ejercicios/aprendizaje/t2_07_mayus_minus_js.html" target="_blank" class="btn btn-sm btn-dark flex-grow-1"><i class="bi bi-play me-1"></i> Probar</a>
                                        <a href="07_ejercicios_r.html#ej_2_7" class="btn btn-sm btn-outline-dark"><i class="bi bi-code-slash"></i> Solución</a>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- Ejercicio 2.8 -->
                        <div class="col-md-6">
                            <div class="card h-100 border exercise-card shadow-sm">
                                <div class="card-header bg-dark text-white d-flex justify-content-between align-items-center py-2">
                                    <span class="fw-bold small">Ejercicio 2.8</span>
                                    <span class="badge text-bg-warning text-dark">08_palindromo_js.html</span>
                                </div>
                                <div class="card-body p-3 d-flex flex-column justify-content-between">
                                    <p class="small text-secondary mb-3">
                                        Algoritmo de palíndromos: determina si una palabra o frase se lee exactamente igual de izquierda a derecha prescindiendo de espacios (ej. <em>"ana"</em>).
                                    </p>
                                    <div class="d-flex gap-2">
                                        <a href="../material/ejercicios/aprendizaje/t2_08_palindromo_js.html" target="_blank" class="btn btn-sm btn-dark flex-grow-1"><i class="bi bi-play me-1"></i> Probar</a>
                                        <a href="07_ejercicios_r.html#ej_2_8" class="btn btn-sm btn-outline-dark"><i class="bi bi-code-slash"></i> Solución</a>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- Ejercicio 2.9 -->
                        <div class="col-md-6">
                            <div class="card h-100 border exercise-card shadow-sm">
                                <div class="card-header bg-dark text-white d-flex justify-content-between align-items-center py-2">
                                    <span class="fw-bold small">Ejercicio 2.9</span>
                                    <span class="badge text-bg-warning text-dark">09_tabla_multiplicar_js.html</span>
                                </div>
                                <div class="card-body p-3 d-flex flex-column justify-content-between">
                                    <p class="small text-secondary mb-3">
                                        Pide dos números y un modo de visualización (LISTA o TABLA), generando la tabla de multiplicar desde el primer valor hasta el segundo.
                                    </p>
                                    <div class="d-flex gap-2">
                                        <a href="../material/ejercicios/aprendizaje/t2_09_tabla_multiplicar_js.html" target="_blank" class="btn btn-sm btn-dark flex-grow-1"><i class="bi bi-play me-1"></i> Probar</a>
                                        <a href="07_ejercicios_r.html#ej_2_9" class="btn btn-sm btn-outline-dark"><i class="bi bi-code-slash"></i> Solución</a>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- Ejercicio 2.10 -->
                        <div class="col-md-12">
                            <div class="card h-100 border exercise-card shadow-sm">
                                <div class="card-header bg-dark text-white d-flex justify-content-between align-items-center py-2">
                                    <span class="fw-bold small">Ejercicio 2.10</span>
                                    <span class="badge text-bg-warning text-dark">10_ejercicio_strings_js.html</span>
                                </div>
                                <div class="card-body p-3 d-flex flex-column justify-content-between">
                                    <p class="small text-secondary mb-3">
                                        1) Función <code>pathObtenerCarpetas(path)</code> para desglosar rutas Unix (<code>"./usr/bin/temp"</code>) en Array mediante <code>split('/')</code>.<br>
                                        2) Función <code>reemplazar(texto, patron)</code> case-insensitive para eliminar todas las apariciones de una palabra dada.
                                    </p>
                                    <div class="d-flex gap-2">
                                        <a href="../material/ejercicios/aprendizaje/t2_10_ejercicio_strings_js.html" target="_blank" class="btn btn-sm btn-dark"><i class="bi bi-play me-1"></i> Probar</a>
                                        <a href="07_ejercicios_r.html#ej_2_10" class="btn btn-sm btn-outline-dark"><i class="bi bi-code-slash"></i> Solución</a>
                                    </div>
                                </div>
                            </div>
                        </div>

                    </div>
                </section>

                <!-- Paginación Inferior -->
                <nav class="d-flex justify-content-between align-items-center mt-2 pt-3 border-top" aria-label="Navegación de temas">
                    <a href="01_introduccion.html" class="btn btn-outline-secondary d-flex align-items-center gap-2">
                        <i class="bi bi-arrow-left"></i>
                        <span>Tema 1: Introducción y Sintaxis</span>
                    </a>
                    <a href="03_arrays.html" class="btn btn-warning text-dark fw-bold d-flex align-items-center gap-2">
                        <span>Tema 3: Arrays y Objetos</span>
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
                            <a class="nav-link px-2 py-1 text-secondary text-truncate" href="#sec2-1"><i class="bi bi-chevron-right me-1"></i> 2.1 Definición Funciones</a>
                            <a class="nav-link px-2 py-1 text-secondary text-truncate" href="#sec2-1-1"><i class="bi bi-chevron-right me-1"></i> 2.1.1 Parámetros</a>
                            <a class="nav-link px-2 py-1 text-secondary text-truncate" href="#sec2-1-2"><i class="bi bi-chevron-right me-1"></i> 2.1.2 Parámetros por Defecto</a>
                            <a class="nav-link px-2 py-1 text-secondary text-truncate" href="#sec2-1-3"><i class="bi bi-chevron-right me-1"></i> 2.1.3 Tipo de Retorno</a>
                            <a class="nav-link px-2 py-1 text-secondary text-truncate" href="#sec2-1-4"><i class="bi bi-chevron-right me-1"></i> 2.1.4 Ámbito y use strict</a>
                            <a class="nav-link px-2 py-1 text-secondary text-truncate" href="#sec2-2"><i class="bi bi-chevron-right me-1"></i> 2.2 Strings, Math, Date</a>
                            <a class="nav-link px-2 py-1 text-secondary text-truncate" href="#sec2-3"><i class="bi bi-chevron-right me-1"></i> 2.3 Arrow Functions</a>
                            <a class="nav-link px-2 py-1 text-warning fw-bold text-truncate" href="#sec-ejercicios"><i class="bi bi-pencil-square me-1"></i> Ejercicios 2.1 - 2.10</a>
                        </nav>
                        
                        <div class="border-top mt-3 pt-3">
                            <a href="../material/t2_funciones.pdf" target="_blank" class="btn btn-outline-danger btn-sm w-100 d-flex align-items-center justify-content-center gap-1">
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
    with open("javascript/archivos/02_funciones.html", "w", encoding="utf-8") as f:
        f.write(doc)
    print("02_funciones.html generated successfully! Length:", len(doc))

if __name__ == '__main__':
    generate_t2_page()
