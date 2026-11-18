<?php
/*
    Ejercicio 8:
    Crea una página llamada 08_comprueba_hora.php en tu carpeta de ejercicios. 
    crea una variable de texto con una hora en ella (por ejemplo, “21:30:12”), 
    y luego procésala para extraer por separado la hora, el minuto y el segundo, 
    y comprobar si es una hora válida. Por ejemplo, la hora anterior sí debería ser válida, 
    pero si ponemos “12:63:11” no debería serlo, porque 63 no es un minuto válido.
*/
   
$hora = "15:59:00";
if (preg_match("/^([0-1][0-9]|[2][0-3]):([0-5][0-9]):([0-5][0-9])$/", $hora, $partes) == 1)
{
    echo "<p>La hora completa es " . $partes[0];
    echo "<p>Hora " . $partes[1];
    echo "<p>Minutos " . $partes[2];
    echo "<p>Segundos" . $partes[3];	
} else {
    echo "Formato de hora no válido";
}
?>