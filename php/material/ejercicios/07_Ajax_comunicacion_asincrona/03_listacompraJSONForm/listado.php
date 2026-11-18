<?php
    $articulos = file("compra.txt", FILE_IGNORE_NEW_LINES);
    $lista = array();
    foreach ($articulos as $articulo){
        $elemento = array('titulo' => $articulo);
        array_push($lista, $elemento);
    }
    echo json_encode($lista);
?>