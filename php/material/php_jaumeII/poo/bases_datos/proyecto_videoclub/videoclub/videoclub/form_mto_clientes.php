				<table width="100%" border="1" align="center">          
					<tr align='center'>
						<td colspan='2'>
							<h1 align="center">MANTENIMIENTO DE CLIENTES </h1><br>
						</td>
					</tr>
					<tr align='center' >
						<td >
							<form name="form1" method="post" action="<?php echo $_SERVER['PHP_SELF'] ?>">		
								<table width='100%' height='100%'  border>
									<tr><td>
										Codigo:<input type = 'text'  name= 'codigo' size='4' value='<?php echo $this->codigo ?>' >
										Nombre:<input type = 'text' name= 'nombre' size='10' value='<?php echo $this->nombre ?>'>
										Apellidos:<input type = 'text' name= 'apellidos'  size='15'  value='<?php echo $this->apellidos ?>'>
									</td></tr>
									<tr><td>
										DNI:<input type = 'text' name= 'dni' size='10'  value='<?php echo $this->dni ?>'>
										Direccion:<input type = 'text' name= 'direccion' size='50'  value='<?php echo $this->direccion ?>'>
										num_tarjeta: <input type= 'text' name= 'num_tarjeta' size='19'  value='<?php echo $this->num_tarjeta ?>'>
									</td></tr>
									<tr><td>
										Usuario:<input type = 'text' name= 'usuario' size='10'  value='<?php echo $this->usuario ?>'>	
										Password:<input type = 'text' name= 'password' size='10'  value='<?php echo $this->password ?>'>
										Tipo usuario:<input type = 'text' name= 'tipousuario' size='5'  value='<?php echo $this->tipousuario ?>'>
									</td></tr>
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