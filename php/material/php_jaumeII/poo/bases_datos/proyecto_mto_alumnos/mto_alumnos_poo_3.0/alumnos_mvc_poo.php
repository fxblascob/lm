<?php
class BaseDatos {
	private $db="alumnos";
	private $host="localhost";
	private $user="root";
	private $pass="";
	public $sql="select * from alumnos";
	protected $objPDO = null, $rows=null, $error=null, $afected=0;
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
				//$rows = $objPDOStatement->fetchAll();
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
				if ($this->objPDO->lastInsertId()>0 ) $this->codigo = $this->objPDO->lastInsertId();
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
class Alumno extends BaseDatos {
	public $id, $nombre,$apellidos,$curso,$grupo,$anyo,$numord,$aula,$foto="";
	//public $RUTA_FOTOS="./img/";
	//public $RUTA_FOTOS=".\\img\\";
	public $RUTA_FOTOS=".".DIRECTORY_SEPARATOR."img".DIRECTORY_SEPARATOR;
	public function mapear($rows) {
		parent::mapear($rows);
		if ($this->id >0)  {
			foreach (glob($this->RUTA_FOTOS.$this->id.".*") as $nombre_fichero) {
				if ($nombre_fichero) $this->foto=  $nombre_fichero;
				else $this->foto = "";
			}
		}
		
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
		$nborrados=$this->ejecucion("delete from alumnos where id = ".$id);
		if  ($nborrados>0) {
			?>	<script>	window.alert("<?php  	echo "se han borrado " .$nborrados. " alumnos " ?>")       </script>	<?php
		}
	}
	function insertar() {
		$sql="insert into alumnos (nombre,apellidos,anyo,curso,grupo,numord,aula) values ";
		$sql = $sql."('".$this->nombre."','".$this->apellidos."','".$this->anyo."','".$this->curso."','".$this->grupo."',".$this->numord.",".$this->aula.")";
		//echo $sql;
		$ninsertados= $this->ejecucion($sql);
		if ($ninsertados>0) {
			?>	<script>	window.alert("<?php  	echo "se han insertados " .$ninsertados. " alumnos " ?>")       </script>	<?php
		}

	}
	function modificar() {
		$sql = "UPDATE alumnos	SET ";
		$sql = $sql . "nombre  =  '".$this->nombre."'  ";
		$sql = $sql . ",apellidos = ' ".$this->apellidos." ' ";
		$sql = $sql . ",anyo = ' ".$this->anyo." ' ";
		$sql = $sql . ",curso = ' ".$this->curso." ' ";
		$sql = $sql . ",grupo = ' ".$this->grupo." ' ";
		$sql = $sql . ",aula = ' ".$this->aula." ' ";
		$sql = $sql . ",numord = ' ".$this->numord." ' ";
		$sql = $sql . " WHERE id = ' ".$this->id." ' ";
		
		//echo $sql;
		$ninsertados= $this->ejecucion($sql);
		if ($ninsertados>0) {
			?>	<script>	window.alert("<?php  	echo "se han modificado " .$ninsertados. " alumnos " ?>")       </script>	<?php
		}

	}

}
class VistaAlumnos {
	public function mostrar_datos_tabla($filas) {
		print "<table border = '1'  align='center'>";
			$this->cabecera_tabla($filas);
			foreach ($filas as $fila) {
				print "<tr>"; 
				foreach ($fila as $elem)	
					print "<td>".$elem."</td>";
			
				print "<td>";
					print '<a href=alumnos_mvc_poo.php?id='.$fila["id"].'&editar_alumno=si'.'>[Editar]</a>';
				print "</td>";
				print "<td>";
					print '<a href=alumnos_mvc_poo.php?id='.$fila["id"].'&borrar_alumno=si'.'>[Borrar]</a>';
				print "</td>";
				print "</tr>"; 
			}
		print "</table>";
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
		$template = file_get_contents('./alumnos_mvc_poo.html');
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
		}
		if (isset($_POST['ultimo'])) {
			$oAlumno->ultimo();
			$oVista->formulario($oAlumno);
		}

		if (isset($_POST['siguiente'])) {
			$oAlumno->id=$miarray['id'];
			$oAlumno->siguiente();
			$oVista->formulario($oAlumno);
		}
		if (isset($_POST['anterior'])) {
			$oAlumno->id=$miarray['id'];
			$oAlumno->anterior();
			$oVista->formulario($oAlumno);
		}
		if (isset($_POST['borrar']) || isset($_GET['borrar_alumno'])) {
			$id = (isset($_POST['id']) ? $_POST['id'] :  $_GET['id']);
			$oAlumno->borrar($id);
			$oVista->formulario($oAlumno);
		}
		if (isset($_POST['insertar']) || isset($_POST['modificar'])) {
			$oAlumno->mapear($_POST);
			if (isset($_POST['insertar'])) $oAlumno ->insertar();
			else  $oAlumno->modificar();
			$oVista->formulario($oAlumno);
		}
		if (isset($_GET['editar_alumno'])) {
			$oAlumno->leer( $_GET['id']);
			$oVista->formulario($oAlumno);
		}
	}
}
$oControlador = new ControladorAlumnos($_POST);