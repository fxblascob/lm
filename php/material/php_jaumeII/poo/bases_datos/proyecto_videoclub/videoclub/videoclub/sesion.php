<?php 
include "./mochuelo_lib.php";

class Sesion  extends BaseDatos{
	public $codigo,$usuario,$password,$tipousuario;
	
	public function leer($usuario,$password) {
		$this->sql="select * from clientes   where usuario = '". $usuario."' and password = '".$password."'  order by codigo asc limit 1";
		$this->mapear($this->consulta($this->sql));
	}
	
}
class ContrSesion extends Sesion{
	
	public function pantalla() { 
		?>
		<table width="45%" border="1" align="center">          
			<tr align='center'>
				<td colspan='2'>
					<h1 align="center">ACCESO AL SISTEMA </h1><br>
				</td>
			</tr>
					<form name="form1" method="post" action="<?php echo $_SERVER['PHP_SELF'] ?>">		
							<tr>
								<td>
									Usuario:<input type = 'text' name= 'usuario' size='10'  >	<br>
									Password:<input type = 'text' name= 'password' size='10' >
								</td>
							</tr>
							<tr align ="center">
								<td>				
									<input type="submit" name="enviar" value="Aceptar">
								</td>
							</tr>
					</form>
					
				
			
			</tr>
		</table>

		<?php
	}
	public function control() {
		if  (!isset($_POST['enviar']) )
			$this->pantalla();
		else {
			$this->leer($_POST['usuario'],$_POST['password']);
			print("<pre>");
			print_r($this);
			print("</pre>");
		}
	}
}

session_start();
$oContrSesion = new ContrSesion();
$oContrSesion->control();

?>