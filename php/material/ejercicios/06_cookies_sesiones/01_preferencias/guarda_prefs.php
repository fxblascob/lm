<?php
echo $_POST["nombre"];
echo $_POST["color"];
setcookie("nombreusu",$_POST["nombre"], time()+300);
setcookie("colorusu",$_POST["color"], time()+300);
header('Location:index.php');
?>
