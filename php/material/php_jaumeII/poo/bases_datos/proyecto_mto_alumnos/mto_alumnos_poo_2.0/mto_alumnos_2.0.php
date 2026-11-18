<?php
class BaseDatos {
	private $db="alumnos";
	private $host="localhost";
	private $user="root";
	private $pass="";
	public $sql="select * from alumnos";
	public $rows=null;
	public $afected=0;
	protected $objPDO = null,  $error=null;
	public function __construct() {
		try {
			$this->objPDO = new PDO("mysql:dbname=".$this->db.";charset=utf8mb4;host=".$this->host, $this->user,$this->pass);
		} catch (PDOException $e) { 
			$this->error = 'Fallo en la conexion. Error: '  . $e->getMessage(); 
			print $this ->error;
		}
	}
	public function consulta($sql){
		$this->rows=null;
		if ($this->objPDO) {
			if ($objPDOStatement = $this->objPDO->query($sql)) {
				$this->rows = $objPDOStatement->fetchAll(PDO::FETCH_ASSOC);
			}
		}
		return($this->rows);
	}
	public function ejecucion($sql){
		$this->afected=0;
		if ($this->objPDO) {
			$this->afected = $this->objPDO->exec($sql);
			if ($this->afected==0) {
				$this->error= $this->objPDO->errorInfo();
				print ( $this->error[2]);
			}else {
				if ($this->objPDO->lastInsertId()>0 ) $this->id = $this->objPDO->lastInsertId();
			}
		}
		return ($this->afected);
	}
	public function mapear($rows) {
		if  ($rows){
			if (isset($rows[0] )) 	foreach ($rows[0] as $campo=>$valor) 	$this->$campo = $valor;
			else				foreach ($rows as $campo=>$valor) 	$this->$campo = $valor;
		}
	}
	
}
class Util {
	const RUTA_FOTOS=".".DIRECTORY_SEPARATOR."fotos".DIRECTORY_SEPARATOR;
	
	public static function borrar_foto($id) {
		if ($id >0)  {
			foreach (glob(self::RUTA_FOTOS.$id.".*") as $nombre_fichero) {
				if ($nombre_fichero) unlink($nombre_fichero);
			}
		}
	}
	
	
	public static function ruta_foto($id) {
		if ($id >0)  {
			foreach (glob(self::RUTA_FOTOS.$id.".*") as $nombre_fichero) {
				if ($nombre_fichero) return($nombre_fichero);
				else return("");
			}
		}
		return("");
	}
	public static function guardar_foto($id){
		if ($_FILES){
			$error = $_FILES['fichero_foto']['error'];
			if ($error==0) {
				$target_dir = self::RUTA_FOTOS;
				$target_file = $target_dir . basename($_FILES["fichero_foto"]["name"]);
				$uploadOk = true;
				$imageFileType = strtolower(pathinfo($target_file,PATHINFO_EXTENSION));
				// Check if image file is a actual image or fake image
				
				$check = getimagesize($_FILES["fichero_foto"]["tmp_name"]);
				if($check == false) {
					echo "no es na imagen .";
					$uploadOk = false;
				}
				//--------------nuevo nombre-----------------
				$target_file = $target_dir .$id.".".$imageFileType;
				// Check file size
				if ($_FILES["fichero_foto"]["size"] > 5000000) {
				    echo "fichero demasiado grande";
				    $uploadOk = false;
				}
				// Allow certain file formats
				if($imageFileType != "jpg" && $imageFileType != "png" && $imageFileType != "jpeg"  && $imageFileType != "gif" ) {
				    echo "Lo siento, solo se permite JPG, JPEG, PNG & GIF.";
				    $uploadOk = false;
				}
				// Check if $uploadOk is set to 0 by an error
				if ($uploadOk) {
					self::borrar_foto($id);
					if (move_uploaded_file($_FILES["fichero_foto"]["tmp_name"], $target_file)) {
						echo "El fichero  $target_file se ha subido con éxito.";
					} else echo "Lo siento, ha ocurrido un error al subir el fichero.";
					    
				}else echo " no se ha subido el fichero. Error";
			}elseif ($error == 1) echo "1-Fichero demasiado grande supera MAX_FILE_SIZE de php.ini";
			  elseif ($error == 2) echo "2-Fichero demasiado grande supera MAX_FILE_SIZE del HTML";
			  elseif ($error == 3) echo "3-Fichero parcialmente subido";
			  elseif ($error == 6) echo "6-falta la carpeta temporal";
			  elseif ($error == 7) echo "7-No se pudo escribir el fichero  a disco";
			  elseif ($error == 8) echo "8-Una extensión de PHP detuvo la subida del fichero";
			  //elseif ($error == 4) echo "4-No se ha subido ninguna  foto";
		}
	}
}
class Alumno extends BaseDatos {
	public $id="", $nombre="",$apellidos="",$curso="",$grupo="",$anyo="",$numord="",$aula="",$foto="";
	

