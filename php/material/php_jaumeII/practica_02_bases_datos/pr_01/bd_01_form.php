<?php function formularioSQL($sql,$salida) { ?>
		<form name="form1" method="get" action="<?php echo $_SERVER['PHP_SELF'] ?>">
			<table width="50%" border="1" align="center">          
				<tr align='center'>
					<td><h1 align="center">ACCESO A DATOS CON PHP </h1><br>
						Introduce la cadena SQL: 
					</td>
				</tr>
				<tr align='center'>
					<td><textarea name="sql" rows=10 cols=80 ><?php echo $sql ?></textarea></td>
				</tr>
				<tr align='center'>
					<td> Formato de salida:
						<label>  <input type  ="radio" name="salida" value="1"  <?php if ($salida == "1") echo "checked";?> >matriz  </label>
						<label>  <input type  ="radio"  name="salida"value ="2" <?php if ($salida == "2") echo "checked";?> >tabla   </label>

						<input type="submit" name="enviar" value="enviar">
					</td>
				</tr>
			</table>
		</form>
<?php } ?>