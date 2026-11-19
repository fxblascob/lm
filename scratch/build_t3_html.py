import os

def generate_t3_page():
    doc = """<!DOCTYPE html>
<html lang="es" data-bs-theme="light">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>03. Gestión de Arrays y Datos Complejos | JavaScript | LMSGI</title>
    <meta name="description" content="Tema 3: Creación y manipulación de arrays, referencias en memoria, bucles de recorrido (for, for..in, for..of), métodos mutadores (push, pop, splice), ordenación (sort), iteradores funcionales (map, filter, every, some, forEach) y objetos literales.">
    
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
                <a href="03_arrays.html" class="list-group-item list-group-item-action active bg-warning text-dark border-warning fw-semibold d-flex align-items-center gap-2 py-2"><i class="bi bi-collection text-dark"></i> 03. Arrays y Objetos</a>
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
                <li class="breadcrumb-item active text-dark fw-semibold" aria-current="page">03. Arrays y Objetos</li>
            </ol>
        </nav>

        <!-- Hero Header del Tema -->
        <div class="card bg-warning-subtle border-warning-subtle shadow-sm mb-4">
            <div class="card-body p-4 p-lg-5">
                <div class="d-flex flex-wrap align-items-center gap-2 mb-3">
                    <span class="badge text-bg-warning px-3 py-2 fs-6 fw-bold text-dark"><i class="bi bi-file-earmark-pdf me-1"></i> Manual Oficial: Tema 3</span>
                    <span class="badge bg-dark text-white px-3 py-2 fs-6">Teoría Completa & Ejercicios 3.1 - 3.10</span>
                </div>
                <h1 class="display-5 fw-bold text-dark mb-3">Tema 3: Gestión de Arrays y Datos Complejos</h1>
                <p class="lead text-dark-emphasis mb-4">
                    Estructuras de datos dinámicas en JavaScript: colecciones indexadas (Arrays), paso por referencia en memoria, bucles iterativos (for, for..in, for..of), operaciones mutadoras (push, unshift, pop, shift, splice), ordenación con sort y comparador personalizado, métodos funcionales (map, filter, every, some, forEach) y objetos literales.
                </p>
                
                <!-- Píldoras de Acceso Rápido a Secciones -->
                <div class="d-flex flex-wrap gap-2 pt-2 border-top border-warning-subtle">
                    <a href="#sec3-1" class="btn btn-sm btn-outline-dark bg-white rounded-pill"><i class="bi bi-hash"></i> 3.1 Creación de Arrays</a>
                    <a href="#sec3-1-1" class="btn btn-sm btn-outline-dark bg-white rounded-pill"><i class="bi bi-hash"></i> 3.1.1 Referencias en Memoria</a>
                    <a href="#sec3-2" class="btn btn-sm btn-outline-dark bg-white rounded-pill"><i class="bi bi-hash"></i> 3.2 Recorrido (for, for..of)</a>
                    <a href="#sec3-3" class="btn btn-sm btn-outline-dark bg-white rounded-pill"><i class="bi bi-hash"></i> 3.3 Operaciones con Arrays</a>
                    <a href="#sec3-4" class="btn btn-sm btn-outline-dark bg-white rounded-pill"><i class="bi bi-hash"></i> 3.4 Ordenación (sort)</a>
                    <a href="#sec3-4-1" class="btn btn-sm btn-outline-dark bg-white rounded-pill"><i class="bi bi-hash"></i> 3.4.1 Operaciones Funcionales</a>
                    <a href="#sec3-5" class="btn btn-sm btn-outline-dark bg-white rounded-pill"><i class="bi bi-hash"></i> 3.5 Objetos Literales</a>
                    <a href="#sec-ejercicios" class="btn btn-sm btn-warning text-dark fw-bold rounded-pill"><i class="bi bi-pencil-square"></i> Ejercicios 3.1 a 3.10</a>
                </div>
            </div>
        </div>

        <div class="row g-4">
            
            <!-- Columna Principal de Contenido (9 cols en lg) -->
            <div class="col-lg-9 d-flex flex-column gap-4">

                <!-- 3.1 Manipulación básica de arrays -->
                <section id="sec3-1" class="card content-card shadow-sm p-4">
                    <div class="d-flex align-items-center gap-2 mb-3">
                        <span class="badge text-bg-warning fs-6">3.1</span>
                        <h2 class="h4 mb-0 fw-bold">Manipulación Básica de Arrays en JavaScript</h2>
                    </div>
                    <p>
                        Un <strong>array</strong> es una estructura de datos que permite almacenar múltiples valores bajo un único identificador de variable.
                    </p>
                    <p>
                        En muchos lenguajes (como C o Java clásico), los arrays poseen una longitud fija predeterminada. Sin embargo, en JavaScript <strong>tienen tamaño dinámico</strong> (actúan internamente como vectores o listas dinámicas redimensionables) y pueden contener elementos de <strong>tipos heterogéneos</strong> (números, cadenas, booleanos, objetos e incluso otros arrays combinados):
                    </p>
                    <div class="code-block mb-3">
<pre class="m-0"><code><span class="code-token-comment">// Formas de inicializar un array:</span>
<span class="code-token-keyword">let</span> conjunto1 = [];                          <span class="code-token-comment">// Sintaxis literal recomendada</span>
<span class="code-token-keyword">let</span> conjunto2 = <span class="code-token-keyword">new</span> <span class="code-token-function">Array</span>();                  <span class="code-token-comment">// Constructor genérico</span>
<span class="code-token-keyword">let</span> conjunto3 = <span class="code-token-keyword">new</span> <span class="code-token-function">Array</span>(<span class="code-token-number">10</span>);                <span class="code-token-comment">// Con tamaño inicial de 10 posiciones</span>

<span class="code-token-comment">// Array heterogéneo con valores iniciales:</span>
<span class="code-token-keyword">let</span> mixto = [<span class="code-token-number">10</span>, <span class="code-token-string">"Hola"</span>, <span class="code-token-number">3.5</span>, <span class="code-token-keyword">true</span>];</code></pre>
                    </div>
                    <p>
                        Para acceder o modificar una posición se utiliza la indexación mediante corchetes <code>[posición]</code>, empezando siempre por el índice <code>0</code>:
                    </p>
                    <div class="code-block mb-3">
<pre class="m-0"><code>mixto[<span class="code-token-number">0</span>] = <span class="code-token-number">20</span>;          <span class="code-token-comment">// Modifica el primer elemento</span>
mixto.<span class="code-token-function">push</span>(<span class="code-token-string">"Buenas"</span>);   <span class="code-token-comment">// Añade un nuevo elemento al final del array</span></code></pre>
                    </div>
                    <div class="alert alert-info border-0 shadow-sm p-3 small mb-0">
                        <strong>Posiciones no correlativas y huecos vacíos:</strong> Si asignamos un valor a un índice muy superior (por ejemplo <code>a[10] = "Fin"</code> en un array vacío), JavaScript crea las posiciones intermedias asignándoles el valor <code>undefined</code>.
                    </div>
                </section>

                <!-- 3.1.1 Arrays y referencias -->
                <section id="sec3-1-1" class="card content-card shadow-sm p-4">
                    <div class="d-flex align-items-center gap-2 mb-3">
                        <span class="badge text-bg-warning fs-6">3.1.1</span>
                        <h2 class="h4 mb-0 fw-bold">Arrays y Paso por Referencia en Memoria</h2>
                    </div>
                    <p>
                        Existe una diferencia crucial entre variables primitivas y arrays en cuanto a su asignación en memoria:
                    </p>
                    <div class="row g-3 mb-3">
                        <div class="col-md-6">
                            <div class="p-3 border rounded bg-body-tertiary h-100">
                                <h6 class="fw-bold text-primary mb-1">Copia por Valor (Tipos Simples)</h6>
                                <p class="small text-secondary mb-2">
                                    Al asignar un número o texto a otra variable, se copia su valor de forma independiente:
                                </p>
                                <div class="code-block p-2">
<pre class="m-0"><code><span class="code-token-keyword">let</span> a = <span class="code-token-number">3</span>;
<span class="code-token-keyword">let</span> b = a;
b = <span class="code-token-number">4</span>;
<span class="code-token-function">console</span>.<span class="code-token-function">log</span>(a); <span class="code-token-comment">// Sigue valiendo 3</span></code></pre>
                                </div>
                            </div>
                        </div>
                        <div class="col-md-6">
                            <div class="p-3 border rounded bg-body-tertiary h-100">
                                <h6 class="fw-bold text-danger mb-1">Paso por Referencia (Arrays y Objetos)</h6>
                                <p class="small text-secondary mb-2">
                                    Al asignar un array a otra variable, ambas apuntan a la <strong>misma dirección de memoria</strong>:
                                </p>
                                <div class="code-block p-2">
<pre class="m-0"><code><span class="code-token-keyword">let</span> datos = [<span class="code-token-number">1</span>, <span class="code-token-number">2</span>, <span class="code-token-number">3</span>, <span class="code-token-number">4</span>];
<span class="code-token-keyword">let</span> datos2 = datos; <span class="code-token-comment">// Misma referencia</span>
datos2[<span class="code-token-number">0</span>] = <span class="code-token-number">10</span>;
<span class="code-token-function">console</span>.<span class="code-token-function">log</span>(datos);  <span class="code-token-comment">// [10, 2, 3, 4] ¡Afectado!</span></code></pre>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="alert alert-light border small mb-0">
                        <i class="bi bi-lightbulb me-1"></i> <strong>Clonación real (Shallow Copy):</strong> Para crear una copia independiente de un array y evitar mutaciones no deseadas, podemos usar el operador spread de ES6: <code>let copia = [...datos];</code> o el método <code>datos.slice()</code>.
                    </div>
                </section>

                <!-- 3.2 Recorrido de arrays -->
                <section id="sec3-2" class="card content-card shadow-sm p-4">
                    <div class="d-flex align-items-center gap-2 mb-3">
                        <span class="badge text-bg-warning fs-6">3.2</span>
                        <h2 class="h4 mb-0 fw-bold">Estructuras de Recorrido de Arrays</h2>
                    </div>
                    <p>
                        Para iterar secuencialmente sobre los elementos de un array disponemos de tres sintaxis principales:
                    </p>

                    <div class="row g-3">
                        <div class="col-md-4">
                            <div class="card h-100 border p-3">
                                <h6 class="fw-bold text-dark mb-1">1. Bucle for Clásico</h6>
                                <p class="small text-secondary mb-2">Control total mediante el índice numérico y la propiedad <code>.length</code>:</p>
                                <div class="code-block p-2">
<pre class="m-0"><code><span class="code-token-keyword">for</span> (<span class="code-token-keyword">let</span> i = <span class="code-token-number">0</span>; i &lt; lista.length; i++) {
    <span class="code-token-function">console</span>.<span class="code-token-function">log</span>(lista[i]);
}</code></pre>
                                </div>
                            </div>
                        </div>
                        <div class="col-md-4">
                            <div class="card h-100 border p-3">
                                <h6 class="fw-bold text-dark mb-1">2. Bucle for..in</h6>
                                <p class="small text-secondary mb-2">Itera sobre los <strong>índices o claves</strong> de la colección:</p>
                                <div class="code-block p-2">
<pre class="m-0"><code><span class="code-token-keyword">for</span> (<span class="code-token-keyword">let</span> indice <span class="code-token-keyword">in</span> lista) {
    <span class="code-token-function">console</span>.<span class="code-token-function">log</span>(lista[indice]);
}</code></pre>
                                </div>
                            </div>
                        </div>
                        <div class="col-md-4">
                            <div class="card h-100 border p-3">
                                <h6 class="fw-bold text-primary mb-1">3. Bucle for..of (ES6)</h6>
                                <p class="small text-secondary mb-2">Itera directamente sobre los <strong>valores</strong> (sintaxis más limpia):</p>
                                <div class="code-block p-2">
<pre class="m-0"><code><span class="code-token-keyword">for</span> (<span class="code-token-keyword">let</span> valor <span class="code-token-keyword">of</span> lista) {
    <span class="code-token-function">console</span>.<span class="code-token-function">log</span>(valor);
}</code></pre>
                                </div>
                            </div>
                        </div>
                    </div>
                </section>

                <!-- 3.3 Operaciones con arrays -->
                <section id="sec3-3" class="card content-card shadow-sm p-4">
                    <div class="d-flex align-items-center gap-2 mb-3">
                        <span class="badge text-bg-warning fs-6">3.3</span>
                        <h2 class="h4 mb-0 fw-bold">Operaciones Esenciales y Métodos Mutadores</h2>
                    </div>
                    <p>
                        A continuación se resumen los métodos fundamentales de la API estándar de Array:
                    </p>
                    <div class="table-responsive table-custom mb-4">
                        <table class="table table-hover align-middle mb-0 small">
                            <thead>
                                <tr>
                                    <th>Método</th>
                                    <th>Efecto / Comportamiento</th>
                                    <th>Ejemplo</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td><code>push(...elems)</code></td>
                                    <td>Añade elementos al <strong>final</strong> del array.</td>
                                    <td><code>datos.push(5, 6);</code></td>
                                </tr>
                                <tr>
                                    <td><code>unshift(...elems)</code></td>
                                    <td>Inserta elementos al <strong>principio</strong> desplazando el resto.</td>
                                    <td><code>datos.unshift(0);</code></td>
                                </tr>
                                <tr>
                                    <td><code>pop()</code></td>
                                    <td>Elimina y devuelve el <strong>último</strong> elemento.</td>
                                    <td><code>let ultimo = datos.pop();</code></td>
                                </tr>
                                <tr>
                                    <td><code>shift()</code></td>
                                    <td>Elimina y devuelve el <strong>primer</strong> elemento.</td>
                                    <td><code>let primero = datos.shift();</code></td>
                                </tr>
                                <tr>
                                    <td><code>join(delimitador)</code></td>
                                    <td>Une todos los elementos en un string separados por el delimitador.</td>
                                    <td><code>datos.join(" : "); // "1 : 2 : 3"</code></td>
                                </tr>
                                <tr>
                                    <td><code>concat(array2)</code></td>
                                    <td>Concatena arrays sin mutar los originales devolviendo uno nuevo.</td>
                                    <td><code>let unidos = a1.concat(a2);</code></td>
                                </tr>
                                <tr>
                                    <td><code>slice(inicio, fin)</code></td>
                                    <td>Extrae un subarray sin modificar el original (fin no incluido).</td>
                                    <td><code>datos.slice(1, 3);</code></td>
                                </tr>
                                <tr>
                                    <td><code>splice(pos, cant, ...add)</code></td>
                                    <td><strong>Método navaja suiza:</strong> elimina <code>cant</code> elementos desde <code>pos</code> e inserta nuevos opcionalmente.</td>
                                    <td><code>datos.splice(1, 2, 20, 30);</code></td>
                                </tr>
                                <tr>
                                    <td><code>reverse()</code></td>
                                    <td>Invierte el orden de los elementos in-place.</td>
                                    <td><code>datos.reverse();</code></td>
                                </tr>
                                <tr>
                                    <td><code>indexOf(elem)</code> / <code>includes(elem)</code></td>
                                    <td>Busca el elemento devolviendo su índice (o -1), o un booleano <code>true/false</code>.</td>
                                    <td><code>datos.includes(10);</code></td>
                                </tr>
                            </tbody>
                        </table>
                    </div>

                    <!-- Tarjeta del Ejercicio 3.1 -->
                    <div class="card exercise-card border-warning bg-warning-subtle shadow-sm p-3">
                        <div class="d-flex align-items-center justify-content-between mb-2">
                            <h4 class="h6 fw-bold text-dark mb-0"><i class="bi bi-pencil-square me-1"></i> Ejercicio 3.1: Secuencia Completa de Operaciones con Arrays</h4>
                            <span class="badge bg-warning text-dark border border-dark-subtle">Ejercicio Oficial</span>
                        </div>
                        <p class="small text-dark-emphasis mb-2">
                            En <code>01_arrays_js.html</code>, realizar los siguientes pasos imprimiendo cada estado separado por <code>"=&gt;"</code> con <code>join()</code>:
                        </p>
                        <ol class="small text-dark-emphasis mb-3 ps-3">
                            <li>Crear un array inicial con 4 elementos numéricos.</li>
                            <li>Concatenar 2 elementos al final (<code>push</code>) y 2 al principio (<code>unshift</code>).</li>
                            <li>Eliminar las posiciones de la 3 a la 5 (ambas incluidas) con <code>splice()</code>.</li>
                            <li>Insertar 2 elementos entre el penúltimo y el último mediante <code>splice()</code>.</li>
                            <li>Invertir el array con <code>reverse()</code>.</li>
                        </ol>
                        <div class="d-flex flex-wrap gap-2">
                            <a href="../material/ejercicios/aprendizaje/t3_01_arrays_js.html" target="_blank" class="btn btn-sm btn-dark"><i class="bi bi-play-circle me-1"></i> Probar Solución</a>
                            <a href="07_ejercicios_r.html#ej_3_1" class="btn btn-sm btn-outline-dark"><i class="bi bi-code-slash me-1"></i> Ver Código Resuelto</a>
                        </div>
                    </div>
                </section>

                <!-- 3.4 Ordenación de arrays -->
                <section id="sec3-4" class="card content-card shadow-sm p-4">
                    <div class="d-flex align-items-center gap-2 mb-3">
                        <span class="badge text-bg-warning fs-6">3.4</span>
                        <h2 class="h4 mb-0 fw-bold">Ordenación de Arrays (Método sort)</h2>
                    </div>
                    <p>
                        El método <code>array.sort()</code> ordena los elementos in-place. Por defecto realiza una <strong>ordenación alfabética basada en cadenas UTF-16</strong>:
                    </p>
                    <div class="code-block mb-3">
<pre class="m-0"><code><span class="code-token-keyword">let</span> nombres = [<span class="code-token-string">"Juan"</span>, <span class="code-token-string">"Ana"</span>, <span class="code-token-string">"Laura"</span>, <span class="code-token-string">"Blas"</span>];
nombres.<span class="code-token-function">sort</span>(); <span class="code-token-comment">// ["Ana", "Blas", "Juan", "Laura"]</span>

<span class="code-token-comment">// ¡Atención con números!:</span>
<span class="code-token-keyword">let</span> nums = [<span class="code-token-number">20</span>, <span class="code-token-number">4</span>, <span class="code-token-number">10</span>];
nums.<span class="code-token-function">sort</span>(); <span class="code-token-comment">// [10, 20, 4] ¡Ordena como texto ("10" &lt; "20" &lt; "4")!</span></code></pre>
                    </div>

                    <h4 class="h6 fw-bold text-dark mt-3">Función Comparadora Personalizada</h4>
                    <p class="small">
                        Para ordenar números correctamente o definir criterios complejos, pasamos una función comparadora <code>(a, b)</code> que devuelve:
                    </p>
                    <ul class="small ps-3 mb-3">
                        <li><strong>Valor negativo (&lt; 0):</strong> si <code>a</code> debe situarse antes que <code>b</code>.</li>
                        <li><strong>Valor positivo (&gt; 0):</strong> si <code>a</code> debe situarse después que <code>b</code>.</li>
                        <li><strong>Cero (0):</strong> si ambos valores son equivalentes.</li>
                    </ul>
                    <div class="code-block mb-3">
<pre class="m-0"><code><span class="code-token-keyword">let</span> datos = [<span class="code-token-number">20</span>, <span class="code-token-number">4</span>, <span class="code-token-number">6</span>, <span class="code-token-number">2</span>, <span class="code-token-number">10</span>];

<span class="code-token-comment">// Ordenación numérica ascendente (menor a mayor):</span>
datos.<span class="code-token-function">sort</span>((a, b) =&gt; a - b); <span class="code-token-comment">// [2, 4, 6, 10, 20]</span>

<span class="code-token-comment">// Ordenación numérica descendente (mayor a menor):</span>
datos.<span class="code-token-function">sort</span>((a, b) =&gt; b - a); <span class="code-token-comment">// [20, 10, 6, 4, 2]</span></code></pre>
                    </div>

                    <!-- Tarjeta del Ejercicio 3.2 -->
                    <div class="card exercise-card border-warning bg-warning-subtle shadow-sm p-3">
                        <h4 class="h6 fw-bold text-dark mb-1"><i class="bi bi-pencil-square me-1"></i> Ejercicio 3.2: Ordenación Numérica de Mayor a Menor</h4>
                        <p class="small text-dark-emphasis mb-2">
                            En <code>02_arrays_ordenacion_js.html</code>, definir un array de números desordenados y mostrarlo ordenado de mayor a menor utilizando <code>sort((a,b) =&gt; b - a)</code>.
                        </p>
                        <div class="d-flex gap-2">
                            <a href="../material/ejercicios/aprendizaje/t3_02_arrays_ordenacion_js.html" target="_blank" class="btn btn-sm btn-dark"><i class="bi bi-play me-1"></i> Probar Solución</a>
                            <a href="07_ejercicios_r.html#ej_3_2" class="btn btn-sm btn-outline-dark"><i class="bi bi-code-slash"></i> Solución</a>
                        </div>
                    </div>
                </section>

                <!-- 3.4.1 Operaciones avanzadas (Programación Funcional) -->
                <section id="sec3-4-1" class="card content-card shadow-sm p-4">
                    <div class="d-flex align-items-center gap-2 mb-3">
                        <span class="badge text-bg-warning fs-6">3.4.1</span>
                        <h2 class="h4 mb-0 fw-bold">Operaciones Funcionales Avanzadas</h2>
                    </div>
                    <p>
                        JavaScript incorpora métodos funcionales que reciben funciones callback o lambdas para transformar, filtrar y validar colecciones:
                    </p>
                    <div class="table-responsive table-custom mb-3">
                        <table class="table table-hover align-middle mb-0 small">
                            <thead>
                                <tr>
                                    <th>Método</th>
                                    <th>Propósito</th>
                                    <th>Resultado Devuelto</th>
                                    <th>Ejemplo con Arrow Function</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td><code>every(cb)</code></td>
                                    <td>Comprueba si <strong>todos</strong> los elementos cumplen la condición</td>
                                    <td>Booleano</td>
                                    <td><code>datos.every(n =&gt; n % 2 === 0);</code></td>
                                </tr>
                                <tr>
                                    <td><code>some(cb)</code></td>
                                    <td>Comprueba si <strong>al menos uno</strong> cumple la condición</td>
                                    <td>Booleano</td>
                                    <td><code>datos.some(n =&gt; n &gt; 10);</code></td>
                                </tr>
                                <tr>
                                    <td><code>forEach(cb)</code></td>
                                    <td>Ejecuta una acción sobre cada elemento (recorrido)</td>
                                    <td><code>undefined</code></td>
                                    <td><code>datos.forEach(n =&gt; console.log(n));</code></td>
                                </tr>
                                <tr>
                                    <td><code>filter(cb)</code></td>
                                    <td>Filtra y devuelve los elementos que cumplen el predicado</td>
                                    <td>Nuevo Array</td>
                                    <td><code>let mayores = datos.filter(n =&gt; n &gt; 10);</code></td>
                                </tr>
                                <tr>
                                    <td><code>map(cb)</code></td>
                                    <td>Transforma cada elemento devolviendo una nueva colección</td>
                                    <td>Nuevo Array</td>
                                    <td><code>let dobles = datos.map(n =&gt; n * 2);</code></td>
                                </tr>
                            </tbody>
                        </table>
                    </div>

                    <!-- Tarjetas de Ejercicios 3.3 y 3.4 -->
                    <div class="row g-3">
                        <div class="col-md-6">
                            <div class="card exercise-card border-warning bg-warning-subtle shadow-sm p-3 h-100">
                                <h4 class="h6 fw-bold text-dark mb-1"><i class="bi bi-pencil-square me-1"></i> Ejercicio 3.3: Comprobar Múltiplos con every()</h4>
                                <p class="small text-dark-emphasis mb-2">
                                    En <code>03_funciones_arrays_js.html</code>, función que recibe un array y un número (valor por defecto 2) y determina si todos los elementos son múltiplos de dicho divisor usando <code>every()</code>.
                                </p>
                                <div class="d-flex gap-2 mt-auto">
                                    <a href="../material/ejercicios/aprendizaje/t3_03_funciones_arrays_js.html" target="_blank" class="btn btn-sm btn-dark flex-grow-1"><i class="bi bi-play me-1"></i> Probar</a>
                                    <a href="07_ejercicios_r.html#ej_3_3" class="btn btn-sm btn-outline-dark"><i class="bi bi-code-slash"></i> Solución</a>
                                </div>
                            </div>
                        </div>
                        <div class="col-md-6">
                            <div class="card exercise-card border-warning bg-warning-subtle shadow-sm p-3 h-100">
                                <h4 class="h6 fw-bold text-dark mb-1"><i class="bi bi-pencil-square me-1"></i> Ejercicio 3.4: Encadenamiento filter() y map()</h4>
                                <p class="small text-dark-emphasis mb-2">
                                    En <code>04_funciones_arrays_js.html</code>, a partir de un array numérico con positivos y negativos, filtrar únicamente los positivos y transformarlos para almacenar sus cuadrados con lambdas.
                                </p>
                                <div class="d-flex gap-2 mt-auto">
                                    <a href="../material/ejercicios/aprendizaje/t3_04_funciones_arrays_js.html" target="_blank" class="btn btn-sm btn-dark flex-grow-1"><i class="bi bi-play me-1"></i> Probar</a>
                                    <a href="07_ejercicios_r.html#ej_3_4" class="btn btn-sm btn-outline-dark"><i class="bi bi-code-slash"></i> Solución</a>
                                </div>
                            </div>
                        </div>
                    </div>
                </section>

                <!-- 3.5 Objetos JavaScript -->
                <section id="sec3-5" class="card content-card shadow-sm p-4">
                    <div class="d-flex align-items-center gap-2 mb-3">
                        <span class="badge text-bg-warning fs-6">3.5</span>
                        <h2 class="h4 mb-0 fw-bold">Objetos Literales en JavaScript</h2>
                    </div>
                    <p>
                        Un <strong>objeto literal</strong> agrupa propiedades en formato clave-valor delimitado por llaves <code>{ ... }</code>:
                    </p>
                    <div class="code-block mb-3">
<pre class="m-0"><code><span class="code-token-keyword">let</span> persona = {
    nombre: <span class="code-token-string">"Nacho"</span>,
    edad: <span class="code-token-number">43</span>,
    telefono: <span class="code-token-string">"611223344"</span>
};

<span class="code-token-comment">// Acceso mediante la notación punto:</span>
<span class="code-token-function">console</span>.<span class="code-token-function">log</span>(persona.nombre); <span class="code-token-comment">// "Nacho"</span>

<span class="code-token-comment">// Adición dinámica de propiedades:</span>
persona.direccion = <span class="code-token-string">"C/ Mayor 13"</span>;</code></pre>
                    </div>

                    <h4 class="h6 fw-bold text-dark mt-3">Arrays de Objetos (Estructura Tabular / JSON)</h4>
                    <p class="small">
                        La combinación de arrays y objetos es la base con la que viaja la información estructurada en la web moderna (APIs REST):
                    </p>
                    <div class="code-block mb-3">
<pre class="m-0"><code><span class="code-token-keyword">let</span> personas = [
    { nombre: <span class="code-token-string">"Nacho"</span>,   edad: <span class="code-token-number">43</span>, telefono: <span class="code-token-string">"611223344"</span> },
    { nombre: <span class="code-token-string">"Javier"</span>,  edad: <span class="code-token-number">55</span>, telefono: <span class="code-token-string">"123456789"</span> },
    { nombre: <span class="code-token-string">"Antonio"</span>, edad: <span class="code-token-number">50</span>, telefono: <span class="code-token-string">"123456788"</span> }
];

<span class="code-token-comment">// Ordenación por nombre utilizando localeCompare():</span>
personas.<span class="code-token-function">sort</span>((a, b) =&gt; a.nombre.<span class="code-token-function">localeCompare</span>(b.nombre));</code></pre>
                    </div>
                </section>

                <!-- SECCIÓN OFICIAL DE EJERCICIOS DEL TEMA 3 (3.5 a 3.10) -->
                <section id="sec-ejercicios" class="card content-card shadow-sm p-4">
                    <div class="d-flex align-items-center justify-content-between flex-wrap gap-2 mb-3">
                        <div class="d-flex align-items-center gap-2">
                            <span class="badge text-bg-warning fs-6"><i class="bi bi-pencil-square"></i></span>
                            <h2 class="h4 mb-0 fw-bold">Boletín Oficial de Ejercicios del Tema 3 (10 Ejercicios)</h2>
                        </div>
                        <a href="07_ejercicios.html" class="btn btn-sm btn-outline-warning text-dark fw-semibold"><i class="bi bi-collection me-1"></i> Catálogo Global</a>
                    </div>
                    <p class="text-secondary small mb-4">
                        Ejercicios del 3.5 al 3.10 planteados en el manual oficial del Tema 3:
                    </p>

                    <div class="row g-3">
                        
                        <!-- Ejercicio 3.5 -->
                        <div class="col-md-6">
                            <div class="card h-100 border exercise-card shadow-sm">
                                <div class="card-header bg-dark text-white d-flex justify-content-between align-items-center py-2">
                                    <span class="fw-bold small">Ejercicio 3.5</span>
                                    <span class="badge text-bg-warning text-dark">05_objetos_js.html</span>
                                </div>
                                <div class="card-body p-3 d-flex flex-column justify-content-between">
                                    <p class="small text-secondary mb-3">
                                        Array con datos de personas, ordenación ascendente por nombre mediante <code>localeCompare()</code> y visualización en el documento.
                                    </p>
                                    <div class="d-flex gap-2">
                                        <a href="../material/ejercicios/aprendizaje/t3_05_objetos_js.html" target="_blank" class="btn btn-sm btn-dark flex-grow-1"><i class="bi bi-play me-1"></i> Probar</a>
                                        <a href="07_ejercicios_r.html#ej_3_5" class="btn btn-sm btn-outline-dark"><i class="bi bi-code-slash"></i> Solución</a>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- Ejercicio 3.6 -->
                        <div class="col-md-6">
                            <div class="card h-100 border exercise-card shadow-sm">
                                <div class="card-header bg-dark text-white d-flex justify-content-between align-items-center py-2">
                                    <span class="fw-bold small">Ejercicio 3.6</span>
                                    <span class="badge text-bg-warning text-dark">06_funciones_arrays_js.html</span>
                                </div>
                                <div class="card-body p-3 d-flex flex-column justify-content-between">
                                    <p class="small text-secondary mb-3">
                                        Array de números enteros y función con <code>array.every()</code> que devuelve si todos los elementos son pares.
                                    </p>
                                    <div class="d-flex gap-2">
                                        <a href="../material/ejercicios/aprendizaje/t3_06_funciones_arrays_js.html" target="_blank" class="btn btn-sm btn-dark flex-grow-1"><i class="bi bi-play me-1"></i> Probar</a>
                                        <a href="07_ejercicios_r.html#ej_3_6" class="btn btn-sm btn-outline-dark"><i class="bi bi-code-slash"></i> Solución</a>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- Ejercicio 3.7 -->
                        <div class="col-md-6">
                            <div class="card h-100 border exercise-card shadow-sm">
                                <div class="card-header bg-dark text-white d-flex justify-content-between align-items-center py-2">
                                    <span class="fw-bold small">Ejercicio 3.7</span>
                                    <span class="badge text-bg-warning text-dark">07_arrays_foreach_js.html</span>
                                </div>
                                <div class="card-body p-3 d-flex flex-column justify-content-between">
                                    <p class="small text-secondary mb-3">
                                        Array de nombres de alumnos ordenado alfabéticamente y mostrado numerado en pantalla mediante recorrido con <code>forEach()</code>.
                                    </p>
                                    <div class="d-flex gap-2">
                                        <a href="../material/ejercicios/aprendizaje/t3_07_arrays_foreach_js.html" target="_blank" class="btn btn-sm btn-dark flex-grow-1"><i class="bi bi-play me-1"></i> Probar</a>
                                        <a href="07_ejercicios_r.html#ej_3_7" class="btn btn-sm btn-outline-dark"><i class="bi bi-code-slash"></i> Solución</a>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- Ejercicio 3.8 -->
                        <div class="col-md-6">
                            <div class="card h-100 border exercise-card shadow-sm">
                                <div class="card-header bg-dark text-white d-flex justify-content-between align-items-center py-2">
                                    <span class="fw-bold small">Ejercicio 3.8</span>
                                    <span class="badge text-bg-warning text-dark">08_arrays_filter_js.html</span>
                                </div>
                                <div class="card-body p-3 d-flex flex-column justify-content-between">
                                    <p class="small text-secondary mb-3">
                                        Función que recibe un array numérico y devuelve un nuevo array filtrado que contiene exclusivamente los números pares usando <code>filter()</code>.
                                    </p>
                                    <div class="d-flex gap-2">
                                        <a href="../material/ejercicios/aprendizaje/t3_08_arrays_filter_js.html" target="_blank" class="btn btn-sm btn-dark flex-grow-1"><i class="bi bi-play me-1"></i> Probar</a>
                                        <a href="07_ejercicios_r.html#ej_3_8" class="btn btn-sm btn-outline-dark"><i class="bi bi-code-slash"></i> Solución</a>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- Ejercicio 3.9 -->
                        <div class="col-md-6">
                            <div class="card h-100 border exercise-card shadow-sm">
                                <div class="card-header bg-dark text-white d-flex justify-content-between align-items-center py-2">
                                    <span class="fw-bold small">Ejercicio 3.9</span>
                                    <span class="badge text-bg-warning text-dark">09_arrays_buscar_js.html</span>
                                </div>
                                <div class="card-body p-3 d-flex flex-column justify-content-between">
                                    <p class="small text-secondary mb-3">
                                        Función <code>arrayContieneValor(array, valor)</code> que devuelve la posición del elemento si existe en la colección, o -1 en caso contrario.
                                    </p>
                                    <div class="d-flex gap-2">
                                        <a href="../material/ejercicios/aprendizaje/t3_09_arrays_buscar_js.html" target="_blank" class="btn btn-sm btn-dark flex-grow-1"><i class="bi bi-play me-1"></i> Probar</a>
                                        <a href="07_ejercicios_r.html#ej_3_9" class="btn btn-sm btn-outline-dark"><i class="bi bi-code-slash"></i> Solución</a>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- Ejercicio 3.10 -->
                        <div class="col-md-6">
                            <div class="card h-100 border exercise-card shadow-sm">
                                <div class="card-header bg-dark text-white d-flex justify-content-between align-items-center py-2">
                                    <span class="fw-bold small">Ejercicio 3.10</span>
                                    <span class="badge text-bg-warning text-dark">10_calculoDNI_js.html</span>
                                </div>
                                <div class="card-body p-3 d-flex flex-column justify-content-between">
                                    <p class="small text-secondary mb-3">
                                        Algoritmo oficial del DNI: validar rango numérico, calcular el resto módulo 23 para indexar en el array de letras y contrastar con la letra introducida.
                                    </p>
                                    <div class="d-flex gap-2">
                                        <a href="../material/ejercicios/aprendizaje/t3_10_calculoDNI_js.html" target="_blank" class="btn btn-sm btn-dark flex-grow-1"><i class="bi bi-play me-1"></i> Probar</a>
                                        <a href="07_ejercicios_r.html#ej_3_10" class="btn btn-sm btn-outline-dark"><i class="bi bi-code-slash"></i> Solución</a>
                                    </div>
                                </div>
                            </div>
                        </div>

                    </div>
                </section>

                <!-- Paginación Inferior -->
                <nav class="d-flex justify-content-between align-items-center mt-2 pt-3 border-top" aria-label="Navegación de temas">
                    <a href="02_funciones.html" class="btn btn-outline-secondary d-flex align-items-center gap-2">
                        <i class="bi bi-arrow-left"></i>
                        <span>Tema 2: Funciones y Modularidad</span>
                    </a>
                    <a href="04_dom.html" class="btn btn-warning text-dark fw-bold d-flex align-items-center gap-2">
                        <span>Tema 4: DOM y BOM</span>
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
                            <a class="nav-link px-2 py-1 text-secondary text-truncate" href="#sec3-1"><i class="bi bi-chevron-right me-1"></i> 3.1 Creación Arrays</a>
                            <a class="nav-link px-2 py-1 text-secondary text-truncate" href="#sec3-1-1"><i class="bi bi-chevron-right me-1"></i> 3.1.1 Referencias</a>
                            <a class="nav-link px-2 py-1 text-secondary text-truncate" href="#sec3-2"><i class="bi bi-chevron-right me-1"></i> 3.2 Recorridos</a>
                            <a class="nav-link px-2 py-1 text-secondary text-truncate" href="#sec3-3"><i class="bi bi-chevron-right me-1"></i> 3.3 Operaciones</a>
                            <a class="nav-link px-2 py-1 text-secondary text-truncate" href="#sec3-4"><i class="bi bi-chevron-right me-1"></i> 3.4 Ordenación (sort)</a>
                            <a class="nav-link px-2 py-1 text-secondary text-truncate" href="#sec3-4-1"><i class="bi bi-chevron-right me-1"></i> 3.4.1 Funcionales</a>
                            <a class="nav-link px-2 py-1 text-secondary text-truncate" href="#sec3-5"><i class="bi bi-chevron-right me-1"></i> 3.5 Objetos Literales</a>
                            <a class="nav-link px-2 py-1 text-warning fw-bold text-truncate" href="#sec-ejercicios"><i class="bi bi-pencil-square me-1"></i> Ejercicios 3.1 - 3.10</a>
                        </nav>
                        
                        <div class="border-top mt-3 pt-3">
                            <a href="../material/t3_arrays.pdf" target="_blank" class="btn btn-outline-danger btn-sm w-100 d-flex align-items-center justify-content-center gap-1">
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
    with open("javascript/archivos/03_arrays.html", "w", encoding="utf-8") as f:
        f.write(doc)
    print("03_arrays.html generated successfully! Length:", len(doc))

if __name__ == '__main__':
    generate_t3_page()
