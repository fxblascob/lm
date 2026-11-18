<?php
    echo "<hr><h1>Manejo de ficheros 3</h1>";
    $fichero = "datos.txt";
    $fichero_copia = "copia_datos.txt";

    if (file_exists($fichero))
    {
        readfile($fichero);
        $contenido = file_get_contents($fichero);
        file_put_contents($fichero_copia, $contenido);
    }else 
        echo "El fichero ".$fichero." no existe";
        
?>