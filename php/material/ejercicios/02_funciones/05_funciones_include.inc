<?php
    function calculaDescuento($precio,$descuento=0)  {
        $precioDescuento = $precio - $precio * $descuento /100;
        echo ("Precio: $precio, descuento: $descuento, precio con el descuento: $precioDescuento");
    }
    $precio = 100;
    $descuento = 20;
    
    calculaDescuento($precio,$descuento)
?>