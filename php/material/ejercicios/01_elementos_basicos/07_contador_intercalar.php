<!DOCTYPE html>
<html lang="es">
    <head>
        <meta charset ="UTF-8">
        <title>Ejercicio 1</title>
    </head>
    <body>
        <?php
        ?>
            <h1> Contadores </h1>
            <p> Este contador va del 1 al 100 </p>;
        <?php
            for ($i = 0; $i <= 100;$i++) {
                if ($i < 100) 
                    echo $i.",";
                else 
                    echo $i;
            }
        ?>
            echo "<p> Este otro va del 10 al 0</p>";
        <?php
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

