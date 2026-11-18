<!DOCTYPE html>
<html lang="es">
    <head>
        <meta charset ="UTF-8">
        <title>Ejercicio 1</title>
    </head>
    <body>
        <h1>Página de prueba en PHP</h1>
        <?php
            for ($i = 0; $i <= 100;$i++) {
                if ($i < 100) 
                    echo $i.",";
                else 
                    echo $i;
            }
            echo "<br>---------------------------<br>";
            $i = 10;
            while($i >= 1) {
                if ($i > 1) 
                    echo $i.",";
                else 
                    echo $i;
                $i--;
            }
        ?>
        <p>
    </body>
</html>

