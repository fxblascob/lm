Actúa como un desarrollador Frontend Senior experto en UI/UX y Bootstrap 5. Necesito modernizar, simplificar y hacer más ergonómica la interfaz de este proyecto web siguiendo estas reglas estrictas:

### 1. Diagnóstico previo (Antes de editar)
Analiza la estructura de carpetas, los archivos HTML/PHP y las hojas de estilo CSS existentes. Preséntame un breve plan de acción indicando:
- Qué archivos CSS propios contienen reglas redundantes que Bootstrap 5 ya resuelve de forma nativa.
- Qué componentes o vistas necesitan mejoras de jerarquía visual, espaciado o navegación.
Espera mi confirmación antes de aplicar cambios masivos si vas a modificar más de 3 archivos a la vez.

### 2. Simplificación y limpieza de CSS
- **Bootstrap-First:** Sustituye los estilos personalizados innecesarios (márgenes, paddings, flexbox manual, grid antiguo, colores básicos, bordes y sombras) por las clases de utilidad nativas de **Bootstrap 5.3** (`d-flex`, `gap-*`, `p-*`, `m-*`, `rounded-*`, `shadow-sm`, `bg-body-tertiary`, etc.).
- **CSS mínimo:** Reduce las hojas de estilo personalizadas al mínimo indispensable (variables CSS `:root` para colores corporativos, ajustes tipográficos específicos o micro-interacciones que Bootstrap no cubra).
- **Sin `!important`:** Elimina reglas forzadas con `!important` ajustando la especificidad o usando las variables nativas de Bootstrap (`--bs-*`).

### 3. Modernización, Navegación y Ergonomía (UI/UX)
- **Menú plegable tipo hamburguesa (`navbar` / `offcanvas`):** Implementa una barra de navegación moderna y responsive con botón hamburguesa (`navbar-toggler`) que permita mostrar y ocultar el menú cómodamente. Define si conviene plegarlo únicamente en pantallas móviles/tablet (`navbar-expand-lg`) o mantenerlo siempre plegable mediante un panel lateral (`offcanvas`) para maximizar el espacio de lectura del contenido.
- **Jerarquía y respiración visual:** Aumenta el espaciado entre secciones, tarjetas y formularios (`gy-4`, `py-4`, `mb-4`) para evitar bloques de texto o botones apelotonados.
- **Componentes modernos:** Actualiza tablas, tarjetas (`card`), botones y enlaces con bordes suaves, contraste limpio, estados `:hover` claros e iconos (Bootstrap Icons si ya están en el proyecto, o SVG ligeros).
- **Ergonomía y móvil:** Garantiza que toda la interfaz sea 100% responsive (`mobile-first`), con áreas táctiles cómodas en botones/enlaces y formularios bien alineados (`form-floating` o etiquetas claras con `form-label`).

### 4. Restricciones técnicas
- **Respeta la lógica intacta:** No alteres rutas de archivos, nombres de variables, atributos `name`/`id` de formularios ni bloques de código PHP/JavaScript funcional.
- **Compatibilidad:** Mantén las versiones de Bootstrap y dependencias externas que ya utiliza el proyecto (incluyendo `bootstrap.bundle.min.js` para que el desplegable hamburguesa funcione sin errores) y no añadas frameworks nuevos.
- Ejecuta los cambios archivo por archivo de forma limpia y explícame brevemente qué CSS has eliminado y por qué clases de Bootstrap lo has sustituido.