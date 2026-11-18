<?php
function conectarDB(){
	$db="ies";
	$host="localhost";
	$user="root";
	$pass="";
	$link = null;
	try {
		$link = new PDO("mysql:dbname=".$db.";charset=utf8mb4;host=".$host, $user,$pass);
	} catch (PDOException $e) { 
		print 'Fallo en la conexion' . $e->getMessage(); 
	}
	return($link);
}
function ejecutarSQL($sql){
	$rows=null;
	if ($objPDO=conectarDB()) {
		if ($objPDOStatement = $objPDO->query($sql)) {
			//$rows = $objPDOStatement->fetchAll();
			$rows = $objPDOStatement->fetchAll(PDO::FETCH_ASSOC);
		}
	}
	return($rows);
}
function cabecera_tabla($filas) {
	foreach ($filas as $fila)  {
		print "<tr>";
		foreach ($fila as $indice => $elemento) 	print "<td>$indice</td>";
		print "</tr>";
		break;
	}
}
function Insert_delete_SQL($sql){
	if ($objPDO=conectarDB()) {
		$afected = $objPDO->exec($sql);
		if ($afected==0) {
			$error= $objPDO->errorInfo();
			if ($error) print ("ERROR  ".$sql ."-->". $error[2]);
		}
		return ($afected);
	}
	return(0);
}
?>