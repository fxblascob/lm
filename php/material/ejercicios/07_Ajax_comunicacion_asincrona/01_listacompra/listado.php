<?php
    $html ="<p>Lista obtenida desde el fichero 'listado.txt'";
    $html .= "<ul>";
    $fichero = file('listado.txt');
    echo "<pre>";
    print_r($fichero);
    echo "</pre>";
    foreach ($fichero as $fila){
        $html .= "<li> $fila</li>";
    }
    $html .= "</ul>";
    echo $html;
?>