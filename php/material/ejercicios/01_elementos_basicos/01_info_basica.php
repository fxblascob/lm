<!DOCTYPE html>
<html lang="es">
    <head>
        <meta charset ="UTF-8">
        <title>Ejercicio 1</title>
    </head>
    <body>
        <h1>Página de prueba en PHP</h1>
        <?php
            $nombre = "Javier Blasco";
            $anyo = 1967;
        ?>
        <p>Me llamo <?php echo $nombre; ?> y he nacido en el año <?php echo $anyo; ?>.</p>
        <?php
            $dato="Hola";
            //unset($dato);		// La variable dato deja de existir
            $dato = "";
            if (empty($dato))
                echo "vacio";
            else
                echo "relleno";	// Diría que es cierto, porque $dato está vacía	
        ?>
    </body>
</html>

