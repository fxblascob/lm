<?php
session_start();

echo "<a href=?borrar=si>Cerrar sesión</a>";

if (isset($_REQUEST["borrar"])){
    session_destroy();
    header("Location:login.php");
}

if (!isset( $_SESSION['loginusu'])){
   header("Location:login.php");

}else {
    echo "<p><a href=pag1.php>pag1.php</a>";
    echo "<p><a href=pag2.php>pag2.php</a>";
} 
?>
