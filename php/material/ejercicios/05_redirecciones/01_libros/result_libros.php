<?php
    // recogida de datos
    $texto     = isset($_REQUEST['texto']) ? $_REQUEST['texto'] : "";
    $buscar_en = isset($_REQUEST['buscar_en']) ? $_REQUEST['buscar_en']: "";
    $tipo      = isset($_REQUEST['tipo']) ? $_REQUEST['tipo'] : "";

    if (empty($texto) || empty($buscar_en) || empty($tipo)) {
        header("Refresh:3;url=form_libros.php");
        echo '<h2 style="color:red">Debes rellenar todos los campos</h2>';
    }
    else {
        // mostrado de datos
        echo "<h1> Recogida de datos del formulario</h1>";
        echo "<h2> Texto: $texto </h2>";
        echo "<h2> Buscar en: $buscar_en </h2>";
        echo "<h2> Tipo: $tipo </h2>";
    }
?>