<?php
    function cuenta($a,$b)  {
        echo ("<h1>vamos a contar desde $a hasta $b</h1>");
        for( $i=$a; $i<=$b; $i++)
            if ($i < $b)
                echo $i.",";
            else 
                echo $i;
    }
    cuenta(10,20);
?>