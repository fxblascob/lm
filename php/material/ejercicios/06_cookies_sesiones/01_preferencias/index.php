<?php
if (isset($_COOKIE['nombreusu']) && isset($_COOKIE['colorusu'])) {
    $color = $_COOKIE['colorusu'];
    $nombre = $_COOKIE['nombreusu'];
    echo "<style>body { background-color: " . $color . "; }</style>";
    echo "<h1>bienvenido ".$nombre."</h1>";
}else{
    echo "<style>body { background-color:white; }</style>";
    echo "<h1>Página de inicio</h1>";
}
echo "<p><a href='preferencias.php'>Preferencias</a>";
echo "<p><a href='borrar_prefs.php'>Borrar Preferencias</a>"
?>