<?php
   function presupuesto($depto) {
        if ($depto == "INFORMÁTICA") return(500);
        if ($depto == "LENGUA")      return(300);
        if ($depto == "MATEMÁTICAS") return(300);
        if ($depto == "INGLÉS")      return(400);
        return(0);
    }

    $departamento = isset($_REQUEST['departamento']) ? $_REQUEST['departamento'] : "";

    echo "<h2> el presupuesto de $departamento  es ".presupuesto($departamento)." euros</h2>";
    