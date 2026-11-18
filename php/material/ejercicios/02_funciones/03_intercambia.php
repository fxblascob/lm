<?php
/*
Crea una página llamada 03_intercambia.php en la carpeta de ejercicios. Añade dentro una función llamada intercambia que reciba 2 parámetros numéricos por referencia, y lo que haga sea intercambiar sus valores. Es decir, si recibe el parámetro $a y el $b, debe hacer que $a tome el valor de $b, y $b tome el valor de $a.
*/
    function intercambia(&$a,&$b)  {
        $aux = $a;
        $a = $b;
        $b = $aux;
    }
    $a = 10;
    $b = 20;
    echo ("<h1> Antes del intercambio  \$a = $a Y \$b= $b</h1>");
    intercambia($a,$b);
    echo ("<h1> Después del intercambio \$a = $a Y \$b= $b</h1>");
?>