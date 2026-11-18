<?php
    $articulos = file("listado.txt", FILE_IGNORE_NEW_LINES);
    $lista = array();
    foreach ($articulos as $articulo){
        if (!empty($articulo)){
            $elemento = array('titulo' => $articulo);
            array_push($lista, $elemento);
        }
    }
    echo json_encode($lista);
?>