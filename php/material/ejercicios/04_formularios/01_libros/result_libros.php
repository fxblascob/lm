<?php
    // recogida de datos
    $texto     = isset($_REQUEST['texto']) ? $_POST['texto'] : "undefined";
    $buscar_en = isset($_REQUEST['buscar_en']) ? $_POST['buscar_en']: "undefined";
    $tipo      = isset($_REQUEST['tipo']) ? $_POST['tipo'] : "undefined";

    // mostrado de datos
    echo "<h1> Recogida de datos del formulario</h1>";
    echo "<h2> Texto: $texto </h2>";
    echo "<h2> Buscar en: $buscar_en </h2>";
    echo "<h2> Tipo: $tipo </h2>";
?>