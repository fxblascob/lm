<?php
/*
    Crea una página llamada 06_manejo_textos.php. Realiza en ella las siguientes operaciones:

    Crea una variable $radio con un radio de circunferencia (el que quieras).
    Crea una variable $area y calcula en ella el área del círculo, como has hecho en algún ejercicio anterior (PI * radio2, definiendo la constante PI).
    Crea una variable $textoResultado que diga “El área calculada del círculo es” y luego ponga la variable $area, mostrando sólo 2 decimales (utiliza la función number_format). Muestra luego esta variable por pantalla con un echo.
    Crea una variable $textoResultadoMayus que convierta el texto anterior a mayúsculas, usando la función strtoupper. Muestra también esta variable por pantalla.
    Crea una variable llamada $textoResultadoModificado que reemplace la palabra “calculada” por la palabra “obtenida”, usando la función str_replace, en la variable $textoResultado.
    Averigua la longitud del texto de la variable anterior usando la función strlen.
    Averigua en qué posición del texto de la variable anterior se encuentra la palabra “círculo”, usando la función strpos.
    Crea una variable $numeros que tenga el valor “1,2,3,4,5”, y utiliza la función explode para quedarte con los números por separado. Sácalos por pantalla, separados por el signo “+” (“1+2+3+4+5”), y después, intenta sumarlos entre sí y mostrar el resultado de la suma a continuación (al final, te quedará algo como “1+2+3+4+5=15”).
*/
   
    define("PI",3.1416);
    $radio = 10;
    $area = PI * $radio + $radio;
    $textoResultado = "<p>El área calculada del circulo de radio $radio es ".number_format($area,2);
    echo "<p>".$textoResultado;

    $textoResultadoMayus = strtoupper($textoResultado);
    echo '<p>'.$textoResultadoMayus;

    $textoResultadoModificado = str_replace("calculada","obtenida",$textoResultado);
    echo ( "<p>".$textoResultadoModificado);

    echo "<p>la longitud de la variable anterior es: ".strlen($textoResultadoModificado);

    echo "<p>la palabra 'circulo' se encuentra en la posición ".strpos($textoResultadoModificado,'circulo');
    
    $textoNumeros = "1,2,3,4,5";
    $numeros = explode(',',$textoNumeros);
    $textoNumeros = implode('+',$numeros);
    $suma=0;
    foreach($numeros as $numero)
        $suma += $numero;
    echo "<p>la suma de $textoNumeros es: $suma";
?>