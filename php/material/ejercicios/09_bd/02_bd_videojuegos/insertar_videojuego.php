<?php
include "cabecera.php";

function insertar($pdo){
    $insercion = $pdo->prepare("INSERT INTO videojuegos(titulo, genero, precio)" .
    " VALUES(:titulo, :genero, :precio)");
    $insercion->bindParam(':titulo', $_REQUEST['titulo']);
    $insercion->bindParam(':genero', $_REQUEST['genero']);
    $insercion->bindParam(':precio', $_REQUEST['precio']);
    return $insercion->execute();
}
//------------------------------------------------------

if (isset($_REQUEST['titulo'])){
    $pdo = conectar();
    if (insertar($pdo)) {
        echo "<h1>Inserción correcta, va a ser redirigido en 3 segundos</h1>";
        header("Refresh:3, url=index.php");
    }else 
        header("Location:error.php");
    $pdo = NULL;
}
?>