<form action="insertar_videojuego.php" method="POST">
    <p>
        <label for="titulo">titulo:</label>
        <input type="text" name="titulo" required>   
    </p>
    <p>
        <label for="genero">Genero:</label>
        <select name="genero" >
            <option value="tipo1">tipo1</option>
            <option value="tipo2">tipo2</option>
            <option value="tipo3">tipo3</option>
        </select>
    </p>
    <p>
        <label for="precio">precio:</label>
        <input type="text" name="precio" required><br>
    </p>
    <input type="submit" value="Enviar">
</form>