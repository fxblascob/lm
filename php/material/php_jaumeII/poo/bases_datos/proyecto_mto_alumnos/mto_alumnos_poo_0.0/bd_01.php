<?php 
include "./bd_lib.php";

class Alumno {
	public $sql, $id, $nombre, $apellidos, $anyo, $curso, $grupo, $aula, $numord,$oBD=null;
	public function Alumno($id) {
		$this->sql="select * from alumnos   where id = ". $id."  order by id asc limit 1";
		$this->oBD = new BaseDatos();
		$rows = $this->oBD->consultaSQL($this->sql);
		$this->mapear_datos($rows);
	}
	public function primero(){
		$this->sql="select * from alumnos  order by id limit 1";
		$this->mapear_datos($this->oBD->consultaSQL($this->sql));
	}
	public function ultimo(){
		$this->sql="select * from alumnos  order by id desc limit 1";
		$this->mapear_datos($this->oBD->consultaSQL($this->sql));
	}
	public function siguiente($id){
		$this->sql="select * from alumnos   where id > ". $id."  order by id asc limit 1";
		$this->mapear_datos($this->oBD->consultaSQL($this->sql));
	}
	public function anterior($id){
		$this->sql = "select * from alumnos   where id < ". $id." order by id desc limit 1";
		$this->mapear_datos($this->oBD->consultaSQL($this->sql));
	}
	public function mapear_datos($rows) {
		if (!is_null($rows))
			foreach ($rows as $row) {
					$this->id =$row['id']; $this->nombre =$row['nombre'];  $this->apellidos=$row['apellidos']; $this->anyo      =$row['anyo']; $this->curso     =$row['curso'];	$this->grupo    =$row['grupo']; $this->numord =$row['numord']; $this->aula =$row['aula'];break;}
		else  {$this->id =""; $this->nombre =""; $this->apellidos=""; $this->anyo ="";	$this->curso ="";$this->grupo="";	$this->numord ="";	 $this->aula="";}
	}
	public function borrar($id) {
		if  ($this->oBD->insertDeleteSQL("delete from alumnos where id = ".$id) >0) 		?>	<script>	window.alert("<?php  	echo "se han borrado " .$this->oBD->afected. " alumnos " ?>")       </script>	<?php
		$this->mapear_datos(null);
	}
	public function insertar() {
		$sql="insert into alumnos (id,nombre,apellidos,anyo,curso,grupo,numord,aula) values ";
		$sql = $sql."(".$this->id.",'".$this->nombre."','".$this->apellidos."','".$this->anyo."','".$this->curso."','".$this->grupo."',".$this->numord.",".$this->aula.")";
		if ($this->oBD->insertDeleteSQL($sql) >0) 	?>	<script>	window.alert("<?php  	echo "se han insertado " .$this->oBD->afected. " alumnos " ?>")       </script>	<?php
	}
	public function modificar() {
		$sql = "UPDATE alumnos	SET ";
		$sql = $sql . "nombre  = ' ".$this->nombre." ' ";
		$sql = $sql . ",apellidos = ' ".$this->apellidos." ' ";
		$sql = $sql . ",anyo = ' ".$this->anyo." ' ";
		$sql = $sql . ",curso = ' ".$this->curso." ' ";
		$sql = $sql . ",grupo = ' ".$this->grupo." ' ";
		$sql = $sql . ",aula = ' ".$this->aula." ' ";
		$sql = $sql . ",numord = ' ".$this->numord." ' ";
		$sql = $sql . " WHERE id = ' ".$this->id." ' ";

		if ($this->oBD->insertDeleteSQL($sql) > 0) 	?>	<script>	window.alert("<?php  	echo "se han modificado " .$this->oBD->afected. " alumnos " ?>")       </script>	<?php
	}
}
class MantenimientoAlumnos {
	public $alu = null;
	public function MantenimientoAlumnos($id) {
		$this->alu = new Alumno($id);
	}
	public function mostrar_datos_tabla($filas) {
		print "<table border = '1'  align='center'>";
			$this->alu->oBD->cabecera_tabla($filas);
			foreach ($filas as $fila) {
				print "<tr>"; 
				foreach ($fila as $elem)	
					print "<td>".$elem."</td>";
				print "<td>";
					print '<a href=bd_01.php?id='.$fila["id"].'&nombre='.urlencode($fila["nombre"]).'&apellidos='.urlencode($fila["apellidos"]).'&anyo='.$fila["anyo"].'&curso='.$fila["curso"].'&grupo='.$fila["grupo"].'&aula='.$fila["aula"].'&numord='.$fila["numord"].'&editar_alumno=si'.'>[Editar]</a>';
				print "</td>";
				print "<td>";
					print '<a href=bd_01.php?id='.$fila["id"].'&borrar_alumno=si'.'>[Borrar]</a>';
				print "</td>";
				print "</tr>"; 
			}
		print "</table>";
	}
	public function mostrar_datos_matriz($filas) {
		print "<pre>";
		print_r($filas);
		print "</pre>";
	}
	public function formularioSQL() { 
		include "./bd_01_form2.php";
	}
}

	$omalu = new MantenimientoAlumnos(isset($_POST['id']) ? $_POST['id'] :  (isset($_GET['id']) ? $_GET['id'] :  ""));

	if  ( 	!isset($_POST['enviar']) && !isset($_POST['primero']) &&  !isset($_POST['siguiente']) && !isset($_POST['ultimo']) &&  !isset($_POST['anterior']) &&  !isset($_POST['insertar'])  && !isset($_POST['borrar']) && !isset($_POST['modificar'])&& !isset($_GET['editar_alumno']) && !isset($_GET['borrar_alumno']))
		$omalu->formularioSQL();
	
	if (isset($_POST['cadena_sql'])) {
		$omalu->alu->sql=$_POST['cadena_sql'];
		$omalu->formularioSQL();
		if ($rows=$omalu->alu->oBD->consultaSQL($omalu->alu->sql)) {
			if (isset($_POST['salida']) && $_POST['salida']==1)  $omalu->mostrar_datos_matriz($rows);
			if (isset($_POST['salida']) && $_POST['salida']==2)  $omalu->mostrar_datos_tabla($rows);
		}
	}
	if (isset($_POST['primero']) || isset($_POST['ultimo']) || isset($_POST['siguiente']) || isset($_POST['anterior']) ) {
		$id = (isset($_POST['id']) ? $_POST['id'] :  "");
		if (isset($_POST['primero'])) $omalu->alu->primero();
		if (isset($_POST['ultimo']))    $omalu->alu->ultimo();
		if (isset($_POST['siguiente'])) $omalu->alu->siguiente($id);
		if (isset($_POST['anterior'])) $omalu->alu->anterior($id);
		$omalu->formularioSQL();
	}
	if (isset($_POST['borrar']) || isset($_GET['borrar_alumno'])) {
		$id = (isset($_POST['id']) ? $_POST['id'] :  $_GET['id']);
		$omalu->alu->borrar($id);
		$omalu->formularioSQL();
	}
	if (isset($_POST['insertar']) || isset($_POST['modificar']) || isset($_GET['editar_alumno'])) {
		$omalu->alu->id            = (isset($_POST['id']) ? $_POST['id'] :  $_GET['id']);
		$omalu->alu->nombre  = (isset($_POST['nombre']) ? $_POST['nombre'] :  $_GET['nombre']);
		$omalu->alu->apellidos = (isset($_POST['apellidos']) ? $_POST['apellidos'] :  $_GET['apellidos']);
		$omalu->alu->anyo       = (isset($_POST['anyo']) ? $_POST['anyo'] :  $_GET['anyo']);
		$omalu->alu->curso      = (isset($_POST['curso']) ? $_POST['curso'] :  $_GET['curso']);
		$omalu->alu->grupo     = (isset($_POST['grupo']) ? $_POST['grupo'] :  $_GET['grupo']);
		$omalu->alu->numord  = (isset($_POST['numord']) ? $_POST['numord'] :  $_GET['numord']);
		$omalu->alu->aula        = (isset($_POST['aula']) ? $_POST['aula'] :  $_GET['aula']);
		
		if (isset($_POST['insertar'])) $omalu->alu->insertar();
		if (isset($_POST['modificar']) || isset($_POST['editar_alumno'])) $omalu->alu->modificar();
		$omalu->formularioSQL();
	}
?>