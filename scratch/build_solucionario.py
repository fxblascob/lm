#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generador del Solucionario Interactivo de PHP (10_ejercicios_r.html).
Incorpora los 40 ejercicios resueltos con navegación bidireccional, filtros por tema,
código fuente cargado de php/material/ejercicios/ y explicaciones didácticas.
"""

import os, sys, re, html, glob
from html.parser import HTMLParser

class TagChecker(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.errors = []
        self.void_tags = {'area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr'}
    def handle_starttag(self, tag, attrs):
        if tag.lower() not in self.void_tags:
            self.stack.append((tag.lower(), self.getpos()))
    def handle_endtag(self, tag):
        t = tag.lower()
        if t in self.void_tags: return
        if not self.stack:
            self.errors.append(f"Cierre sin apertura: </{t}> en pos {self.getpos()}")
            return
        last, pos = self.stack.pop()
        if last != t:
            self.errors.append(f"Descuadre en pos {self.getpos()}: esperaba </{last}> (abierto en {pos}) pero llegó </{t}>")

TOPICS = [
    {"num": "00", "title": "00. Primeros pasos con PHP", "file": "00_primeros_pasos.html", "badge": "Tema 00"},
    {"num": "01", "title": "01. Elementos básicos de PHP", "file": "01_elementos_basicos.html", "badge": "Tema 01"},
    {"num": "02", "title": "02. Uso de funciones", "file": "02_funciones.html", "badge": "Tema 02"},
    {"num": "03", "title": "03. Arrays, errores y otros conceptos", "file": "03_arrays.html", "badge": "Tema 03"},
    {"num": "04", "title": "04. Recogida de datos de formularios", "file": "04_formularios.html", "badge": "Tema 04"},
    {"num": "05", "title": "05. Redirecciones e inclusiones", "file": "05_redirecciones.html", "badge": "Tema 05"},
    {"num": "06", "title": "06. Cookies y sesiones", "file": "06_cookies_sesiones.html", "badge": "Tema 06"},
    {"num": "07", "title": "07. Comunicación asíncrona con AJAX", "file": "07_ajax.html", "badge": "Tema 07"},
    {"num": "08", "title": "08. Programación orientada a objetos", "file": "08_poo.html", "badge": "Tema 08"},
    {"num": "09", "title": "09. Acceso a bases de datos", "file": "09_bd.html", "badge": "Tema 09"},
]

def extract_div_content(html_str, start_pos):
    stack = 0
    content_start = html_str.find('>', start_pos) + 1
    for m in re.finditer(r'</?div\b[^>]*>', html_str[start_pos:], re.IGNORECASE):
        tag = m.group(0).lower()
        if tag.startswith('</div'):
            stack -= 1
            if stack == 0:
                end_pos = start_pos + m.start()
                return html_str[content_start:end_pos].strip()
        else:
            stack += 1
    return None

def get_exercise_statements():
    statements = {}
    for f in sorted(glob.glob('php/archivos/0*.html')):
        with open(f, 'r', encoding='utf-8') as fp:
            c = fp.read()
        for m in re.finditer(r'<div id="(ej_\d+_\d+)" class="card exercise-card', c):
            ej_id = m.group(1)
            txt_idx = c.find('class="exercise-text text-dark">', m.start())
            div_start = c.rfind('<div', m.start(), txt_idx + 1)
            statements[ej_id] = extract_div_content(c, div_start)
    return statements

def read_file_safe(path):
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8', errors='replace') as fp:
            return fp.read()
    return f"// Archivo no encontrado: {path}"

def main():
    statements = get_exercise_statements()

    # Mapeo de soluciones completas
    EXERCISES_DATA = [
        # TEMA 00
        {
            "id": "ej_00_1", "tema": "00", "num": 1,
            "title": "Instalación y puesta en marcha del entorno XAMPP",
            "files": [
                {
                    "name": "verificacion_xampp.sh", "lang": "bash",
                    "content": """# 1. Comprobar que los servicios de Apache y MySQL están corriendo en el sistema:
sudo /opt/lampp/lampp status

# O si utilizas los servicios del sistema nativo:
sudo systemctl status apache2
sudo systemctl status mariadb

