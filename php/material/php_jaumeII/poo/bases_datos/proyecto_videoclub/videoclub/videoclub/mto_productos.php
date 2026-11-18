<?php 
include "./mochuelo_lib.php";
ini_set('upload_max_filesize', '1000M');
ini_set('post_max_size', '1000M');
ini_set('max_execution_time', 300);
ini_set('memory_limit','1000M');
//phpinfo();
class Producto  extends BaseDatos{
	public $sql, $codigo, $tipo_producto, $titulo,$ruta,$genero, $subgenero,$caratula;
	
	public function __construct($codigo) {
		parent::__construct();
		$this->leer($codigo);
	}
	public function leer($codigo) {
		$this->sql="select * from productos   where codigo = '". $codigo."'  order by codigo asc limit 1";
		$this->mapear($this->consulta($this->sql));
	}
	public function primero(){
		$this->sql="select * from productos  order by codigo asc limit 1";
		$this->mapear($this->consulta($this->sql));
	}
	public function ultimo(){
		$this->sql="select * from productos  order by codigo desc limit 1";
		$this->mapear($this->consulta($this->sql));
	}
	public function siguiente($codigo){
		$this->sql="select * from productos  where codigo > '". $codigo."'  order by codigo asc limit 1";
		$this->mapear($this->consulta($this->sql));
	}
	public function anterior($codigo){
		$this->sql = "select * from productos  where codigo < '". $codigo."' order by codigo desc limit 1";
		$this->mapear($this->consulta($this->sql));
	}
	public function borrar($codigo) {
		if  ($this->ejecucion("delete from productos where codigo = '".$codigo."'") >0) 		?>	<script>	window.alert("<?php  	echo "se han borrado " .$this->afected. " registros " ?>")       </script>	<?php
		$this->mapear(null);
		$this->borrar_caratulas($codigo);
		$this->borrar_peliculas($codigo);
	}

