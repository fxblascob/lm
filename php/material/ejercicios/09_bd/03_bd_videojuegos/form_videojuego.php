<?php include("cabecera.inc"); ?>
<form action="insertar_videojuego.php" method="POST">
    <p>
        <label for="titulo">titulo:</label>
        <input type="text" name="titulo" required>   
    </p>
    <p>
        <label for="genero">Genero:</label>
        <select name="genero" required>
            <option value="Aventura">Aventura</option>
            <option value="Arcade">Arcade</option>
            <option value="Estrategia">Estrategia</option>
        </select>
    </p>
    <p>
        <label for="precio">precio:</label>
        <input type="text" name="precio" required><br>
    </p>
    <input type="submit" value="Enviar">
</form>

<?php include("pie.inc"); ?>