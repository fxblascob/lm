    <?php include("cabecera.inc"); ?>

    <form action="<?php echo $_SERVER['PHP_SELF']; ?>" method="get">
        <label for="precio">Introduce un importe para buscar juegos más baratos</label>
        <input type="number" name="precio" required>
        <input type="submit" value="Enviar">
    </form>
   

    <?php

    function conectar() {
        $host = "localhost";
        $nombreBD = "videojuegos";
        $usuario = "root";
        $password = "";
        $pdo = new PDO("mysql:host=$host;dbname=$nombreBD;charset=utf8",$usuario, $password);
        return $pdo;
    }
    
    $pdo = conectar();

    if (isset($_REQUEST['precio']) && !empty($_REQUEST['precio'])){
        $consulta = $pdo->prepare("SELECT * FROM videojuegos where precio < :precio ");
        $consulta->bindParam(':precio',$_REQUEST['precio']);
        echo "<h2> Listado de los juegos cuyo precio es menor que ".$_REQUEST['precio']." </h2>";
    }else {
        $consulta = $pdo->prepare("SELECT * FROM videojuegos");
        echo "<h2> Listado de todos los juegos </h2>";
    }

    $consulta->execute();

    while($registro = $consulta->fetch())
        echo "<p>".$registro['titulo']." - " .$registro['genero']." - " .$registro['precio'];

    $pdo = NULL;
    
    include("pie.inc"); 
?>
