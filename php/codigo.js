function hacerclic(){
    document.querySelector("#contenedor_cuerpo p:first-clild").onclick=mostraralerta;
   
}
function mostraralerta() {
    alert("hizo clic");
}
window.onload=hacerclic;
