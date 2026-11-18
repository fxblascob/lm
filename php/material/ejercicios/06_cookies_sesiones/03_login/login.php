<?php
session_start();
if (isset($_REQUEST['usuario']) && isset($_REQUEST['contrasenya'])) {
    $fichero = file('usuarios.txt');

    foreach ($fichero as $fila){
        $elemento = explode(':', $fila);
        $usuario = trim($elemento[0]);
        $contrasenya = trim($elemento[1]);
        if ($_REQUEST['usuario']==$usuario && $_REQUEST['contrasenya']==$contrasenya){
            $_SESSION['loginusu'] = $_REQUEST['usuario'];
            echo $_SESSION['loginusu'];
            header("Location:index.php");
        }
    }
    echo "<p style='color:red'>usuario o contraseña incorrectos</p>";
}
?>
<form action="<?php echo $_SERVER['PHP_SELF'] ?>" method="POST">
    <p>usuario:<input type="text" name="usuario" required>
    <p>contraseña:<input type="password" name="contrasenya" required>
    <p><input type="submit" value="Enviar">
</form>