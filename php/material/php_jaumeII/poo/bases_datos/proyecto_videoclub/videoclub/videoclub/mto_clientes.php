<?php 
include "./mochuelo_lib.php";

class Cliente  extends BaseDatos{
	public $sql, $codigo, $nom_videoclub, $dni,$nombre,$apellidos, $direccion,$num_tarjeta,$usuario,$password,$tipousuario;
	
	public function __construct($codigo) {
		parent::__construct();
		$this->leer($codigo);
	}
	public function leer($codigo) {
		$this->sql="select * from clientes   where codigo = '". $codigo."'  order by codigo asc limit 1";
		$this->mapear($this->consulta($this->sql));
	}
	public function primero(){
		$this->sql="select * from clientes  order by codigo asc limit 1";
		$this->mapear($this->consulta($this->sql));
	}
	public function ultimo(){
		$this->sql="select * from clientes  order by codigo desc limit 1";
		$this->mapear($this->consulta($this->sql));
	}
	public function siguiente($codigo){
		$this->sql="select * from clientes  where codigo > '". $codigo."'  order by codigo asc limit 1";
		$this->mapear($this->consulta($this->sql));
	}
	public function anterior($codigo){
		$this->sql = "select * from clientes  where codigo < '". $codigo."' order by codigo desc limit 1";
		$this->mapear($this->consulta($this->sql));
	}
	public function borrar($codigo) {
		if  ($this->ejecucion("delete from clientes where codigo = '".$codigo."'") >0) 		?>	<script>	window.alert("<?php  	echo "se han borrado " .$this->afected. " registros " ?>")       </script>	<?php
		$this->mapear(null);
	}
	public function insertar() {
		$sql="insert into clientes (nombre,apellidos,dni,direccion,num_tarjeta,usuario,password,tipousuario) values ";
		$sql = $sql."('".$this->nombre."','".$this->apellidos."','".$this->dni."','".$this->direccion."','".$this->num_tarjeta."','".$this->usuario."','".$this->password."','".$this->tipousuario."')";
		if ($this->ejecucion($sql) >0) 	?>	<script>	window.alert("<?php  	echo "se han insertado " .$this->afected. " clientes " ?>")       </script>	<?php
	}
	public function modificar() {
		$sql = "UPDATE clientes 	SET ";
		$sql = $sql . "nombre  		= '".$this->nombre."' ";
		$sql = $sql . ",apellidos 	= '".$this->apellidos."' ";
		$sql = $sql . ",dni       		= '".$this->dni."' ";
		$sql = $sql . ", direccion 	= '".$this->direccion."' ";
		$sql = $sql . ",num_tarjeta 	= '".$this->num_tarjeta."' ";
		$sql = $sql . ",usuario		 = '".$this->usuario."' ";
		$sql = $sql . ",password	 = '".$this->password."' ";
		$sql = $sql . ",tipousuario   = '".$this->tipousuario."' ";
		$sql = $sql . " WHERE codigo = '".$this->codigo."' ";
		
		if ($this->ejecucion($sql) > 0) {	?>	<script>	window.alert("<?php  	echo "se han modificado " .$this->afected. " registros " ?>")       </script>	<?php 
			
		}
	}
}
class ContrMantClientes extends Cliente{
	public function __construct($codigo) {
		parent::__construct($codigo);
		$this->control();
	}
	public function mostrar_datos_tabla($filas) {
		print "<table border = '1'  align='center'>";
			$this->cabecera_tabla($filas);
			foreach ($filas as $fila) {
				print "<tr>"; 
					foreach ($fila as $elem)	
						print "<td>".$elem."</td>";
					print "<td>";
						print '<a href=mto_clientes.php?codigo='.$fila["codigo"].'&editar_registro=si'.'>[Editar]</a>';
					print "</td>";
					print "<td>";
						print '<a href=mto_clientes.php?codigo='.$fila["codigo"].'&borrar_registro=si'.'>[Borrar]</a>';
					print "</td>";
				print "</tr>"; 
			}
		print "</table>";
	}
	public function pantalla() { 
		include "./form_mto_clientes.php";
	}
	public function control() {
		if  ( 	!isset($_POST['enviar']) && !isset($_POST['primero']) &&  !isset($_POST['siguiente']) && !isset($_POST['ultimo']) &&  !isset($_POST['anterior']) &&  !isset($_POST['insertar'])  && !isset($_POST['borrar']) && !isset($_POST['modificar'])&& !isset($_GET['editar_registro']) && !isset($_GET['borrar_registro']))
			$this->pantalla();
		
		if (isset($_POST['cadena_sql'])) {
			$this->sql=$_POST['cadena_sql'];
			$this->pantalla();
			if ($rows=$this->consulta($this->sql)) {
				$this->mostrar_datos_tabla($rows);
			}
		}
		if (isset($_POST['primero']) || isset($_POST['ultimo']) || isset($_POST['siguiente']) || isset($_POST['anterior']) ) {
			$codigo = (isset($_POST['codigo']) ? $_POST['codigo'] :  "");
			if (isset($_POST['primero'])) $this->primero();
			if (isset($_POST['ultimo']))    $this->ultimo();
			if (isset($_POST['siguiente'])) $this->siguiente($codigo);
			if (isset($_POST['anterior'])) $this->anterior($codigo);
			$this->pantalla();
		}
		if (isset($_POST['borrar']) || isset($_GET['borrar_registro'])) {
			$codigo = "";
			if (isset($_POST['codigo'])) $codigo = $_POST['codigo'];
			if (isset($_GET['codigo']))   $codigo = $_GET['codigo'];
			$this->borrar($codigo);
			$this->pantalla();
		}
		if (isset($_POST['insertar']) || isset($_POST['modificar']) || isset($_GET['editar_registro'])) {
			if (isset($_POST['codigo'])) {
				$this->mapear($_POST);
			}else if (isset($_GET['codigo'])) {
				$this->leer($_GET['codigo']);
			}
			if (isset($_POST['insertar'])) $this->insertar();
			if (isset($_POST['modificar']) || isset($_POST['editar_registro'])) $this->modificar();
			$this->pantalla();
		}
	}
}

$oContrMantClientes = new ContrMantClientes(isset($_POST['codigo']) ? $_POST['codigo'] :  (isset($_GET['codigo']) ? $_GET['codigo'] :  ""));

?>