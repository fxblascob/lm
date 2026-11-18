<?php 
include('cabecera.inc'); 

$error = $_GET['error'];
// mostrado de datos
echo "<h1>  ERROR </h1>";
echo "<h2>  $error </h2>";
echo "<a href='formulario.php'> Volver al formulario </a>";
        
include('pie.inc'); 
?>