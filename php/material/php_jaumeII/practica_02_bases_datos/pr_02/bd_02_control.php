<?php 
include "./bd_lib.php";
include "./bd_02_form.php";


function mostrar_datos_tabla($filas) {
	print "<table border = '1'  align='center'>";
		cabecera_tabla($filas);
		foreach ($filas as $fila) {
			print "<tr>"; 
			foreach ($fila as $elem)	
				print "<td>".$elem."</td>";
			print "<td>";
				print '<a href="bd_02_control.php?id='.$fila["id"].'&editar_alumno=si'.'>[Editar]</a>';
			print "</td>";
			print "<td>";
				print '<a href=bd_02_control.php?id='.$fila["id"].'&borrar_alumno=si'.'>[Borrar]</a>';
			print "</td>";
			print "</tr>"; 
		}
	print "</table>";
}

function mostrar_datos_matriz($filas) {
	print "<pre>";
	print_r($filas);
	print "</pre>";
}
function mapear_datos($rows,&$id,&$nombre,&$apellidos,&$anyo,&$curso,&$grupo,&$numord,&$aula) {
	foreach ($rows as $row) {
			$id          =$row['id'];
			$nombre =$row['nombre'];
			$apellidos=$row['apellidos'];
			$anyo      =$row['anyo'];
			$curso     =$row['curso'];
			$grupo    =$row['grupo'];
			$numord =$row['numord'];
			$aula       =$row['aula'];
			break;
	}
}

