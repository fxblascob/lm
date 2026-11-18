<?php

class CalculadoraMatrices {
		public $m1 = null;
		public $m2 = null;
		public $mr = null;

		public function __construct($dim) {
			$this->m1=$this->leer_matriz($dim);
			$this->m2=$this->leer_matriz($dim);
		}
		private function leer_matriz($dim) {
			$m=null;
			for ($i=1;$i<=$dim;$i++)	{
				for ($j=1;$j<=$dim;$j++)	{
					$m[$i][$j] = rand (0,10);			
				}	
			}
			return $m;
		}
		public function sumar_matrices($dim) {
			for ($i=1;$i<=$dim;$i++)	{
				for ($j=1;$j<=$dim;$j++)	{
					$this->mr[$i][$j] = $this->m1[$i][$j]+$this->m2[$i][$j];		
				}	
			}
		}
		public function restar_matrices($dim) {
			for ($i=1;$i<=$dim;$i++)	{
				for ($j=1;$j<=$dim;$j++)	{
					$this->mr[$i][$j] = $this->m1[$i][$j]-$this->m2[$i][$j];		
				}	
			}
		}
		public function traspuesta($dim) {
			for ($i=1;$i<=$dim;$i++)	{
				for ($j=1;$j<=$dim;$j++)	{
					$this->mr[$j][$i] = $this->m1[$i][$j]	;
				}	
			}
		}
		public function multiplicar_matrices($dim) {
			for ($i=1;$i<=$dim;$i++)	{
				for ($j=1;$j<=$dim;$j++)	{
					$temporal=0;
					for ($k=1;$k<=$dim;$k++)    
						$temporal = $temporal*1.0 + $this->m1[$i][$k] * $this->m2[$k][$j];
					$this->mr[$i][$j] = $temporal ;			
				}	
			}     
		}
}
class Vista {
	private function escribir_matriz($m,$dim){
			echo "<table style='2px solid black' >";
				for ($i=1;$i<=$dim;$i++)	{
					if (($i % 2)== 0 ) echo "<tr bgColor='green'>";else "<tr>";
						for ($j=1;$j<=$dim;$j++)	{
							echo "<td>";	echo $m[$i][$j];	echo "</td>";
						}
					echo "</tr>";
				}	
			echo "</table>";
		}
	public function escribir_matrices($m1,$m2,$mr,$dim,$operacion) {
			if ($dim>0) {
				echo "<table cellpadding=3 cellspacing =3 >";
				echo "<tr><td>";	
				$this->escribir_matriz($m1,$dim); 
				echo "</td>";	
				echo "<td valign='center'>".$operacion."</td>";
				echo "<td>";
				if ($operacion != 'traspuesta') $this->escribir_matriz($m2,$dim);
				echo "</td>";
				echo "<td valign='center'>=</td>";
				echo "<td>";
				$this->escribir_matriz($mr,$dim);
				echo "</td></tr>";
				echo "</table>";
			}
		}
	public function formulario ($dim) {
		?>
			 <table >
				 <tr><td colspan='2'><h1>Calculadora  de matrices-</h1></td></tr>
				 <tr>
					 <form method="post" action="<?php echo $_SERVER['PHP_SELF']; ?>">
					 <td>
						<input type="submit" name="suma"         value="suma        ">
						<br>
						<input type="submit" name="resta"          value="resta        ">
						<br>
						<input type="submit" name="producto"    value="producto  ">
						<br>
						<input type="submit" name="traspuesta" value="traspuesta"><br>
					</td>
					 <td>
						Dimensi&oacute;n de las matrices cuadradas:<br>
						<input type="text" name="dim" value ="<?php  echo $dim; ?>" ><br>
					</td>
					 </form>
				</tr>
			</table>

		<?php
	}
}
class Controlador {
	public function __construct($array) {
		$dim=0;
		$op="";
		if (isset($array['dim'])) $dim = $array['dim']; else $dim = 0;
		if (isset($array['suma'])) $op = "+"; 
		if (isset($array['resta'])) $op = "-";
		if (isset($array['producto'])) $op = "*";
		if (isset($array['traspuesta'])) $op = "traspuesta";
		
		$oVista = new Vista($dim);
		$oVista->formulario($dim);
		
		if ($dim > 0 && $op != "")  {
			$oCalc = new CalculadoraMatrices($dim);
			if ($op =="+")  		$oCalc->sumar_matrices($dim);
			if ($op =="-")  		$oCalc->restar_matrices($dim);
			if ($op =="*") 		$oCalc->multiplicar_matrices($dim);
			if ($op =="traspuesta")   $oCalc->traspuesta($dim);
			$oVista->escribir_matrices($oCalc->m1,$oCalc->m2,$oCalc->mr,$dim,$op);
		}
	}
}

$oControlador = new Controlador($_POST)

?>
