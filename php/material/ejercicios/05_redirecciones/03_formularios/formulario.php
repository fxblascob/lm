<?php  
  include('cabecera.inc');

  if (isset($_REQUEST['login']) && isset($_REQUEST['password']) && isset($_FILES['fichero']['tmp_name'])) {
    $login = isset($_REQUEST['login']) ? $_REQUEST['login'] : "";
    $password = isset($_REQUEST['password']) ? $_REQUEST['password'] : "";
    $fichero = isset($_FILES['fichero']) ? $_FILES['fichero']['tmp_name'] : "";

    if (is_uploaded_file ($_FILES['fichero']['tmp_name']))   {
      $nombreDirectorio = "fotos/";
      $idUnico = time();   
      $nombreFichero = $idUnico . "-" . $_FILES['fichero']['name']; 
      move_uploaded_file ($_FILES['fichero']['tmp_name'], $nombreDirectorio .  $nombreFichero); 
    } else
        print ("No se ha podido subir el fichero\n");

    if (empty($login) || empty($password) || empty($fichero)) {
      $error = empty($login) ? "falta el usuario "  : "";
      $error .=  empty($password) ? "falta la  contraseña " : "";
      $error .=  empty($fichero) ? "falta la foto " : "";
      header("Location:error.php?error=".$error);
    }else {
      echo "<h2> tu login : $login </h2>";
      echo "<h2> tu password : $password </h2>";
      echo "<h2> tu foto : $fichero </h2>";
    }
  }else {
    ?>
    <form action="<?php echo $_SERVER['PHP_SELF']; ?>" method="POST" enctype="multipart/form-data">
        <label for="login">Usuario:</label>
        <input type="text" name="login" id="login" size="20" ><br>
        

        <label for="password">Password:</label>
        <input type="password" id="password" name="password" >

        <p><label for="foto">Fotografia</label>
        <input type="file" id="fichero"  name="fichero" >

        <input type="hidden" name="MAX_FILE_SIZE" value="20000" />
        <p><input type="submit" id="enviar"  value="Enviar" >
      </form>
    <?php
  }
  include('pie.inc');
  ?>
