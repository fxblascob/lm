
<?php
    function conectarBD() {
        $host = "localhost";
        $nombreBD = "videojuegos";
        $usuario = "root";
        $password = "";
        $pdo = new PDO("mysql:host=$host;dbname=$nombreBD;charset=utf8",$usuario, $password);
        return $pdo;
    }

    $deportes="aventuras";

    $pdo=conectarBD();
    $consulta = $pdo->prepare("SELECT * FROM videojuegos WHERE genero=:genero");
    $consulta->bindParam(':genero', $deportes);
    if ($consulta->execute())    {
        echo "No hay error<br>";
        while($registro = $consulta->fetch())
        {
            echo $registro['id']."----".$registro['titulo']."<br>";
        }
    }
    else
    {
        echo "Error";
    }
    $consulta = NULL;
    $pdo = NULL;
?>