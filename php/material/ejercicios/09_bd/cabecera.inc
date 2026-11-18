<!DOCTYPE html>
<html lang="es">
    <head>
        
    </head>
    <body>
        <h1>CABECERA</H1>
        <ul class="menuNavegacion">
            <li><a href="inicio.php">Inicio</a></li>
            <li><a href="noticias.php">Noticias</a></li>
        </ul>
        <form action="<?php echo $_SERVER['PHP_SELF']; ?>" method="post" enctype="multipart/form-data" >
            <label for="login">Login:</label>
                <input type="text" name="login" id="login" size="20"><br>
            <label for="email">E-mail:</label>
                <input type="text" name="email" id="email" size="50"><br>
            <select multiple name="idiomas[]" size="5">
                    <option value="Valenciano">Valenciano</option>
                    <option value="Castellano">Castellano</option>
                    <option value="Inglés">Inglés</option>
            </select><br>
            <input type="hidden" name="MAX_FILE_SIZE" value="20000" />
            <input type="file" name="fichero" /><br>
            <input  type="submit" value="enviar">
        </form>
