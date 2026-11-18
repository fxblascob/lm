<?php
function conectar(){
    $host = "localhost";
    $nombreBD = "videojuegos";
    $usuario = "root";
    $password = "";
    $pdo = new PDO("mysql:host=$host;dbname=$nombreBD;charset=utf8",$usuario, $password);
    return $pdo;
}
?>
<!DOCTYPE html>
<html lang="es">
    <head>
        <!-- cabecera para vaciar la cache -->
        <meta http-equiv='expires' content='0'>
        <meta http-equiv='pragma' content='no-cache'>
        <meta http-equiv="Last-Modified" content="0">
        <meta http-equiv="Cache-Control" content="no-cache, mustrevalidate">

        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body {
                background-color:grey;
            }
            nav {
                border:2px   solid black;
            }
        </style>
    </head>
    <body>
        <h1> Lenguaje de marcas - Iniciación a PHP - <?php echo $_SERVER['PHP_SELF']; ?> </h1>
        <nav>
        <p> <a href="./index.php">Index</a> <a href="./form_videojuego.php">Alta videojuego</a> </p>
        </nav>

