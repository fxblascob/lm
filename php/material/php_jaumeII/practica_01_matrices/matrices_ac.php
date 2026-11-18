<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8" />
<title></title>
</head>
<body>
<?php
 	if(isset($_POST['dim'])) $dim = $_POST['dim'];else $dim=0;
	if(isset($_POST['suma'])) $operacion="+";
	else if(isset($_POST['resta'])) $operacion="-";
		  else if(isset($_POST['producto'])) $operacion="*";
			else if(isset($_POST['traspuesta'])) $operacion="traspuesta";
		  		 else $operacion="";
?>
 <table >
 
 <tr><td colspan='2'><h1>Calculadora de matrices</h1></td></tr>
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
		Dimensión de las matrices cuadradas:<br>
		<input type="text" name="dim" value ="<?php  echo $dim; ?>" ><br>
	</td>
	 </form>
</tr>
</table>

<?php
	function leer_matriz(&$m1,$n) {
		for ($i=1;$i<=$n;$i++)	{
			for ($j=1;$j<=$n;$j++)	{
				$m1[$i][$j] = rand (0,10);			
			}	
		}
	}
	
	function escribir_matriz($m,$n){
		echo "<table cellpadding=3 cellspacing=3 border=1  bgcolor='#E5E5E5' >";
			for ($i=1;$i<=$n;$i++)	{
					if (($i % 2)== 0 ) echo "<tr bgColor='green'>";else "<tr>";
					for ($j=1;$j<=$n;$j++)	{
						echo "<td>";
						echo $m[$i][$j];
						echo "</td>";
					}
					echo "</tr>";
			}	
			echo "</table>";
	}
	function escribir_matrices($m1,$m2,$mr,$operacion,$n) {
		echo "<table cellpadding=3 cellspacing =3 >";
			echo "<tr><td>";	
			escribir_matriz($m1,$n); 
			echo "</td>";	
			echo "<td valign='center'>".$operacion."</td>";
			echo "<td>";
			if ($operacion != 'traspuesta') escribir_matriz($m2,$n);
			echo "</td>";
			echo "<td valign='center'>=</td>";
			echo "<td>";
			escribir_matriz($mr,$n);
			echo "</td></tr>";
		echo "</table>";
		
	}
	function sumar_matrices($m1,$m2,&$mr,$n) {
		for ($i=1;$i<=$n;$i++)	{
			for ($j=1;$j<=$n;$j++)	{
				$mr[$i][$j] = $m1[$i][$j]+$m2[$i][$j];		
			}	
		}
	}
	function restar_matrices($m1,$m2,&$mr,$n) {
		for ($i=1;$i<=$n;$i++)	{
			for ($j=1;$j<=$n;$j++)	{
				$mr[$i][$j] = $m1[$i][$j]-$m2[$i][$j];		
			}	
		}
	}
	function traspuesta($m1,&$mr,$n) {
		for ($i=1;$i<=$n;$i++)	{
			for ($j=1;$j<=$n;$j++)	{
				$mr[$j][$i] = $m1[$i][$j]	;
			}	
		}
	}
	function multiplicar_matrices($m1,$m2,&$mr,$n) {
		for ($i=1;$i<=$n;$i++)	{
			for ($j=1;$j<=$n;$j++)	{
				$temporal=0;
				for ($k=1;$k<=$n;$k++)    
					$temporal = $temporal*1.0 + $m1[$i][$k] * $m2[$k][$j];
				$mr[$i][$j] = $temporal ;			
			}	
		}     
	}
	if ($dim>0) {
		leer_matriz($m1,$dim);
		leer_matriz($m2,$dim);
		if ($operacion=="+") {
			sumar_matrices($m1,$m2,$mr,$dim);
			escribir_matrices($m1,$m2,$mr,$operacion,$dim);
		}
		if ($operacion=="-"){
			restar_matrices($m1,$m2,$mr,$dim);
			escribir_matrices($m1,$m2,$mr,$operacion,$dim);
		}
		if ($operacion=="*") {
			multiplicar_matrices($m1,$m2,$mr,$dim);
			escribir_matrices($m1,$m2,$mr,$operacion,$dim);
		}
		if ($operacion=="traspuesta") {
			traspuesta($m1,$mr,$dim);
			escribir_matrices($m1,$mr,$mr,$operacion,$dim);
		}
		
	}

?>
</body>
</html>