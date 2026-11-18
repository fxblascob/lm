<?php
class Persona
{
    private $dni;
    private $nombre;
    private $email;
    public function __construct($dni, $nombre, $email)
    {
        $this->dni = $dni;
        $this->nombre = $nombre;
        $this->email = $email;
    }
    public function __get($nombre)
    {
        if ($nombre == 'dni')
            return $this->dni;
        else if ($nombre == 'nombre')
            return $this->nombre;
        else if ($nombre == 'email')
            return $this->email;
    }

    public function __set($nombre, $valor)
    {
        if ($nombre == 'dni')
            $this->codigo = $dni;
        else if ($nombre == 'nombre')
            $this->nombre = $valor;
        else if ($nombre == 'email')
            $this->version = $email;
    }
    public function Mostrar()
    {
        echo "<p>$this->dni, $this->nombre, $this->email";
    }
}
class Estudiante extends Persona
{
    private $numExpediente;
 
    public function __construct($dni, $nombre, $email,$numExpediente)
    {
        parent::__construct($dni, $nombre, $email);
        $this->numExpediente = $numExpediente;
    }
    public function __get($nombre)
    {
        if ($nombre == 'numExpediente')
            return $this->numExpediente;
    }

    public function __set($nombre, $valor)
    {
        if ($nombre == 'numExpedinte')
            $this->codigo = $numExpediente;
    }
    public function Mostrar()
    {
        parent::Mostrar();
        echo ",".$this->numExpediente."</p>";
    }
}

$persona = new Persona("123456789A","Pepe","pepe@edu.es");
$estudiante = new Estudiante("123456789A","Pepe","pepe@edu.es","11111111");
$persona->Mostrar();
$estudiante->Mostrar();
?>
