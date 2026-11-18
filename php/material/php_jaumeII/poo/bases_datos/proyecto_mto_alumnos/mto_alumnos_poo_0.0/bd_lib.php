<?php

// version POO

class BaseDatos {
	public $db="alumnos",$host="127.0.0.1", $user="alumno", $pass="alumno", $objPDO = null, $rows=null, $error=null, $afected=0;
	public function BaseDatos() {
		try {
			$this->objPDO = new PDO("mysql:dbname=".$this->db.";charset=utf8mb4;host=".$this->host, $this->user,$this->pass);
		} catch (PDOException $e) { 
			$this->error = 'Fallo en la conexion ' . $e->getMessage(); 
			print $this ->error;
		}
	}
	
	public function consultaSQL($sql){
		$this->rows=null;
		if ($this->objPDO) {
			if ($objPDOStatement = $this->objPDO->query($sql)) {
				//$rows = $objPDOStatement->fetchAll();
				$this->rows = $objPDOStatement->fetchAll(PDO::FETCH_ASSOC);
			}
		}
		return($this->rows);
	}
	public function InsertDeleteSQL($sql){
		$this->afected=0;
		if ($this->objPDO) {
			$this->afected = $this->objPDO->exec($sql);
			if ($this->afected==0) {
				$this->error= $this->objPDO->errorInfo();
				print ("ERROR ". $this->error[2]);
			}
		}
		return ($this->afected);
	}
	public function cabecera_tabla($filas) {
		foreach ($filas as $fila)  {
			print "<tr>";
			foreach ($fila as $indice => $elemento) 	print "<td>$indice</td>";
			print "</tr>";
			break;
		}
	}
}

?>