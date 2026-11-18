<form action="result_libros.php" method="POST">
    <label for="texto">Texto de búsqueda:</label>
    <input type="text" name="texto" id="texto" size="20" required><br>
    

    buscar en:<br>
    <input type="radio" id="titulo" name="buscar_en" value="titulo" required>
    <label for="titulo">titulo</label><br>
    <input type="radio" id="nombre" name="buscar_en" value="nombre" required>
    <label for="nombre">nombre</label><br>
    <input type="radio" id="autor" name="buscar_en" value="autor" required>
    <label for="autor">autor</label><br>

    <label for="tipo">Tipo de libro:</label>
    <select id="tipo" name="tipo">
      <option value="narrativa">Narrativa</option>
      <option value="libros_texto">Libros de texto</option>
      <option value="guias_mapas">Guias y mapas</option>
    </select>
    <p>
    <input type="submit" value="Enviar">
    </p>  
    <h2 style="color:red">Debes rellenar todos los campos</h2>

</form>
