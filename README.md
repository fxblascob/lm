# Lenguajes de Marcas y Sistemas de Gestión de Información (LMSGI)

Repositorio con el temario, ejercicios prácticos, soluciones y recursos didácticos para el módulo formativo de **Lenguajes de Marcas y Sistemas de Gestión de Información** (Ciclos Formativos de Grado Superior de Informática: DAW, DAM y ASIR).

---

## 📚 Estructura de Contenidos

El material está organizado en una web central (`index.html`) que articula los diferentes bloques temáticos:

| Bloque | Directorio | Descripción |
| :--- | :--- | :--- |
| **0. Introducción** | Raíz (`tema1_...`) | Conceptos iniciales y evolución de los lenguajes de marcas. |
| **1. HTML** | [`html/`](./html) | Sintaxis HTML, estructura, formato, enlaces, tablas, formularios y HTML5. |
| **2. CSS** | [`css/`](./css) | Hojas de estilo, selectores, reglas de cascada, diseño adaptativo y Bootstrap. |
| **3. XML** | [`xml/`](./xml) | Documentos XML bien formados, validación con DTD y consultas con XPath. |
| **4. JavaScript** | [`javascript/`](./javascript) | Programación en cliente, sintaxis, manipulación del DOM, BOM y eventos. |
| **5. PHP** | [`php/`](./php) | Desarrollo web del lado del servidor, formularios, sesiones, POO y acceso a BBDD (PDO). |

---

## 🚀 Cómo Visualizar el Material

### Visualización en local
1. Clona el repositorio o descarga los archivos.
2. Abre el archivo `index.html` en cualquier navegador web moderno (Firefox, Chrome, Edge, Brave).
3. Alternativamente, puedes iniciar un servidor HTTP local desde la raíz del proyecto:
   ```bash
   python3 -m http.server 8080
   ```
   Y acceder a `http://localhost:8080`.

### Ejercicios de PHP y Bases de Datos
Para ejecutar los ejemplos y prácticas de la sección `php/`:
- Se requiere un entorno LAMP, XAMPP o servidor web con PHP >= 7.4 y MySQL/MariaDB.
- Los volcados SQL incluidos (`alumnos.sql`, `ies.sql`, `academia.sql`) contienen esquemas y datos de prueba ficticios preparados para su importación en clase.

---

## 🛠️ Tecnologías y Recursos
- **HTML5 & CSS3**
- **JavaScript (ES6+)**
- **XML / DTD / XPath**
- **PHP & MySQL / MariaDB (PDO)**
- **Bootstrap 5.1.3**