	public function mapear($rows) {
		parent::mapear($rows);
		$this->foto=  Util::ruta_foto($this->id);
	}
	
	public function leer($id) {
		$this->sql= "select * from alumnos  where id = $id ";
		$rows=$this->consulta($this->sql);
		$this->mapear($rows);
	}
	public function buscar($nombre,$apellidos){
		$rows=$this->consulta("select * from alumnos  where apellidos like '%$apellidos%' and nombre like '%$nombre%'" );
		return($rows);
	}
	public function primero(){
		$this->sql= "select * from alumnos  order by id limit 1";
		$rows=$this->consulta($this->sql);
		$this->mapear($rows);
	}
	public function ultimo(){
		$this->sql="select * from alumnos  order by id desc limit 1";
		$rows=$this->consulta($this->sql);
		$this->mapear($rows);
	}
	public function siguiente(){
		$this->sql="select * from alumnos   where id >  $this->id  order by id asc limit 1";
		$rows=$this->consulta($this->sql);
		$this->mapear($rows);
		
	}
	function anterior(){
		$this->sql = "select * from alumnos   where id <  $this->id order by id desc limit 1";
		$rows=$this->consulta($this->sql);
		$this->mapear($rows);
	}
	function borrar($id) {
		$this->afected = $this->ejecucion("delete from alumnos where id = ".$id);
		if  ($this->afected>0) {
			?>	<script>	window.alert("<?php  	echo "se han borrado " .$this->afected. " alumnos " ?>")       </script>	<?php
		}
	}
	function insertar() {
		$sql="insert into alumnos (nombre,apellidos,anyo,curso,grupo,numord,aula) values ";
		$sql = $sql."('".$this->nombre."','".$this->apellidos."','".$this->anyo."','".$this->curso."','".$this->grupo."',".$this->numord.",".$this->aula.")";
		//echo $sql;
		$this->afected= $this->ejecucion($sql);
		if ($this->afected > 0) {
			?>	<script>	window.alert("<?php  	echo "se han insertados " .$this->afected. " alumnos " ?>")       </script>	<?php
		}
		
		
	
	}
	function modificar() {
		$this->sql = "UPDATE alumnos	SET nombre  =  '$this->nombre' ,apellidos = '$this->apellidos',anyo = '$this->anyo',curso = '$this->curso',grupo = '$this->grupo',aula = '$this->aula',numord = '$this->numord' WHERE id = '$this->id' ";
		
		$this->afected= $this->ejecucion($this->sql);
		if ($this->afected>0) {
			?>	<script>	window.alert("<?php  	echo "se han modificado " .$this->afected. " alumnos " ?>")       </script>	<?php
		}

	}

}
class VistaAlumnos {
	public function mostrar_datos_tabla($filas) {
		print "<div id= 'contenedor_listado'>";
			print "<table border = '1'  align='center'>";
				$this->cabecera_tabla($filas);
				foreach ($filas as $fila) {
					print "<tr>"; 
					foreach ($fila as $elem)	
						print "<td>".$elem."</td>";
					print "<td>";
						print '<img src="'.Util::ruta_foto($fila["id"]).'" border="0" width="70" height="70">';
					print "</td>";
					print "<td>";
						print '<a href='.$_SERVER["PHP_SELF"].'?id='.$fila["id"].'&editar_alumno=si'.'>[Editar]</a>';
						
					print "</td>";
					print "<td>";
						print '<a href='.$_SERVER["PHP_SELF"].'$id='.$fila["id"].'&borrar_alumno=si'.'>[Borrar]</a>';
					print "</td>";
					print "</tr>"; 
				}
			print "</table>";
		print "</div>";
	}
	public function cabecera_tabla($filas) {
		if ($filas)  {
			foreach ($filas as $fila)  {
				print "<tr>";
				foreach ($fila as $indice => $elemento) 	print "<td>$indice</td>";
				print "</tr>";
				break;
			}
		}
	}
	public  function formulario($obj) { 
		$diccionario = array(
			'form_action'=>$_SERVER["PHP_SELF"] ,
			'form_id' => $obj->id ,
			'form_nombre' => $obj->nombre,
			'form_apellidos' => $obj->apellidos,
			'form_curso' => $obj->curso,
			'form_grupo' => $obj->grupo,
			'form_aula' => $obj->aula,
			'form_anyo' => $obj->anyo,
			'form_numord' => $obj->numord,
			'form_sql' => $obj->sql,
			'form_foto' => $obj->foto 
		);
		$template = file_get_contents('./mto_alumnos.html');
		
		foreach ($diccionario as $clave=>$valor) {
			$template = str_replace('{'.$clave.'}', $valor, $template);
		}
		print $template;
	}
}



