    <form action="subir_imagen.php" method="post" enctype="multipart/form-data">
        <p><label>titulo de la imanen<input type="text" name ="texto"></label>
        <p><input type="file" name="fichero" />        
        <p><input type="hidden" name="MAX_FILE_SIZE" value="20000" />
        <p><input type="submit" value="Enviar" /> 
    </form>