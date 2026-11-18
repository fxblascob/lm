<?php
session_start();
//si han pulsado en vaciar el carrito o el carrito no existe inicializo el carrito y el total
if (isset($_REQUEST['borrar']) || !isset($_SESSION['carrito'])){
    $_SESSION['carrito'] = array();
    $_SESSION['total'] = 0;
    //session_destroy();
}
// los articulos
$articulos = array(
    array("id" => 1, "nombre" => "Zapatillas Nike", "precio" => 60),
    array("id" => 2, "nombre" => "Sudadera Domyos", "precio" => 15),
    array("id" => 3, "nombre" => "Pala de pádel Vairo", "precio" => 50),
    array("id" => 4, "nombre" => "Pelota de baloncesto Molten", "precio" => 20)
);
//muestro los articulos
foreach ($articulos as $articulo)  {
    $id     = $articulo['id'];
    $nombre = $articulo['nombre'];
    $precio = $articulo['precio'];
    echo "<p>$id - <a href=carro.php?id=$id> $nombre </a> - $precio ";
}

//si han pulsado en un articulo, lo añado al carrito como un array y sumo el precio
if (isset($_REQUEST['id'])){
    foreach($articulos as $articulo) {
        if ($articulo["id"] == $_REQUEST["id"]) {
            array_push($_SESSION["carrito"], $articulo);
            $_SESSION["total"] += $articulo["precio"];
        }
    }
}
//muestro el carrito-------------------
if (isset($_SESSION['carrito'])) {
    echo "<h2> Carrito </h2>";
    foreach ($_SESSION["carrito"] as $articulo){
        echo "<p>".$articulo["nombre"] ." (" .$articulo["precio"] . ") euros";
    }
    echo "<p>TOTAL: " . $_SESSION["total"] . "<p>";
    echo "<p><a href=carro.php?borrar=si>Borrar carro</p>";
}  

?>