<?php
function conectar() {
    $host = "localhost";
    $nombreBD = "videojuegos";
    $usuario = "root";
    $password = "";
    $pdo = new PDO("mysql:host=$host;dbname=$nombreBD;charset=utf8",$usuario, $password);
    return $pdo;
}

function insertar($pdo){
    $insercion = $pdo->prepare("INSERT INTO videojuegos(titulo, genero, precio)" .
    " VALUES(:titulo, :genero, :precio)");
    $insercion->bindParam(':titulo', $_REQUEST['titulo']);
    $insercion->bindParam(':genero', $_REQUEST['genero']);
    $insercion->bindParam(':precio', $_REQUEST['precio']);
    return $insercion->execute();
}

if (isset($_REQUEST['titulo'])){
    $pdo = conectar();
    if (insertar($pdo)) 
        header("Location:index.php");        
    else 
        header("Location:error.php");
    $pdo = NULL;
}
?>