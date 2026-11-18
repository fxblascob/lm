<?php 
class Vista {
	public function formulario($num,$base,$exp,$result){
		?>
		<form action="" method="post">
			<table>
				<tr>
					<td>
						<input type="submit" value="Factorial" name="factorial">
					</td>
					<td>
						Iterativo:<input type="radio" value="iterativo" checked name ="metodo">
						Recursivo:<input type="radio" value="recursivo"  name ="metodo">
					</td>
				</tr>
				<tr>
					<td>
						<input type="submit" value="Potencia" name="potencia">
					</td>
					<td>
						Número:<input type="text" name="num" value="<?php echo $num ?>">
					</td>
				</tr>
				<tr>
					<td>
						<input type="submit" value="Fibonacci" name="fibonacci">
					</td>
					<td>
						Base: <input type="text" name="base" value="<?php echo $base ?>">
						Exponente: <input type="text" name="exp" value="<?php echo $exp ?>">
					</td>
				</tr>
				<tr>
					<td>
						Resultado:
					</td>
					<td>
						<?php echo $result ?>
					</td>
				</tr>

		</form>
		
		<?php
	}
}
class Mates {
	
	public function factorial_iterativo($num) {
		$result=1;
		if ($num<1)
			for ($i=$num; $i<=-1; $i++) $result= $result*$i;
		else
			for ($i=$num; $i>=1; $i--) $result= $result*$i;
		return($result);
	}
	public function factorial_recursivo($num) {
		if ($num==1) return 1;
		elseif ($num == -1) return -1;
		elseif ($num < -1)  return $num * $this->factorial_recursivo($num+1);
		else return $num * $this->factorial_recursivo($num-1);
	}
	public function potencia_iterativo($base,$exp) {
		if ($exp==0)  return(1);
		$result=$base;
		for ($i=$exp; $i>1; $i--) $result= $result*$base;
		return($result);
	}
	public function potencia_recursivo($base,$exp) {
		if ($exp==0) return(1);
		if ($exp==1) return($base);
		return($base * $this->potencia_recursivo($base , $exp-1));
	}
	public function fibonacci_iterativo($num) {
		$res1=0;
		$res2=1;
		for ($i=0; $i<=$num-2; $i++) {
			$res2 = $res1+$res2;
			$res1 = $res2 - $res1; 
		}
		return($res2);
	}
	public function fibonacci_recursivo($num) {
		if ($num==1) return 1;
		if ($num==0) return 0;
		else return ($this->fibonacci_recursivo($num-1) +  $this->fibonacci_recursivo($num-2));
	}
}
class Controlador {
	public $oMates = null;
	public $oVista = null;
	public $num = "", $base = "", $exp = "", $result = "";
	public  function __construct( $miarray) {
		
		$this->num = (isset($miarray['num'])) ? $miarray['num'] : "";
		$this->base = (isset($miarray['base'])) ? $miarray['base'] : "";
		$this->exp = (isset($miarray['exp'])) ? $miarray['exp'] : "";
		
		$this->oVista = new Vista();
		$this->oMates = new Mates();
		
		if (isset($miarray['factorial'])) {
			if (isset($miarray['metodo']) && $miarray['metodo']=="iterativo") {
				$this->result=$this->oMates->factorial_iterativo($this->num);
				$this->oVista->formulario($this->num,$this->base,$this->exp,$this->result);
			}else {
				$this->result=$this->oMates->factorial_recursivo($this->num);
				$this->oVista->formulario($this->num,$this->base,$this->exp,$this->result);
			}
		}elseif (isset($miarray['potencia'])) {
			if (isset($miarray['metodo']) && $miarray['metodo']=="iterativo") {
				$this->result=$this->oMates->potencia_iterativo($this->base,$this->exp);
				$this->oVista->formulario($this->num,$this->base,$this->exp,$this->result);			
			}else{
				$this->result=$this->oMates->potencia_recursivo($this->base,$this->exp);
				$this->oVista->formulario($this->num,$this->base,$this->exp,$this->result);
			} 
		}elseif (isset($miarray['fibonacci'])) {
			if (isset($miarray['metodo']) && $miarray['metodo']=="iterativo") {
				$this->result=$this->oMates->fibonacci_iterativo($this->num);
				$this->oVista->formulario($this->num,$this->base,$this->exp,$this->result);
			}else {
				$this->result=$this->oMates->fibonacci_recursivo($this->num);
				$this->oVista->formulario($this->num,$this->base,$this->exp,$this->result);
			}
		}else $this->oVista->formulario($this->num,$this->base,$this->exp,$this->result);
	}
	
}

$oControlador = new Controlador($_POST);
