function ocultarMenu(){
    if (document.getElementById("if").style.display=="none"){
        document.getElementById("if").style.display="inline";
        document.getElementById("contenedor_cuerpo").style.width="88%"
    }else{
        document.getElementById("if").style.display="none";
        document.getElementById("contenedor_cuerpo").style.width="99%"
    }
}