class ControladorAlumnos {
	
	public function __construct($miarray) {
		
		$oAlumno= new Alumno();
		$oVista= new VistaAlumnos();
		
		if  ( 	!isset($_POST['enviar']) && !isset($_POST['primero']) &&    
			!isset($_POST['siguiente']) && !isset($_POST['ultimo']) &&   
			!isset($_POST['anterior']) &&  !isset($_POST['anterior']) && 
			!isset($_POST['insertar'])  && !isset($_POST['borrar']) &&
			!isset($_POST['modificar'])&& !isset($_GET['editar_alumno']) && 
			!isset($_GET['borrar_alumno']) && !isset($_POST['limpiar']) ||  (isset($_POST['limpiar'])))
		$oVista->formulario($oAlumno);

		if (isset($_POST['enviar']) ) {
			$sql=$_POST['cadena_sql'];
			$oVista->formulario($oAlumno);
			if ($rows=$oAlumno->consulta($sql)) {
				$oVista->mostrar_datos_tabla($rows);
			}
		}
		if (isset($_POST['buscar'])) {
			$oVista->mostrar_datos_tabla($oAlumno->buscar($_POST['nombre'],$_POST['apellidos']));
		}

		if (isset($_POST['primero'])) {
			$oAlumno->primero();
			$oVista->formulario($oAlumno);
			$oVista->mostrar_datos_tabla($oAlumno->rows);
		}
		if (isset($_POST['ultimo'])) {
			$oAlumno->ultimo();
			$oVista->formulario($oAlumno);
			$oVista->mostrar_datos_tabla($oAlumno->rows);
		}
		if (isset($_POST['siguiente'])) {
			$oAlumno->id=$miarray['id'];
			$oAlumno->siguiente();
			$oVista->formulario($oAlumno);
			$oVista->mostrar_datos_tabla($oAlumno->rows);
		}
		if (isset($_POST['anterior'])) {
			$oAlumno->id=$miarray['id'];
			$oAlumno->anterior();
			$oVista->formulario($oAlumno);
			$oVista->mostrar_datos_tabla($oAlumno->rows);
		}
		if (isset($_POST['borrar']) || isset($_GET['borrar_alumno'])) {
			$id = (isset($_POST['id']) ? $_POST['id'] :  $_GET['id']);
			$oAlumno->borrar($id);
			Util::borrar_foto($id);
			$oVista->formulario($oAlumno);
		}
		if (isset($_POST['insertar']) || isset($_POST['modificar'])) {
			$oAlumno->mapear($_POST);
			//print "<pre>";
			//print_r($_FILES);
			//print "</pre>";
			if (isset($_POST['insertar'])) $oAlumno ->insertar();
			else  $oAlumno->modificar();
			Util::guardar_foto($oAlumno->id);
			$oAlumno->foto = Util::ruta_foto($oAlumno->id); //para refrescar la foto
			$oVista->formulario($oAlumno);
		}
		if (isset($_GET['editar_alumno'])) {
			$oAlumno->leer( $_GET['id']);
			$oVista->formulario($oAlumno);
		}
	}
	
}
$oControlador = new ControladorAlumnos($_POST);