function buscar($nombre,$apellidos){
	$rows=ejecutarSQL("select * from alumnos  where apellidos like '%$apellidos%' and nombre like '%$nombre%'" );
	if ($rows) 	mostrar_datos_tabla($rows);
}
function primero(&$id,&$nombre,&$apellidos,&$anyo,&$curso,&$grupo,&$numord,&$aula){
	$rows=ejecutarSQL("select * from alumnos  order by id limit 1");
	if ($rows) 	mapear_datos($rows,$id,$nombre,$apellidos,$anyo,$curso,$grupo,$numord,$aula);
}
function ultimo(&$id,&$nombre,&$apellidos,&$anyo,&$curso,&$grupo,&$numord,&$aula){
	$rows=ejecutarSQL("select * from alumnos  order by id desc limit 1");
	if ($rows) 	mapear_datos($rows,$id,$nombre,$apellidos,$anyo,$curso,$grupo,$numord,$aula);
}
function siguiente(&$id,&$nombre,&$apellidos,&$anyo,&$curso,&$grupo,&$numord,&$aula){
	$sql="select * from alumnos   where id > ". $id."  order by id asc limit 1";
	$rows=ejecutarSQL($sql);
	if ($rows) 	mapear_datos($rows,$id,$nombre,$apellidos,$anyo,$curso,$grupo,$numord,$aula);
	
}
function anterior(&$id,&$nombre,&$apellidos,&$anyo,&$curso,&$grupo,&$numord,&$aula){
	$sql = "select * from alumnos   where id < ". $id." order by id desc limit 1";
	$rows=ejecutarSQL($sql);
	if ($rows) 	mapear_datos($rows,$id,$nombre,$apellidos,$anyo,$curso,$grupo,$numord,$aula);
}
function borrar($id) {
	$nborrados=Insert_delete_SQL("delete from alumnos where id = ".$id);
	if  ($nborrados>0) {
		?>	<script>	window.alert("<?php  	echo "se han borrado " .$nborrados. " alumnos " ?>")       </script>	<?php
	}
}
function insertar(&$id,&$nombre,&$apellidos,&$anyo,&$curso,&$grupo,&$numord,&$aula) {
	$sql="insert into alumnos (nombre,apellidos,anyo,curso,grupo,numord,aula) values ";
	$sql = $sql."('".$nombre."','".$apellidos."','".$anyo."','".$curso."','".$grupo."',".$numord.",".$aula.")";
	//echo $sql;
	$ninsertados= Insert_delete_SQL($sql);
	if ($ninsertados>0) {
		?>	<script>	window.alert("<?php  	echo "se han insertados " .$ninsertados. " alumnos " ?>")       </script>	<?php
	}

}
function modificar(&$id,&$nombre,&$apellidos,&$anyo,&$curso,&$grupo,&$numord,&$aula) {
	$sql = "UPDATE alumnos	SET ";
	$sql = $sql . "nombre  =  '".$nombre."'  ";
	$sql = $sql . ",apellidos = ' ".$apellidos." ' ";
	$sql = $sql . ",anyo = ' ".$anyo." ' ";
	$sql = $sql . ",curso = ' ".$curso." ' ";
	$sql = $sql . ",grupo = ' ".$grupo." ' ";
	$sql = $sql . ",aula = ' ".$aula." ' ";
	$sql = $sql . ",numord = ' ".$numord." ' ";
	$sql = $sql . " WHERE id = ' ".$id." ' ";
	
	//echo $sql;
	$ninsertados= Insert_delete_SQL($sql);
	if ($ninsertados>0) {
		?>	<script>	window.alert("<?php  	echo "se han modificado " .$ninsertados. " alumnos " ?>")       </script>	<?php
	}

}



	if  ( 	!isset($_POST['enviar']) && !isset($_POST['primero']) &&     !isset($_POST['siguiente']) && !isset($_POST['ultimo']) &&       !isset($_POST['anterior']) &&  !isset($_POST['anterior']) && 	!isset($_POST['insertar'])  && !isset($_POST['borrar']) && !isset($_POST['modificar'])&& !isset($_GET['editar_alumno']) && !isset($_GET['borrar_alumno']) && !isset($_POST['limpiar']))
		formularioSQL("","",""."","","","","","","");

	if (isset($_POST['enviar']) ) {
		$sql=$_POST['cadena_sql'];
		formularioSQL($sql,"","",""."","","","","","","");
		if ($rows=ejecutarSQL($sql)) {
			if (isset($_POST['salida']) && $_POST['salida']==1)  mostrar_datos_matriz($rows);
			if (isset($_POST['salida']) && $_POST['salida']==2)  mostrar_datos_tabla($rows);
		}
	}
	
	if (isset($_POST['buscar'])) {
		//formularioSQL("","",""."","","","","","","");
		buscar($_POST['nombre'],$_POST['apellidos']);
		
	}
	if (isset($_POST['limpiar'])) {
		formularioSQL("","",""."","","","","","","");
	}
	if (isset($_POST['primero'])) {
		primero($id,$nombre,$apellidos,$anyo,$curso,$grupo,$numord,$aula);
		formularioSQL("",$id,$nombre,$apellidos,$anyo,$curso,$grupo,$numord,$aula);
	}
	if (isset($_POST['ultimo'])) {
		ultimo($id,$nombre,$apellidos,$anyo,$curso,$grupo,$numord,$aula);
		formularioSQL("",$id,$nombre,$apellidos,$anyo,$curso,$grupo,$numord,$aula);
	}

	if (isset($_POST['siguiente'])) {
		$id = $_POST['id'];
		siguiente($id,$nombre,$apellidos,$anyo,$curso,$grupo,$numord,$aula);
		formularioSQL("",$id,$nombre,$apellidos,$anyo,$curso,$grupo,$numord,$aula);
	}
	if (isset($_POST['anterior'])) {
		$id = $_POST['id'];
		anterior($id,$nombre,$apellidos,$anyo,$curso,$grupo,$numord,$aula);
		formularioSQL("",$id,$nombre,$apellidos,$anyo,$curso,$grupo,$numord,$aula);
		
	}
	if (isset($_POST['borrar']) || isset($_GET['borrar_alumno'])) {
		$id = (isset($_POST['id']) ? $_POST['id'] :  $_GET['id']);
		borrar($id);
		formularioSQL("select * from alumnos","",""."","","","","","","");
	}
	if (isset($_POST['insertar']) || isset($_POST['modificar'])) {
		if (isset( $_POST['id'])) 		$id=$_POST['id'];
		if (isset( $_POST['nombre'])) 	$nombre=$_POST['nombre'];
		if (isset( $_POST['apellidos'])) 	$apellidos=$_POST['apellidos'];
		if (isset( $_POST['anyo'])) 		$anyo=$_POST['anyo'];
		if (isset( $_POST['curso']))		$curso=$_POST['curso'];
		if (isset( $_POST['grupo'])) 	$grupo=$_POST['grupo'];
		if (isset( $_POST['numord'])) 	$numord=$_POST['numord'];
		if (isset( $_POST['aula'])) 		$aula=$_POST['aula'];
		
		if (isset($_POST['insertar'])) insertar($id,$nombre,$apellidos,$anyo,$curso,$grupo,$numord,$aula);
		else  modificar($id,$nombre,$apellidos,$anyo,$curso,$grupo,$numord,$aula);
		formularioSQL("select * from alumnos",$id,$nombre,$apellidos,$anyo,$curso,$grupo,$numord,$aula);
	}
	if (isset($_GET['editar_alumno'])) {
		if (isset( $_GET['id'])) 		$id=$_GET['id'];
		if (isset( $_GET['nombre'])) 	$nombre=$_GET['nombre'];
		if (isset( $_GET['apellidos'])) 	$apellidos=$_GET['apellidos'];
		if (isset( $_GET['anyo'])) 		$anyo=$_GET['anyo'];
		if (isset( $_GET['curso']))		$curso=$_GET['curso'];
		if (isset( $_GET['grupo'])) 	$grupo=$_GET['grupo'];
		if (isset( $_GET['numord'])) 	$numord=$_GET['numord'];
		if (isset( $_GET['aula'])) 		$aula=$_GET['aula'];
		
		//if (isset($_POST['insertar'])) insertar($id,$nombre,$apellidos,$anyo,$curso,$grupo,$numord,$aula);
		//else  modificar($id,$nombre,$apellidos,$anyo,$curso,$grupo,$numord,$aula);
		formularioSQL("select * from alumnos",$id,$nombre,$apellidos,$anyo,$curso,$grupo,$numord,$aula);
	}
?>