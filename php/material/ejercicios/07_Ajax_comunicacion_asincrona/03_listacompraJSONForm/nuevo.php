<?php
    if (isset($_POST['nuevoArticulo']) && !empty($_POST['nuevoArticulo'])){
        file_put_contents ('compra.txt', PHP_EOL.$_POST['nuevoArticulo'], FILE_APPEND);
    }
    header('Location: listado.php');
?>