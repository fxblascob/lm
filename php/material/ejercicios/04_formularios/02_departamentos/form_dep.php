<form action="presupuesto.php" method="POST">
  <label for="departamento">Departamento:</label>
  <select id="departamento" name="departamento">
    <option value="INFORMÁTICA">INFORMÁTICA</option>
    <option value="LENGUA">LENGUA</option>
    <option value="MATEMÁTICAS">MATEMÁTICAS</option>
    <option value="INGLÉS">INGLÉS</option>
  </select>
  <hr>
  <label for="departamentos">Departamentos</label>
  <select multiple name="departamentos[]" size="5">
    <option value="INFORMÁTICA">INFORMÁTICA</option>
    <option value="LENGUA">LENGUA</option>
    <option value="MATEMÁTICAS">MATEMÁTICAS</option>
    <option value="INGLÉS">INGLÉS</option>
    </select>
    <hr>
  <input type="submit" value="Enviar" />
</form>
