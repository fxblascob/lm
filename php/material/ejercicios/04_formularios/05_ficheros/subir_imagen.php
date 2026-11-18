<?php
    if (isset($_REQUEST['texto'])){
        echo "se envia algo";
        if (is_uploaded_file ($_FILES['fichero']['tmp_name']) &&
         ( $_FILES['fichero']['type'] == "image/jpeg" || $_FILES['fichero']['type'] == "image/png"))
        {
            echo ("<pre>");
            print_r($_FILES);
            echo("</pre>");
            $directorio = "./imgs/";
            if (!file_exists($directorio))  mkdir($directorio);

            $fichero =  $_FILES['fichero']['name']; 
            move_uploaded_file ($_FILES['fichero']['tmp_name'], $directorio.$fichero); 

            print ("<p>Fichero subido correctamente</p>");
            print("<p>Nombre: ".$_FILES['fichero']['name'] );
            print("<p>Destino: ".$directorio . $fichero );
            print("<p><img src=".$directorio. $fichero .">");
        } else
        print ("No se ha podido subir el fichero\n");
    }
?>