# 2. Abrir en el navegador para comprobar la pantalla de bienvenida:
# http://localhost/ o http://127.0.0.1/"""
                }
            ],
            "explanation": "El entorno XAMPP empaqueta Apache, MariaDB/MySQL y el intérprete PHP. Una vez iniciado el servidor web, cualquier archivo con extensión <code>.php</code> ubicado dentro de la carpeta raíz pública (<code>htdocs</code>) será procesado por el servidor antes de enviar el resultado en HTML al cliente."
        },
        {
            "id": "ej_00_2", "tema": "00", "num": 2,
            "title": "Verificación del intérprete con phpinfo()",
            "files": [
                {
                    "name": "informacion.php", "lang": "php",
                    "content": """<?php
/**
 * Tema 00 - Ejercicio 2
 * Archivo: htdocs/prueba/informacion.php
 * Muestra la configuración completa del entorno PHP, módulos activos y directivas.
 */
phpinfo();
?>"""
                }
            ],
            "explanation": "La función <code>phpinfo()</code> genera una página completa con información exhaustiva sobre la versión de PHP en ejecución, directivas de configuración de <code>php.ini</code>, extensiones cargadas (PDO, cURL, mbstring) y variables del entorno del servidor web."
        },

        # TEMA 01
        {
            "id": "ej_01_1", "tema": "01", "num": 1,
            "title": "Variables, cálculo de edad y visualización con echo",
            "files": [
                {
                    "name": "01_info_basica.php", "lang": "php",
                    "path": "php/material/ejercicios/01_elementos_basicos/01_info_basica.php"
                }
            ],
            "explanation": "Declara variables con el prefijo <code>$</code>. Calcula la edad restando el año de nacimiento al año actual y concatena cadenas mediante el operador punto <code>.</code> o interpolando directamente dentro de comillas dobles."
        },
        {
            "id": "ej_01_2", "tema": "01", "num": 2,
            "title": "Constantes matemáticas y cálculo del área del círculo",
            "files": [
                {
                    "name": "02_area_circulo.php", "lang": "php",
                    "path": "php/material/ejercicios/01_elementos_basicos/02_area_circulo.php"
                }
            ],
            "explanation": "Para definir constantes globales se utiliza <code>define('PI', 3.14159)</code> o la constante matemática interna <code>M_PI</code> de PHP. La función <code>round($val, 2)</code> o <code>number_format()</code> permite limitar los decimales impresos en pantalla."
        },
        {
            "id": "ej_01_3", "tema": "01", "num": 3,
            "title": "Evaluación de operadores de asignación, comparación y lógicos",
            "files": [
                {
                    "name": "03_echo.php", "lang": "php",
                    "content": """<?php
/**
 * Tema 01 - Ejercicio 3: Evaluación de expresiones lógicas y de asignación
 */
$num1 = 3;
$num2 = 5;
$num3 = 8;
$num1 *= 4; // $num1 pasa a ser 12

echo $num1; // Imprime: 12
echo "<br>";

echo $num1 <= $num2; // 12 <= 5 es falso -> echo de booleano false no muestra nada en pantalla (vacío)
echo "<br>";

echo $num3 > $num1 and $num3 > $num2; // 8 > 12 es falso -> echo false no muestra nada
echo "<br>";

echo $num3 > $num1 or $num3 > $num2; // 8 > 5 es verdadero (true) -> echo true muestra '1'
echo "<br>";

echo $num1 == $num2; // 12 == 5 es falso -> muestra vacío
echo "<br>";

echo $num1 != $num2; // 12 != 5 es verdadero -> muestra '1'
echo "<br>";
?>"""
                }
            ],
            "explanation": "En PHP, cuando se envía un valor booleano a <code>echo</code>, el valor <code>true</code> se convierte en la cadena <code>\"1\"</code>, mientras que <code>false</code> se convierte en una cadena vacía <code>\"\"</code>. Si deseamos inspeccionar tipos y valores exactos en desarrollo se recomienda usar <code>var_dump()</code>."
        },
        {
            "id": "ej_01_4", "tema": "01", "num": 4,
            "title": "Estructura condicional simple if..else para comparar notas",
            "files": [
                {
                    "name": "04_prueba_if.php", "lang": "php",
                    "path": "php/material/ejercicios/01_elementos_basicos/04_prueba_if.php"
                }
            ],
            "explanation": "La estructura de control <code>if..else</code> bifurca el flujo en función de la condición lógica evaluada. Si la condición es verdadera se ejecuta el primer bloque; en caso contrario, el bloque de reserva."
        },
        {
            "id": "ej_01_5", "tema": "01", "num": 5,
            "title": "Bifurcación múltiple if..elseif..else con tres valores",
            "files": [
                {
                    "name": "05_prueba_if.php", "lang": "php",
                    "path": "php/material/ejercicios/01_elementos_basicos/05_prueba_if.php"
                }
            ],
            "explanation": "Con <code>elseif</code> podemos encadenar múltiples condiciones consecutivas. Alternativamente, la función nativa <code>max($nota1, $nota2, $nota3)</code> permite obtener el mayor directamente."
        },
        {
            "id": "ej_01_6", "tema": "01", "num": 6,
            "title": "Bucles for progresivo y regresivo con separadores condicionales",
            "files": [
                {
                    "name": "06_contador.php", "lang": "php",
                    "path": "php/material/ejercicios/01_elementos_basicos/06_contador.php"
                }
            ],
            "explanation": "Demuestra el uso clásico de bucles <code>for ($i = 1; $i <= 100; $i++)</code> y bucles regresivos con decremento <code>$i--</code>. Se incluye una condición para evitar imprimir la coma final al término de la secuencia."
        },
        {
            "id": "ej_01_7", "tema": "01", "num": 7,
            "title": "Intercalación de bloques HTML y código de control PHP",
            "files": [
                {
                    "name": "07_contador_intercalar.php", "lang": "php",
                    "path": "php/material/ejercicios/01_elementos_basicos/07_contador_intercalar.php"
                }
            ],
            "explanation": "PHP permite abrir y cerrar etiquetas <code><?php ... ?></code> dentro de un bucle o condicional, dejando el marcado HTML limpio en el cuerpo sin tener que concatenar gigantescas sentencias <code>echo</code>."
        },

        # TEMA 02
        {
            "id": "ej_02_1", "tema": "02", "num": 1,
            "title": "Definición e invocación de funciones personalizadas",
            "files": [
                {
                    "name": "01_saludo_funciones.php", "lang": "php",
                    "path": "php/material/ejercicios/02_funciones/01_saludo_funciones.php"
                }
            ],
            "explanation": "Encapsular lógica recurrente dentro de funciones <code>function saludo($nombre) { ... }</code> fomenta la reutilización del código y la legibilidad."
        },
        {
            "id": "ej_02_2", "tema": "02", "num": 2,
            "title": "Paso de argumentos para parametrizar un bucle contador",
            "files": [
                {
                    "name": "02_contador_funciones.php", "lang": "php",
                    "path": "php/material/ejercicios/02_funciones/02_contador_funciones.php"
                }
            ],
            "explanation": "La función acepta el valor límite como parámetro formal, permitiendo invocar <code>cuenta(50)</code> o <code>cuenta(10)</code> dinámicamente según sea necesario."
        },
        {
            "id": "ej_02_3", "tema": "02", "num": 3,
            "title": "Paso de parámetros por referencia (&) para modificar variables",
            "files": [
                {
                    "name": "03_intercambia.php", "lang": "php",
                    "path": "php/material/ejercicios/02_funciones/03_intercambia.php"
                }
            ],
            "explanation": "Al anteponer el ampersand <code>&</code> en la declaración de parámetros (<code>function intercambia(&$a, &$b)</code>), la función recibe la dirección de memoria de las variables originales, permitiendo alterar su valor fuera del ámbito de la función."
        },
        {
            "id": "ej_02_4", "tema": "02", "num": 4,
            "title": "Parámetros con valores por defecto (argumentos opcionales)",
            "files": [
                {
                    "name": "04_descuento.php", "lang": "php",
                    "path": "php/material/ejercicios/02_funciones/04_descuento.php"
                }
            ],
            "explanation": "Los parámetros por defecto (<code>function calculaPrecio($precio, $descuento = 0.10)</code>) deben ubicarse siempre a la derecha de los obligatorios. Si el llamador no pasa el segundo argumento, PHP toma automáticamente el valor predeterminado."
        },
        {
            "id": "ej_02_5", "tema": "02", "num": 5,
            "title": "Modularización y reutilización con include y require",
            "files": [
                {
                    "name": "05_funciones_include.inc", "lang": "php",
                    "path": "php/material/ejercicios/02_funciones/05_funciones_include.inc"
                },
                {
                    "name": "05_funciones_include.php", "lang": "php",
                    "path": "php/material/ejercicios/02_funciones/05_funciones_include.php"
                }
            ],
            "explanation": "Separar bibliotecas de funciones en archivos auxiliares (<code>.inc</code> o <code>.php</code>) y cargarlas mediante <code>require_once 'archivo.php'</code> previene la duplicación de código y errores de redefinición de funciones."
        },
        {
            "id": "ej_02_6", "tema": "02", "num": 6,
            "title": "Tratamiento de cadenas de texto (strlen, strtoupper, strpos)",
            "files": [
                {
                    "name": "06_manejo_textos.php", "lang": "php",
                    "path": "php/material/ejercicios/02_funciones/06_manejo_textos.php"
                }
            ],
            "explanation": "PHP ofrece funciones nativas potentes para manipulación de strings: <code>strlen()</code> para longitud, <code>strtoupper()</code> y <code>strtolower()</code> para mayúsculas/minúsculas, <code>strpos()</code> para búsqueda de subcadenas y <code>substr()</code> para extracción."
        },
        {
            "id": "ej_02_7", "tema": "02", "num": 7,
            "title": "Fechas y marcas de tiempo con date() y time()",
            "files": [
                {
                    "name": "07_ahora.php", "lang": "php",
                    "path": "php/material/ejercicios/02_funciones/07_ahora.php"
                }
            ],
            "explanation": "La función <code>date('d/m/Y H:i:s')</code> formatea marcas de tiempo UNIX según los especificadores estándar de PHP. Configurar <code>date_default_timezone_set('Europe/Madrid')</code> asegura que la hora coincida con el huso horario local."
        },
        {
            "id": "ej_02_8", "tema": "02", "num": 8,
            "title": "Validación de formatos y rangos horarios",
            "files": [
                {
                    "name": "08_comprueba_hora.php", "lang": "php",
                    "path": "php/material/ejercicios/02_funciones/08_comprueba_hora.php"
                }
            ],
            "explanation": "Valida que los valores de hora, minuto y segundo se encuentren dentro de los rangos válidos (0..23 para horas, 0..59 para minutos/segundos) mediante operadores lógicos o expresiones regulares con <code>preg_match()</code>."
        },
        {
            "id": "ej_02_9", "tema": "02", "num": 9,
            "title": "Manejo de archivos del sistema: lectura y copias de seguridad",
            "files": [
                {
                    "name": "09_CopiaSeguridad.php", "lang": "php",
                    "path": "php/material/ejercicios/02_funciones/09_CopiaSeguridad.php"
                },
                {
                    "name": "datos.txt", "lang": "plaintext",
                    "path": "php/material/ejercicios/02_funciones/datos.txt"
                }
            ],
            "explanation": "Operaciones básicas con el sistema de ficheros: <code>file_exists()</code> para verificar existencia, <code>copy()</code> para duplicar ficheros o <code>fopen()</code>, <code>fread()</code>, <code>fwrite()</code> y <code>fclose()</code> para lectura y escritura de bajo nivel."
        },

        # TEMA 03
        {
            "id": "ej_03_1", "tema": "03", "num": 1,
            "title": "Generación dinámica de tablas de multiplicar con arrays",
            "files": [
                {
                    "name": "01_TablaMultiplicar.php", "lang": "php",
                    "path": "php/material/ejercicios/03_arrays/01_TablaMultiplicar.php"
                }
            ],
            "explanation": "Uso de arrays indexados numéricamente para almacenar resultados y generación de una tabla HTML estructurada con <code>&lt;table class=\"table\"&gt;</code>."
        },
        {
            "id": "ej_03_2", "tema": "03", "num": 2,
            "title": "Matrices asociativas y bidimensionales de datos",
            "files": [
                {
                    "name": "02_Coches.php", "lang": "php",
                    "path": "php/material/ejercicios/03_arrays/02_Coches.php"
                }
            ],
            "explanation": "Estructuración de datos tabulares mediante arrays multidimensionales donde cada elemento es un array asociativo con claves semánticas (<code>'marca'</code>, <code>'modelo'</code>, <code>'precio'</code>), iterados mediante bucles <code>foreach</code>."
        },
        {
            "id": "ej_03_3", "tema": "03", "num": 3,
            "title": "Control de errores: operador @, die() y excepciones try..catch",
            "files": [
                {
                    "name": "03_CopiaSeguridad_die.php", "lang": "php",
                    "path": "php/material/ejercicios/03_arrays/03_CopiaSeguridad_die.php"
                },
                {
                    "name": "03_CopiaSeguridad_arroba.php", "lang": "php",
                    "path": "php/material/ejercicios/03_arrays/03_CopiaSeguridad_arroba.php"
                },
                {
                    "name": "03_CopiaSeguridad_excepciones.php", "lang": "php",
                    "path": "php/material/ejercicios/03_arrays/03_CopiaSeguridad_excepciones.php"
                }
            ],
            "explanation": "Comparativa de las tres aproximaciones de control de fallos en PHP: el operador de supresión <code>@</code> (desaconsejado en PHP moderno), corte inmediato con <code>or die()</code>, y el manejo profesional mediante bloques <code>try { ... } catch (Exception $e) { ... }</code>."
        },
        {
            "id": "ej_03_4", "tema": "03", "num": 4,
            "title": "Estructura compleja de Currículum con array multidimensional",
            "files": [
                {
                    "name": "04_curriculum.php", "lang": "php",
                    "path": "php/material/ejercicios/03_arrays/04_curriculum.php"
                }
            ],
            "explanation": "Diseño de una ficha de presentación curricular renderizada a partir de un array con sub-arrays de formación, experiencia laboral y competencias técnicas, recorridos anidadamente mediante bucles <code>foreach ($datos as $clave => $seccion)</code>."
        },

        # TEMA 04
        {
            "id": "ej_04_1", "tema": "04", "num": 1,
            "title": "Formulario de búsqueda de libros y recepción por método GET/POST",
            "files": [
                {
                    "name": "form_libros.php", "lang": "php",
                    "path": "php/material/ejercicios/04_formularios/01_libros/form_libros.php"
                },
                {
                    "name": "result_libros.php", "lang": "php",
                    "path": "php/material/ejercicios/04_formularios/01_libros/result_libros.php"
                }
            ],
            "explanation": "El formulario HTML envía los campos hacia la página de procesamiento mediante la variable superglobal <code>$_POST</code> o <code>$_GET</code>. Se debe utilizar <code>htmlspecialchars()</code> para neutralizar caracteres especiales e impedir vulnerabilidades XSS."
        },
        {
            "id": "ej_04_2", "tema": "04", "num": 2,
            "title": "Cálculo de presupuestos de departamentos con campos select",
            "files": [
                {
                    "name": "form_dep.php", "lang": "php",
                    "path": "php/material/ejercicios/04_formularios/02_departamentos/form_dep.php"
                },
                {
                    "name": "presupuesto.php", "lang": "php",
                    "path": "php/material/ejercicios/04_formularios/02_departamentos/presupuesto.php"
                }
            ],
            "explanation": "Procesamiento de menús desplegables <code>&lt;select&gt;</code> e inputs numéricos. El script de destino valida que los valores recibidos existan y realiza cálculos aritméticos condicionales antes de presentar el presupuesto final."
        },
        {
            "id": "ej_04_3", "tema": "04", "num": 3,
            "title": "Formulario de departamentos con casillas checkbox múltiples",
            "files": [
                {
                    "name": "form_dept2.php", "lang": "php",
                    "path": "php/material/ejercicios/04_formularios/03_form_dept2/form_dept2.php"
                },
                {
                    "name": "presupuesto.php", "lang": "php",
                    "path": "php/material/ejercicios/04_formularios/03_form_dept2/presupuesto.php"
                }
            ],
            "explanation": "Al nombrar los checkboxes con corchetes en HTML (<code>name=\"servicios[]\"</code>), PHP recopila automáticamente todas las casillas marcadas por el usuario en forma de array en <code>$_POST['servicios']</code>."
        },
        {
            "id": "ej_04_4", "tema": "04", "num": 4,
            "title": "Formulario autónomo unificado (auto-procesamiento en la misma página)",
            "files": [
                {
                    "name": "04presupuesto2.php", "lang": "php",
                    "path": "php/material/ejercicios/04_formularios/04_presupuesto/04presupuesto2.php"
                }
            ],
            "explanation": "Patrón clásico de auto-procesamiento donde la página detecta si ha recibido un envío mediante <code>if ($_SERVER['REQUEST_METHOD'] === 'POST')</code> o <code>isset($_POST['enviar'])</code>. Si no se ha enviado, muestra el formulario vacío; si ya se envió, valida los datos y muestra los errores o resultados en la misma vista."
        },
        {
            "id": "ej_04_5", "tema": "04", "num": 5,
            "title": "Subida de archivos y ficheros multimedia con $_FILES",
            "files": [
                {
                    "name": "form_imagen.php", "lang": "php",
                    "path": "php/material/ejercicios/04_formularios/05_ficheros/form_imagen.php"
                },
                {
                    "name": "subir_imagen.php", "lang": "php",
                    "path": "php/material/ejercicios/04_formularios/05_ficheros/subir_imagen.php"
                }
            ],
            "explanation": "El formulario requiere obligatoriamente el atributo <code>enctype=\"multipart/form-data\"</code>. El servidor recibe los metadatos en <code>$_FILES['foto']</code> y tras validar el tamaño, tipo MIME y posibles errores, traslada el archivo temporal a su destino definitivo con <code>move_uploaded_file()</code>."
        },

        # TEMA 05
        {
            "id": "ej_05_1", "tema": "05", "num": 1,
            "title": "Redirección HTTP con cabecera header('Location: ...')",
            "files": [
                {
                    "name": "form_libros.php", "lang": "php",
                    "path": "php/material/ejercicios/05_redirecciones/01_libros/form_libros.php"
                },
                {
                    "name": "result_libros.php", "lang": "php",
                    "path": "php/material/ejercicios/05_redirecciones/01_libros/result_libros.php"
                }
            ],
            "explanation": "Si un formulario recibe campos vacíos o peticiones no autorizadas, se envía una cabecera de redirección <code>header('Location: form_libros.php?error=1')</code> seguida inmediatamente de <code>exit;</code> para impedir que se continúe procesando el script."
        },
        {
            "id": "ej_05_2", "tema": "05", "num": 2,
            "title": "Plantillas modulares con cabeceras y fragmentos reutilizables",
            "files": [
                {
                    "name": "cabecera.inc", "lang": "php",
                    "path": "php/material/ejercicios/05_redirecciones/02_libros/cabecera.inc"
                },
                {
                    "name": "form_libros.php", "lang": "php",
                    "path": "php/material/ejercicios/05_redirecciones/02_libros/form_libros.php"
                },
                {
                    "name": "result_libros.php", "lang": "php",
                    "path": "php/material/ejercicios/05_redirecciones/02_libros/result_libros.php"
                }
            ],
            "explanation": "Estructurar la aplicación web separando la barra de navegación, la cabecera HTML y los estilos en archivos comunes incluidos con <code>include 'cabecera.inc'</code> garantiza un diseño uniforme en todas las pantallas."
        },
        {
            "id": "ej_05_3", "tema": "05", "num": 3,
            "title": "Flujo completo de validación, subida de imágenes y manejo de errores",
            "files": [
                {
                    "name": "cabecera.inc", "lang": "php",
                    "path": "php/material/ejercicios/05_redirecciones/03_formularios/cabecera.inc"
                },
                {
                    "name": "formulario.php", "lang": "php",
                    "path": "php/material/ejercicios/05_redirecciones/03_formularios/formulario.php"
                },
                {
                    "name": "error.php", "lang": "php",
                    "path": "php/material/ejercicios/05_redirecciones/03_formularios/error.php"
                },
                {
                    "name": "pie.inc", "lang": "php",
                    "path": "php/material/ejercicios/05_redirecciones/03_formularios/pie.inc"
                }
            ],
            "explanation": "Arquitectura modular completa de un formulario con verificación de campos de texto, renombrado aleatorio o temporal de imágenes con <code>time()</code> para evitar colisiones y redirección a una vista de error descriptiva ante cualquier fallo."
        },

        # TEMA 06
        {
            "id": "ej_06_1", "tema": "06", "num": 1,
            "title": "Gestión de preferencias del usuario mediante Cookies del navegador",
            "files": [
                {
                    "name": "index.php", "lang": "php",
                    "path": "php/material/ejercicios/06_cookies_sesiones/01_preferencias/index.php"
                },
                {
                    "name": "preferencias.php", "lang": "php",
                    "path": "php/material/ejercicios/06_cookies_sesiones/01_preferencias/preferencias.php"
                },
                {
                    "name": "guarda_prefs.php", "lang": "php",
                    "path": "php/material/ejercicios/06_cookies_sesiones/01_preferencias/guarda_prefs.php"
                },
                {
                    "name": "borrar_prefs.php", "lang": "php",
                    "path": "php/material/ejercicios/06_cookies_sesiones/01_preferencias/borrar_prefs.php"
                }
            ],
            "explanation": "Uso de <code>setcookie('nombre', $valor, time() + 3600*24*30)</code> para persistir preferencias (idioma, tema de color) en el cliente. Para eliminar una cookie se invoca <code>setcookie()</code> con una fecha de caducidad en el pasado (<code>time() - 3600</code>)."
        },
        {
            "id": "ej_06_2", "tema": "06", "num": 2,
            "title": "Implementación de un Carrito de la Compra en Sesión con $_SESSION",
            "files": [
                {
                    "name": "carro.php", "lang": "php",
                    "path": "php/material/ejercicios/06_cookies_sesiones/02_carro/carro.php"
                }
            ],
            "explanation": "Toda página que interactúe con sesiones debe iniciar con <code>session_start()</code> antes de producir ninguna salida HTML. El array asociativo <code>$_SESSION['carrito']</code> conserva los artículos añadidos a lo largo de la navegación del usuario."
        },
        {
            "id": "ej_06_3", "tema": "06", "num": 3,
            "title": "Sistema de Autenticación de Usuarios y Control de Acceso",
            "files": [
                {
                    "name": "cabecera.inc", "lang": "php",
                    "path": "php/material/ejercicios/06_cookies_sesiones/03_login/cabecera.inc"
                },
                {
                    "name": "login.php", "lang": "php",
                    "path": "php/material/ejercicios/06_cookies_sesiones/03_login/login.php"
                },
                {
                    "name": "index.php", "lang": "php",
                    "path": "php/material/ejercicios/06_cookies_sesiones/03_login/index.php"
                },
                {
                    "name": "pag1.php", "lang": "php",
                    "path": "php/material/ejercicios/06_cookies_sesiones/03_login/pag1.php"
                },
                {
                    "name": "pag2.php", "lang": "php",
                    "path": "php/material/ejercicios/06_cookies_sesiones/03_login/pag2.php"
                }
            ],
            "explanation": "El usuario envía sus credenciales; tras comprobar la coincidencia, se almacena su identidad en <code>$_SESSION['usuario'] = $usuario</code>. Las páginas protegidas verifican <code>if (!isset($_SESSION['usuario'])) { header('Location: login.php'); exit; }</code>. El cierre de sesión se ejecuta con <code>session_destroy()</code>."
        },

        # TEMA 07
        {
            "id": "ej_07_1", "tema": "07", "num": 1,
            "title": "Peticiones asíncronas con AJAX y XMLHttpRequest en texto plano",
            "files": [
                {
                    "name": "listacompra.html", "lang": "html",
                    "path": "php/material/ejercicios/07_Ajax_comunicacion_asincrona/01_listacompra/listacompra.html"
                },
                {
                    "name": "listado.php", "lang": "php",
                    "path": "php/material/ejercicios/07_Ajax_comunicacion_asincrona/01_listacompra/listado.php"
                },
                {
                    "name": "listado.txt", "lang": "plaintext",
                    "path": "php/material/ejercicios/07_Ajax_comunicacion_asincrona/01_listacompra/listado.txt"
                }
            ],
            "explanation": "El navegador utiliza el objeto JavaScript <code>XMLHttpRequest</code> (o la moderna API <code>fetch()</code>) para solicitar un recurso backend sin recargar la página y actualiza dinámicamente el DOM con la respuesta recibida."
        },
        {
            "id": "ej_07_2", "tema": "07", "num": 2,
            "title": "Intercambio de datos asíncronos en formato JSON",
            "files": [
                {
                    "name": "listacompra.html", "lang": "html",
                    "path": "php/material/ejercicios/07_Ajax_comunicacion_asincrona/02_listacompraJson/listacompra.html"
                },
                {
                    "name": "listado.php", "lang": "php",
                    "path": "php/material/ejercicios/07_Ajax_comunicacion_asincrona/02_listacompraJson/listado.php"
                }
            ],
            "explanation": "El backend en PHP serializa estructuras de datos con <code>echo json_encode($datos);</code> y la cabecera <code>header('Content-Type: application/json');</code>. El cliente frontend parsea el resultado con <code>JSON.parse()</code> o <code>response.json()</code> para crear elementos HTML de forma segura."
        },
        {
            "id": "ej_07_3", "tema": "07", "num": 3,
            "title": "Envío y actualización asíncrona mediante formularios AJAX",
            "files": [
                {
                    "name": "lista_compra.html", "lang": "html",
                    "path": "php/material/ejercicios/07_Ajax_comunicacion_asincrona/03_listacompraJSONForm/lista_compra.html"
                },
                {
                    "name": "listado.php", "lang": "php",
                    "path": "php/material/ejercicios/07_Ajax_comunicacion_asincrona/03_listacompraJSONForm/listado.php"
                },
                {
                    "name": "nuevo.php", "lang": "php",
                    "path": "php/material/ejercicios/07_Ajax_comunicacion_asincrona/03_listacompraJSONForm/nuevo.php"
                }
            ],
            "explanation": "El cliente intercepta el evento <code>submit</code> del formulario con <code>e.preventDefault()</code>, empaqueta los campos con <code>FormData</code> y envía una petición POST asíncrona hacia <code>nuevo.php</code>, recargando a continuación la lista sin pestañeo."
        },

        # TEMA 08
        {
            "id": "ej_08_1", "tema": "08", "num": 1,
            "title": "Modelado de Clases, Herencia y Encapsulamiento en PHP (POO)",
            "files": [
                {
                    "name": "clases.php", "lang": "php",
                    "path": "php/material/ejercicios/08_poo/clases.php"
                }
            ],
            "explanation": "Demostración de los principios de Programación Orientada a Objetos: clase base <code>Persona</code> con atributos privados/protegidos, método constructor <code>__construct()</code>, métodos accesores (getters y setters), y clase derivada <code>Empleado</code> que extiende a la clase padre con <code>extends</code> e invoca a <code>parent::__construct()</code>."
        },

        # TEMA 09
        {
            "id": "ej_09_1", "tema": "09", "num": 1,
            "title": "Conexión a Base de Datos MySQL con PDO y ejecución de SELECT",
            "files": [
                {
                    "name": "prueba.php", "lang": "php",
                    "path": "php/material/ejercicios/09_bd/prueba.php"
                }
            ],
            "explanation": "PHP Data Objects (PDO) es la interfaz estándar para interactuar con bases de datos relacionales. Permite definir el DSN de conexión (<code>mysql:host=localhost;dbname=academia;charset=utf8mb4</code>), configurar el modo de excepciones con <code>ATTR_ERRMODE => ERRMODE_EXCEPTION</code> y recuperar filas como objetos o arrays asociativos."
        },
        {
            "id": "ej_09_2", "tema": "09", "num": 2,
            "title": "CRUD de Videojuegos con Inserción y Formularios vinculados a BD",
            "files": [
                {
                    "name": "cabecera.php", "lang": "php",
                    "path": "php/material/ejercicios/09_bd/02_bd_videojuegos/cabecera.php"
                },
                {
                    "name": "index.php", "lang": "php",
                    "path": "php/material/ejercicios/09_bd/02_bd_videojuegos/index.php"
                },
                {
                    "name": "form_videojuego.php", "lang": "php",
                    "path": "php/material/ejercicios/09_bd/02_bd_videojuegos/form_videojuego.php"
                },
                {
                    "name": "insertar_videojuego.php", "lang": "php",
                    "path": "php/material/ejercicios/09_bd/02_bd_videojuegos/insertar_videojuego.php"
                }
            ],
            "explanation": "Aplicación web conectada a MySQL con listado general de registros y formulario de alta que valida los datos antes de ejecutar sentencias <code>INSERT INTO</code>."
        },
        {
            "id": "ej_09_3", "tema": "09", "num": 3,
            "title": "Consultas Preparadas con Parámetros Ligados (Prevenir Inyección SQL)",
            "files": [
                {
                    "name": "insertar_videojuego.php", "lang": "php",
                    "path": "php/material/ejercicios/09_bd/03_bd_videojuegos/insertar_videojuego.php"
                },
                {
                    "name": "form_videojuego.php", "lang": "php",
                    "path": "php/material/ejercicios/09_bd/03_bd_videojuegos/form_videojuego.php"
                },
                {
                    "name": "index.php", "lang": "php",
                    "path": "php/material/ejercicios/09_bd/03_bd_videojuegos/index.php"
                },
                {
                    "name": "academia.sql", "lang": "sql",
                    "path": "php/material/ficheros/academia.sql"
                }
            ],
            "explanation": "Regla esencial de ciberseguridad: NUNCA concatenar variables del usuario directamente dentro de consultas SQL. Se utiliza <code>$stmt = $pdo->prepare('INSERT INTO ... VALUES (:titulo, :precio)');</code> y <code>$stmt->execute([':titulo' => $titulo, ...])</code> para que el motor de BD trate los parámetros estrictamente como datos, neutralizando ataques de inyección SQL."
        }
    ]

    # Cargar contenido de archivos
    for item in EXERCISES_DATA:
        for f in item["files"]:
            if "path" in f:
                f["content"] = read_file_safe(f["path"])

    # Generar bloques HTML para cada ejercicio
    cards_html = []
    for item in EXERCISES_DATA:
        ej_id = item["id"]
        tema_num = item["tema"]
        topic_info = next((t for t in TOPICS if t["num"] == tema_num), None)
        topic_title = topic_info["title"] if topic_info else f"Tema {tema_num}"
        topic_file = topic_info["file"] if topic_info else "00_primeros_pasos.html"
        statement_text = statements.get(ej_id, f"<p>Consulta el enunciado en la lección teórica {topic_title}.</p>")

        # Bloques de archivos
        files_tabs = []
        files_content = []
        for f_idx, f in enumerate(item["files"]):
            f_id = f"{ej_id}_file_{f_idx}"
            active_cls = "active" if f_idx == 0 else ""
            show_cls = "show active" if f_idx == 0 else ""
            lang = f.get("lang", "php")
            lang_icon = "bi-filetype-php" if lang == "php" else ("bi-database" if lang == "sql" else ("bi-filetype-html" if lang == "html" else "bi-terminal"))

            # Tab button si hay más de 1 archivo
            if len(item["files"]) > 1:
                files_tabs.append(f"""<li class="nav-item" role="presentation">
    <button class="nav-link {active_cls} py-1 px-3 small" id="{f_id}-tab" data-bs-toggle="tab" data-bs-target="#{f_id}-pane" type="button" role="tab" aria-controls="{f_id}-pane" aria-selected="{'true' if f_idx == 0 else 'false'}">
        <i class="bi {lang_icon} me-1"></i>{f['name']}
    </button>
</li>""")

            raw_code = f.get("content", "")
            escaped_code = html.escape(raw_code.strip())

            files_content.append(f"""<div class="tab-pane fade {show_cls}" id="{f_id}-pane" role="tabpanel" aria-labelledby="{f_id}-tab" tabindex="0">
    <div class="code-block position-relative bg-dark rounded-3 p-3 text-light">
        <div class="d-flex justify-content-between align-items-center pb-2 mb-2 border-bottom border-secondary border-opacity-25 small text-secondary">
            <span class="text-info font-monospace fw-semibold"><i class="bi {lang_icon} me-1"></i>{f['name']}</span>
            <button class="btn btn-sm btn-outline-secondary py-0 px-2 text-light" style="font-size: 0.75rem;" onclick="navigator.clipboard.writeText(this.closest('.code-block').querySelector('code').innerText)"><i class="bi bi-clipboard"></i> Copiar</button>
        </div>
        <pre class="m-0 font-monospace small" style="overflow-x: auto; max-height: 480px;"><code>{escaped_code}</code></pre>
    </div>
</div>""")

        tabs_header = ""
        if len(item["files"]) > 1:
            tabs_header = f"""<ul class="nav nav-tabs nav-tabs-sm mb-2" id="{ej_id}-tabs" role="tablist">
{''.join(files_tabs)}
</ul>"""

        card_code = f"""<!-- Ejercicio {ej_id} -->
<article class="card exercise-card mb-5 border-0 shadow-sm rounded-3 overflow-hidden" id="{ej_id}" data-category="tema{tema_num}">
    <div class="card-header bg-white border-bottom py-3 px-4 d-flex justify-content-between align-items-center flex-wrap gap-2">
        <div class="d-flex align-items-center gap-2">
            <span class="badge bg-info text-dark fw-bold px-3 py-2 fs-6">Tema {tema_num} &bull; Ejercicio {item['num']}</span>
            <h2 class="h5 fw-bold mb-0 text-dark">{item['title']}</h2>
        </div>
        <div class="d-flex align-items-center gap-2">
            <a href="{topic_file}#{ej_id}" class="btn btn-sm btn-outline-primary d-flex align-items-center gap-1" title="Ir al contenido teórico">
                <i class="bi bi-book"></i>
                <span class="d-none d-sm-inline">Ver en Teoría</span>
            </a>
            <a href="#inicio" class="btn btn-sm btn-light border" title="Volver arriba">
                <i class="bi bi-chevron-up"></i>
            </a>
        </div>
    </div>
    <div class="card-body p-4">
        <!-- Enunciado -->
        <div class="alert alert-light border rounded-3 p-3 mb-4">
            <h6 class="fw-bold text-secondary text-uppercase small mb-2 d-flex align-items-center gap-2">
                <i class="bi bi-question-circle text-info"></i> Enunciado de la Actividad
            </h6>
            <div class="exercise-text mb-0">
                {statement_text}
            </div>
        </div>

        <!-- Archivos de la Solución -->
        <div class="mb-4">
            <h6 class="fw-bold text-dark mb-2 d-flex align-items-center gap-2">
                <i class="bi bi-check2-circle text-success"></i> Solución Implementada
            </h6>
            {tabs_header}
            <div class="tab-content" id="{ej_id}-tabContent">
                {''.join(files_content)}
            </div>
        </div>

        <!-- Explicación Didáctica -->
        <div class="p-3 bg-body-tertiary rounded-3 border-start border-4 border-success">
            <h6 class="fw-bold text-success mb-1 d-flex align-items-center gap-2">
                <i class="bi bi-lightbulb"></i> Explicación Didáctica y Buenas Prácticas
            </h6>
            <p class="small text-secondary mb-0">{item['explanation']}</p>
        </div>
    </div>
</article>"""
        cards_html.append(card_code)

    all_cards_str = "\n".join(cards_html)

    # Menú Offcanvas
    offcanvas_items = []
    for t in TOPICS:
        offcanvas_items.append(f"""<a href="{t['file']}" class="list-group-item list-group-item-action bg-dark text-white-50 border-secondary d-flex align-items-center gap-2 py-2">
    <i class="bi bi-chevron-right text-info"></i>
    <span class="small">{t['title']}</span>
</a>""")
    offcanvas_items.append(f"""<a href="10_ejercicios_r.html" class="list-group-item list-group-item-action active bg-info text-dark border-info d-flex align-items-center gap-2 py-2 fw-semibold">
    <i class="bi bi-check2-circle"></i>
    <span class="small">10. Solucionario de Ejercicios</span>
</a>""")
    offcanvas_links_str = "\n".join(offcanvas_items)

    full_html = f"""<!DOCTYPE html>
<html lang="es" data-bs-theme="light">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>10. Solucionario Completo de PHP (40 Ejercicios) | LMSGI</title>
    <meta name="description" content="Solucionario oficial de los 40 ejercicios prácticos del temario de PHP: código fuente completo, explicaciones didácticas y buenas prácticas de desarrollo web backend.">
    
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
        .exercise-card {{
            transition: transform 0.15s ease, box-shadow 0.15s ease;
        }}
        .exercise-card:hover {{
            box-shadow: 0 0.5rem 1.25rem rgba(0, 0, 0, 0.08) !important;
        }}
        .filter-btn.active {{
            background-color: #0dcaf0;
            color: #000;
            border-color: #0dcaf0;
            font-weight: 600;
        }}
        .sticky-summary {{
            position: sticky;
            top: 5rem;
            max-height: calc(100vh - 6rem);
            overflow-y: auto;
        }}
    </style>
</head>
<body id="inicio">

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
                <a class="btn btn-sm btn-dark text-light-emphasis" href="../../javascript/index.html">JavaScript</a>
                <a class="btn btn-sm btn-info text-dark fw-medium" href="../index.html">PHP</a>
            </nav>

            <!-- Botón Rápido de Retorno -->
            <a href="../index.html" class="btn btn-sm btn-outline-warning d-flex align-items-center gap-1">
                <i class="bi bi-house-door"></i>
                <span class="d-none d-sm-inline">Portada PHP</span>
            </a>
        </div>
    </header>

    <!-- 2. Menú Lateral Offcanvas -->
    <div class="offcanvas offcanvas-start text-bg-dark" tabindex="-1" id="offcanvasNav" aria-labelledby="offcanvasNavLabel">
        <div class="offcanvas-header border-bottom border-secondary">
            <h5 class="offcanvas-title d-flex align-items-center gap-2" id="offcanvasNavLabel">
                <i class="bi bi-filetype-php text-info"></i> Temario PHP
            </h5>
            <button type="button" class="btn-close btn-close-white" data-bs-dismiss="offcanvas" aria-label="Cerrar"></button>
        </div>
        <div class="offcanvas-body p-3">
            <h6 class="text-uppercase text-secondary small fw-bold mb-2">Unidades Didácticas</h6>
            <div class="list-group list-group-flush mb-4">
                {offcanvas_links_str}
            </div>

            <div class="p-3 bg-secondary bg-opacity-25 rounded-3 border border-secondary border-opacity-50">
                <h6 class="fw-bold text-white mb-2 small"><i class="bi bi-info-circle text-info me-1"></i>Sobre el Solucionario</h6>
                <p class="small text-secondary mb-0">Contiene los 40 ejercicios resueltos y comentados de todos los temas con código compatible con PHP 8.x.</p>
            </div>
        </div>
    </div>

    <!-- 3. Cabecera de la Lección -->
    <header class="bg-dark text-white py-4 py-md-5 border-bottom border-secondary">
        <div class="container-xl">
            <!-- Breadcrumbs -->
            <nav aria-label="breadcrumb" class="mb-3">
                <ol class="breadcrumb breadcrumb-dark mb-0 small">
                    <li class="breadcrumb-item"><a href="../../index.html" class="text-secondary text-decoration-none">Inicio</a></li>
                    <li class="breadcrumb-item"><a href="../index.html" class="text-secondary text-decoration-none">PHP</a></li>
                    <li class="breadcrumb-item active text-info" aria-current="page">Solucionario Completo</li>
                </ol>
            </nav>

            <div class="d-flex flex-column flex-md-row justify-content-between align-items-start align-items-md-center gap-3">
                <div>
                    <span class="badge bg-info text-dark fw-bold mb-2 px-3 py-1 text-uppercase tracking-wider">Práctica &bull; Solucionario Oficial</span>
                    <h1 class="display-6 fw-bold mb-2 text-white">Solucionario de Ejercicios Prácticos de PHP</h1>
                    <p class="lead text-secondary mb-0">40 ejercicios resueltos con código fuente listo para ejecutar, explicaciones técnicas y enlaces a teoría.</p>
                </div>
                <div class="d-flex align-items-center gap-2">
                    <a href="../material/ficheros/academia.sql" download class="btn btn-outline-light btn-sm d-flex align-items-center gap-2">
                        <i class="bi bi-database text-warning"></i>
                        <span>Descargar academia.sql</span>
                    </a>
                </div>
            </div>
        </div>
    </header>

    <!-- 4. Contenido Principal -->
    <main class="container-xl py-4 flex-grow-1">

        <!-- Barra de Filtros por Tema -->
        <section class="card border-0 shadow-sm rounded-3 p-3 mb-4 bg-white" aria-label="Filtro de ejercicios">
            <div class="d-flex align-items-center justify-content-between flex-wrap gap-2 mb-2">
                <div class="d-flex align-items-center gap-2">
                    <i class="bi bi-funnel-fill text-info fs-5"></i>
                    <h2 class="h6 fw-bold mb-0 text-dark">Filtrar por Tema Didáctico</h2>
                </div>
                <span class="badge bg-light text-secondary border small" id="counterBadge">Mostrando 40 ejercicios</span>
            </div>
            <div class="d-flex flex-wrap gap-1" id="filterBtnGroup">
                <button type="button" class="btn btn-sm btn-outline-secondary filter-btn active rounded-pill px-3" data-filter="all">Todos (40)</button>
                <button type="button" class="btn btn-sm btn-outline-secondary filter-btn rounded-pill px-2" data-filter="tema00">Tema 00 (2)</button>
                <button type="button" class="btn btn-sm btn-outline-secondary filter-btn rounded-pill px-2" data-filter="tema01">Tema 01 (7)</button>
                <button type="button" class="btn btn-sm btn-outline-secondary filter-btn rounded-pill px-2" data-filter="tema02">Tema 02 (9)</button>
                <button type="button" class="btn btn-sm btn-outline-secondary filter-btn rounded-pill px-2" data-filter="tema03">Tema 03 (4)</button>
                <button type="button" class="btn btn-sm btn-outline-secondary filter-btn rounded-pill px-2" data-filter="tema04">Tema 04 (5)</button>
                <button type="button" class="btn btn-sm btn-outline-secondary filter-btn rounded-pill px-2" data-filter="tema05">Tema 05 (3)</button>
                <button type="button" class="btn btn-sm btn-outline-secondary filter-btn rounded-pill px-2" data-filter="tema06">Tema 06 (3)</button>
                <button type="button" class="btn btn-sm btn-outline-secondary filter-btn rounded-pill px-2" data-filter="tema07">Tema 07 (3)</button>
                <button type="button" class="btn btn-sm btn-outline-secondary filter-btn rounded-pill px-2" data-filter="tema08">Tema 08 (1)</button>
                <button type="button" class="btn btn-sm btn-outline-secondary filter-btn rounded-pill px-2" data-filter="tema09">Tema 09 (3)</button>
            </div>
        </section>

        <!-- Listado de Ejercicios -->
        <section id="exercisesContainer">
            {all_cards_str}
        </section>

        <!-- Navegación Inferior -->
        <nav class="container-xl my-4 py-3 border-top border-bottom" aria-label="Navegación entre temas">
            <div class="d-flex justify-content-between align-items-center gap-2">
                <div>
                    <a href="09_bd.html" class="btn btn-outline-secondary btn-sm d-flex align-items-center gap-2">
                        <i class="bi bi-chevron-left"></i>
                        <span class="d-none d-sm-inline">09. Acceso a BD</span>
                    </a>
                </div>
                <div>
                    <a href="#inicio" class="btn btn-light btn-sm border d-flex align-items-center gap-1 text-secondary" title="Subir al inicio">
                        <i class="bi bi-chevron-up"></i>
                        <span class="d-none d-md-inline">Arriba</span>
                    </a>
                </div>
                <div>
                    <a href="../index.html" class="btn btn-info btn-sm text-dark d-flex align-items-center gap-2 fw-semibold">
                        <span>Índice PHP</span>
                        <i class="bi bi-house-door"></i>
                    </a>
                </div>
            </div>
        </nav>

    </main>

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
    </footer>

    <!-- Bootstrap 5.3 JS Bundle (CDN) -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>

    <!-- Filtro Interactivo de Ejercicios -->
    <script>
        document.addEventListener('DOMContentLoaded', function() {{
            const buttons = document.querySelectorAll('#filterBtnGroup .filter-btn');
            const cards = document.querySelectorAll('.exercise-card');
            const counter = document.getElementById('counterBadge');

            function applyFilter(filter) {{
                let count = 0;
                cards.forEach(card => {{
                    if (filter === 'all' || card.getAttribute('data-category') === filter) {{
                        card.classList.remove('d-none');
                        count++;
                    }} else {{
                        card.classList.add('d-none');
                    }}
                }});
                if (counter) {{
                    counter.textContent = `Mostrando ${{count}} ejercicio${{count === 1 ? '' : 's'}}`;
                }}
            }}

            buttons.forEach(btn => {{
                btn.addEventListener('click', function() {{
                    buttons.forEach(b => b.classList.remove('active'));
                    this.classList.add('active');
                    const filter = this.getAttribute('data-filter');
                    applyFilter(filter);
                }});
            }});

            // Soporte para URL hash con filtro directo (#ej_02_3)
            if (window.location.hash) {{
                const targetId = window.location.hash.substring(1);
                const targetCard = document.getElementById(targetId);
                if (targetCard) {{
                    const cat = targetCard.getAttribute('data-category');
                    const matchingBtn = document.querySelector(`#filterBtnGroup button[data-filter="${{cat}}"]`);
                    if (matchingBtn) {{
                        // No restringir el filtro si se busca un ancla concreta, pero asegurar que sea visible
                        targetCard.classList.remove('d-none');
                        targetCard.scrollIntoView({{ behavior: 'smooth' }});
                    }}
                }}
            }}
        }});
    </script>

</body>
</html>"""

    out_path = 'php/archivos/10_ejercicios_r.html'
    with open(out_path, 'w', encoding='utf-8') as fp:
        fp.write(full_html)
    print(f"Solucionario generado con éxito en {out_path} ({len(full_html)} bytes)")

    # Validar balance de tags
    c = TagChecker()
    c.feed(full_html)
    if c.errors or c.stack:
        print(f"ERRORES EN SOLUCIONARIO: {len(c.errors)} errores, {len(c.stack)} tags sin cerrar: {[x[0] for x in c.stack[-5:]]}")
        for err in c.errors[:5]:
            print("  ", err)
    else:
        print("Solucionario 100% BALANCED OK (0 errores)")

if __name__ == '__main__':
    main()
