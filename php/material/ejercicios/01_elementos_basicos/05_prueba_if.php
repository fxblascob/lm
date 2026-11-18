<!DOCTYPE html>
<html lang="es">
    <head>
        <meta charset ="UTF-8">
        <title>Ejercicio 1</title>
    </head>
    <body>
        <h1>Página de prueba en PHP</h1>
        <?php
            $nota1 = 7;
            $nota2 = 7.5;
            $nota3 = 8;
            if ($nota1 > $nota2 && $nota1 > $nota3)
                echo "La nota mayor es: " .$nota1;
            elseif($nota2 > $nota1 && $nota2 > $nota3) 
                echo "La nota mayor es: " .$nota2;
            else 
            echo "La nota mayor es: " .$nota3;
        ?>
        <p>
    </body>
</html>

