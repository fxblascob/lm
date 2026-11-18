<?php
class BaseDatos {
	private $baseDatos="videoclub",$servidor="127.0.0.1", $usuariobd="mochuelo", $contrasenyabd="mochuelo";
	private $ftp_server="127.0.0.1";
	private $ftp_user_name="lliurex";
	private $ftp_user_pass  ="lliurex";
	protected $objPDO = null, $rows=null, $error=null, $afected=0;
	protected $ruta_caratulas="../alu/caratulas/";
	protected $ruta_peliculas="../alu/peliculas/";
	
	public function __construct() {
		try {
			$this->objPDO = new PDO("mysql:dbname=".$this->baseDatos.";charset=utf8mb4;host=".$this->servidor, $this->usuariobd,$this->contrasenyabd);
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
	public function cabecera_tabla($filas) {
		foreach ($filas as $fila)  {
			print "<tr>";
			foreach ($fila as $indice => $elemento) 	print "<td>$indice</td>";
			print "</tr>";
			break;
		}
	}
	public function subir_fichero_ftp($source_file,$destination_file) {
		$conn_id = ftp_connect($this->ftp_server); 
		$login_result = ftp_login($conn_id, $this->ftp_user_name, $this->ftp_user_pass); 
		if ((!$conn_id) || (!$login_result)) {  
		    echo "¡La conexión FTP ha fallado!";
		    echo "Se intentó conectar al $this->ftp_server por el usuario $this->ftp_user_name"; 
		    exit; 
		} else echo "Conexión a $this->ftp_server realizada con éxito, por el usuario $this->ftp_user_name"; 
		$upload = ftp_put($conn_id, $destination_file, $source_file, FTP_BINARY);  
		if (!$upload)       echo "¡La subida FTP ha fallado!";
		else    echo "Subida de $source_file a $this->ftp_server como $destination_file";	
		ftp_close($conn_id);
	}
}
?>