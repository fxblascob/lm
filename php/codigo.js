function hacerclic(){
    var p = document.querySelector("#contenedor_cuerpo p:first-child");
    if (p) {
        p.onclick = mostraralerta;
    }
}
function mostraralerta() {
    alert("hizo clic");
}
window.onload = hacerclic;
