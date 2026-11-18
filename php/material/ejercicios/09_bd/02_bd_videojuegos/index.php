<?php
    include "cabecera.php";
    //------------------------------------------
    $pdo = conectar();
    $consulta = $pdo->prepare("SELECT * FROM videojuegos ");

    if ($consulta->execute()) {
        echo "<ol><h2>Listado de todos los videojuegos</h2>";
        while($registro = $consulta->fetch())
        {
            echo "<li>".$registro['titulo']." - " .$registro['genero']." - " .$registro['precio'];
        }
        echo"</ol>";
        $pdo = NULL;
    }else {
        echo "<p>Error</p>";
    }
    
?>