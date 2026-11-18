<?php
	
	include "./bd_lib.php";
	include "./bd_01_form.php";

	$sql = isset($_GET['sql'])  ? $_GET['sql'] : "select * from alumnos"; 
	$salida = isset($_GET['salida'])  ? $_GET['salida'] : "1"; 
	formularioSQL($sql,$salida);
	if (isset($_GET['enviar'])) {		
		$rows = ejecutarSQL($sql);
		if ($rows) {
			if  ($_GET['salida'] == 1) {
				echo "<pre>";
				print_r ($rows);
				echo "</pre>";
				
			}else {
				$i = 0;
				echo "<table align='center'>";
				echo cabecera_tabla($rows);
				foreach ($rows as $row)  {
					$i++;
					if  (($i%2)==0)		echo "<tr>";
					else echo "<tr bgColor='orange'>";
					foreach ($row as $campo) {
						 echo "<td>",$campo,"</td>";
					}
					echo "</tr>";
				}
				echo "</table>";
			}
			
		}
	}
?>