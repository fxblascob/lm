<?php function formularioSQL($sql,$id,$nombre,$apellidos,$anyo,$curso,$grupo,$numord,$aula) { ?>
			<table width="100%" border="1" align="center">          
				<tr align='center'>
					<td colspan='2'><h1 align="center">ACCESO A DATOS CON PHP </h1><br>
						Introduce la cadena SQL: 
					</td>
				
				</tr>
				<tr align='center' >
					
					<td >
						<form name="form1" method="post" action="<?php echo $_SERVER['PHP_SELF'] ?>">		
							<table width='100%' height='100%'  border>
								<tr><td>
									ID:<input type = 'text' name= 'id' size='4' value='<?php echo $id ?>'>
									Nombre:<input type = 'text' name= 'nombre' size='10' value='<?php echo $nombre ?>'>
									Apellidos:<input type = 'text' name= 'apellidos'  size='15'  value='<?php echo $apellidos ?>'>
								</td></tr>
								<tr><td>
									Curso:<input type = 'text' name= 'curso' size='6'  value='<?php echo $curso ?>'>
									Grupo:<input type = 'text' name= 'grupo' size='2'  value='<?php echo $grupo ?>'>
									Anyo:<input type = 'text' name= 'anyo' size='9'  value='<?php echo $anyo ?>'>
								</td></tr>
								<tr><td>
									Num Ord:<input type = 'text' name= 'numord' size='2'  value='<?php echo $numord ?>'>	
									Aula:<input type = 'text' name= 'aula' size='2'  value='<?php echo $aula ?>'>
								</td></tr>
								<tr><td>				
									<input type="submit" name="primero" value="<<">
									<input type="submit" name="anterior" value=" < ">
									<input type="submit" name="siguiente" value=" > ">
									<input type="submit" name="ultimo" value=">>">
									<input type="submit" name="insertar" value="Ins">
									<input type="submit" name="modificar" value="edit">
									<input type="submit" name="borrar" value="delete">
									<input type="submit" name="limpiar" value="clear">
									<input type="submit" name="buscar" value="buscar">

								</td></tr>
							</table>
						</form>
						
					
					</td>
					<td >
						<form name="form2" method="post" action="<?php echo $_SERVER['PHP_SELF'] ?>">
							<table width='100%'  height='100%'  border>
								<tr><td>
									<textarea name="cadena_sql" rows=10 cols=40 ><?php echo $sql ?></textarea>
								</td></tr>
								<tr><td>
									Formato de salida:
									<label>  <input type  ="radio" name="salida" value="1">                matriz  </label>
									<label>  <input type  ="radio"  name="salida"value ="2" checked  >tabla   </label>
									<input type="submit" name="enviar" value="enviar">
								</td></tr>
							</table>
						</form>
					</td>
				</tr>
			</table>
		</form>
<?php } ?>