<form action= <?PHP echo $_SERVER['PHP_SELF']; ?> method="POST">
        <label for="departamento">Departamento:</label>
        <select id="departamento" name="departamento">
            <option value="INFORMÁTICA">INFORMÁTICA</option>
            <option value="LENGUA">LENGUA</option>
            <option value="MATEMÁTICAS">MATEMÁTICAS</option>
        <option value="INGLÉS">INGLÉS</option>
        </select>  
        <input type="submit" value="Enviar" /> 
    </form>
<?php
    if (isset($_REQUEST['departamento'])) {
        $departamento = isset($_REQUEST['departamento']) ? $_REQUEST['departamento'] : "";
        $departamentos = isset($_REQUEST['departamentos']) ? $_REQUEST['departamentos'] : "";
        switch ($departamento){
            case "INFORMÁTICA":
                $presupuesto = 500;
                break;
            case "LENGUA":
                $presupuesto = 300;
                break;
            case "MATEMÁTICAS":
                $presupuesto = 300;
                break;
            case "INGLÉS":
                $presupuesto = 400;
                break;
            default:
                echo "departamento incorrecto: $departamento";
                break;
        }
        echo "<h2> el presupuesto de $departamento es $presupuesto euros</h2>";
       
    }
?>
    
