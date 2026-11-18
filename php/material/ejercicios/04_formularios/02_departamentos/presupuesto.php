<?php
   function presupuesto($depto) {
        if ($depto == "INFORMÁTICA") return(500);
        if ($depto == "LENGUA")      return(300);
        if ($depto == "MATEMÁTICAS") return(300);
        if ($depto == "INGLÉS")      return(400);
        return(0);
    }

    $departamento = isset($_REQUEST['departamento']) ? $_REQUEST['departamento'] : "";
    $departamentos = isset($_REQUEST['departamentos']) ? $_REQUEST['departamentos'] :Array();
    $total = 0;
    $dep = "";
    $cantidad = count($departamentos);
    if ($cantidad > 0 ){
        for ($i = 0; $i < $cantidad; $i++) {
            if ($i == $cantidad - 1 && $cantidad > 1 )   $dep .= " Y ";
            if ($i < $cantidad - 1 && $cantidad > 1 && $i > 0)    $dep .=  ", ";
            $dep .= $departamentos[$i];
            $total += presupuesto($departamentos[$i]);       
        }
    }
    
    
    echo "<h2> el presupuesto de $departamento  es ".presupuesto($departamento)." euros</h2>";
    echo "<h2> el presupuesto de $dep es $total euros</h2>";
    