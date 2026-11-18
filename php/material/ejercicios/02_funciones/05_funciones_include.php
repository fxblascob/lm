<?php
/*
Crea una página llamada 04_descuento.php en la carpeta de ejercicios. 
Crea una función llamada calculaDescuento que reciba un parámetro $precio con el precio de una compra,
y un parámetro opcional llamado $descuento con el porcentaje de descuento a aplicar. 
Si no se pone este segundo parámetro, el valor por defecto será 0. 
La función devolverá con un return el precio con el descuento aplicado. 
Utiliza después la función desde el código PHP para calcular el descuento de un precio de 250 euros 
con un 10% de descuento, y el de un precio de 85 euros sin indicar descuento.
*/
    include "./05_funciones_include.inc";
   
    $precio = 100;
    $descuento = 20;
    
    calculaDescuento($precio,$descuento)
?>