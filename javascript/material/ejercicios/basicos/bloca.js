//function keypressed() {alert(" Las teclas no funcionan ");}
//document.onkeydown=keypressed;


var message="No funciona ";
function clickIE() {
	if (document.all) {
		(message);
		return false;
	}
}
function clickNS(e) {
	if(document.layers||(document.getElementById&&!document.all)) {
		if (e.which==2||e.which==3) {
				(message);
				return false;
		}
	}
}

if (document.layers) 		{
	document.captureEvents(Event.MOUSEDOWN);
	document.captureEvents(Event.ONDRAGSTART);
	document.onmousedown=clickNS;
}
else	{
	document.onmouseup=clickNS;
	document.oncontextmenu=clickIE;

}

document.oncontextmenu=new Function("return false")

function izquierda(e) {
	if (navigator.appName == 'Netscape' && (e.which == 1 || e.which == 2)){
		//alert('Botón izquierdo inhabilitado')
		return false;
	}
	else if (navigator.appName == 'Microsoft Internet Explorer' && (event.button == 1)){
		//alert('Botón izquierdo inhabilitado')
	}
}
//document.onmousedown=izquierda