	public function borrar_peliculas($codigo){
		$files = glob($this->ruta_peliculas.$codigo.".*");
		foreach($files as $file) 
			unlink($file);
	}
	public function borrar_caratulas($codigo){
		$files = glob($this->ruta_caratulas.$codigo.".*");
		foreach($files as $file) 	
			unlink($file);
	}
	public function insertar() {
		$sql="insert into productos (tipo_producto,titulo,genero,subgenero) values ";
		$sql = $sql."('".$this->tipo_producto."','".$this->titulo."','".$this->genero."','".$this->subgenero."')";
		if ($this->ejecucion($sql) >0)  	?>	<script>	window.alert("<?php  	echo "se han insertado " .$this->afected. " registros " ?>")       </script>	<?php
	}
	public function modificar() {
		$sql = "UPDATE productos 	SET ";
		$sql = $sql . "tipo_producto	= '".$this->tipo_producto."' ";
		$sql = $sql . ",titulo		 	= '".$this->titulo."' ";
		$sql = $sql . ",genero	 	= '".$this->genero."' ";
		$sql = $sql . ",subgenero 	= '".$this->subgenero."' ";
		$sql = $sql . " WHERE codigo   = '".$this->codigo."' ";
		$this->sql = $sql;
		echo $this->sql;
		if ($this->ejecucion($sql) > 0) 	?>	<script>	window.alert("<?php  	echo "se han modificado " .$this->afected. " registros " ?>")       </script>	<?php
	}
	public function mapear($rows) {
		parent::mapear($rows);
		if ($this->codigo >0)  {
			foreach (glob($this->ruta_peliculas.$this->codigo.".*") as $nombre_fichero) 
				$this->ruta = $nombre_fichero;
			foreach (glob($this->ruta_caratulas.$this->codigo.".*") as $nombre_fichero) 
				$this->caratula = $nombre_fichero;
		}
	}
	public function mostrar_pelicula($codigo) {
		$nombre_fichero = "";
		if ($codigo >0)  foreach (glob($this->ruta_peliculas.$codigo.".*") as $nombre_fichero) ;
		return $nombre_fichero;
	}
	public function mostrar_ruta_caratula($codigo) {
		$nombre_fichero = "";
		if ($codigo >0)   foreach (glob($this->ruta_caratulas.$codigo.".*") as $nombre_fichero) ;
		return $nombre_fichero;
	}
	public function mostrar_caratula($codigo) {
		$nombre_fichero = "";
		if ($codigo >0)  foreach (glob($this->ruta_caratulas.$codigo.".*") as $nombre_fichero) ;
		if ($nombre_fichero) return ('<img src="'.$nombre_fichero.'" border="0" width="70" height="70">');
		else return("");
	}
	
	
	public function subir_pelicula_ftp() {
		if ($_FILES && strlen($this->codigo)>0)  {
			$info = new SplFileInfo($_FILES['fichero_ruta']['name']);
			$ruta = $this->ruta_peliculas . $this->codigo.".".$info->getExtension();
			if  (strlen($info)>0) {
				$this->borrar_peliculas($this->codigo);
				$this->subir_fichero_ftp($_FILES["fichero_ruta"]["tmp_name"],$ruta);
			}
		}
	}
	public function subir_caratula(){
		if ($_FILES && strlen($this->codigo)>0) {
			$info = new SplFileInfo($_FILES['fichero_caratula']['name']);
			$ruta = $this->ruta_caratulas . $this->codigo.".".$info->getExtension();
			if  (strlen($info)>0) {
				$this->borrar_caratulas($this->codigo);
				$resultado = move_uploaded_file($_FILES["fichero_caratula"]["tmp_name"], $ruta);
				if ($resultado) {echo "caratula subida";}
				else{echo "Error al subir la caratula";}
			}
		}
	}
	public function subir_pelicula(){
		if ($_FILES && strlen($this->codigo)>0) {
			$info = new SplFileInfo($_FILES['fichero_ruta']['name']);
			$ruta = $this->ruta_peliculas . $this->codigo.".".$info->getExtension();
			if  (strlen($info)>0) {
				$this->borrar_peliculas($this->codigo);
				$resultado = move_uploaded_file($_FILES["fichero_ruta"]["tmp_name"], $ruta);
				if ($resultado){echo "pelicula subida";}
				else{echo "Error al subir la pelicula";}
			}
		}
	}
}
class ContrMantProductos extends Producto{
	public function __construct($codigo) {
		parent::__construct($codigo);
		$this->control();
	}
	public function mostrar_datos_tabla($filas) {
		print "<table border = '1'  align='center'>";
			$this->cabecera_tabla($filas);
			foreach ($filas as $fila) {
				print "<tr>"; 
					foreach ($fila as $campo=>$elem) {
						print "<td>";	
							if ($campo == "caratula") {
								print "<a href='". $this->mostrar_ruta_caratula($fila['codigo'])."'>";	
								print $this->mostrar_caratula($fila['codigo']);		
								print "</a>";
							}
							if ($campo == "ruta") 	{
								print "<a href='".$this->mostrar_pelicula($fila['codigo'])."'>";	
								print $this->mostrar_pelicula($fila['codigo']);		
								print "</a>";
							}
							if ($campo != "caratula" && $campo !="ruta") {print $elem;}
						print "</td>";
					}
					print "<td>";
						print '<a href=mto_productos.php?codigo='.$fila["codigo"].'&editar_registro=si'.'>[Editar]</a>';
					print "</td>";
					print "<td>";
						print '<a href=mto_productos.php?codigo='.$fila["codigo"].'&borrar_registro=si'.'>[Borrar]</a>';
					print "</td>";
				print "</tr>"; 
			}
		print "</table>";
	}
	public function pantalla() { 
		include "./form_mto_productos.php";
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
			if (isset($_POST['insertar']))  $this->insertar();
			if (isset($_POST['modificar']) || isset($_POST['editar_registro'])) $this->modificar();
			$this->subir_caratula();
			$this->subir_pelicula();
			$this->pantalla();
		}
	
	}
	
}

$oContrMantProductos = new ContrMantProductos(isset($_POST['codigo']) ? $_POST['codigo'] :  (isset($_GET['codigo']) ? $_GET['codigo'] :  ""));

?>