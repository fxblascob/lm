	<script>
		function nombre(fic) {
			fic = fic.split('\\');
			alert(fic[fic.length-1]);
			return(fic[fic.length-1]);
			
		}
	</script>
	<table width="100%" border="1" align="center">          
		<tr align='center'>
			<td colspan='2'>
				<h1 align="center">MANTENIMIENTO DE PRODUCTOS </h1><br>
			</td>
		</tr>
		<tr align='center' >
			<td >
				<form name="form1" enctype="multipart/form-data"  method="post" action="<?php echo $_SERVER['PHP_SELF'] ?>">		
					<table width='100%' height='100%'  border>
						<tr><td>
							Codigo:<input type = 'text' name= 'codigo' size='4' value='<?php echo $this->codigo ?>'>
							Tipo prod:<input type = 'text' name= 'tipo_producto' size='4' value='<?php echo $this->tipo_producto ?>'>
							Titulo:<input type = 'text' name= 'titulo'  size='15'  value='<?php echo $this->titulo ?>'>
						</td></tr>
						<tr><td>
														
							Genero:<input type = 'text' name= 'genero' size='20'  value='<?php echo $this->genero ?>'>
							Subgenero: <input type= 'text' name= 'subgenero' size='20'  value='<?php echo $this->subgenero ?>'>
						</td></tr>
						<tr >
							<td  >
								Pelicula:<input type = 'file' name= 'fichero_ruta'    > 
								<br>
								<a href='<?php echo $this->ruta ?>' ><?php echo $this->ruta ?></a>
								<br>
								Caratula:<input type = 'file' name= 'fichero_caratula'   accept='image/*'  >	
								<br>
							
							
								<a href='<?php echo $this->caratula ?>' ><?php echo $this->caratula ?></a>
							</td>
							<td colspan="2">
								 <a href='<?php echo $this->caratula ?>' ><?php echo $this->mostrar_caratula($this->codigo) ?> </a>
							</td>
						</tr>
						<tr><td>				
							<input type="submit" name="primero" value="<<">
							<input type="submit" name="anterior" value=" < ">
							<input type="submit" name="siguiente" value=" > ">
							<input type="submit" name="ultimo" value=">>">
							<input type="submit" name="insertar" value="Ins">
							<input type="submit" name="modificar" value="edit">
							<input type="submit" name="borrar" value="del">

						</td></tr>
					</table>
				</form>
				
			
			</td>
			<td >
				Introduce la cadena SQL: 
				<form name="form2" method="post" action="<?php echo $_SERVER['PHP_SELF'] ?>">
					<table width='100%'  height='100%'  border>
						<tr><td>
							<textarea name="cadena_sql" rows=10 cols=40 ><?php echo $this->sql ?></textarea>
						</td></tr>
						<tr><td>
							<input type="submit" name="enviar" value="enviar">
						</td></tr>
					</table>
				</form>
			</td>
		</tr>
	</table>
</form>