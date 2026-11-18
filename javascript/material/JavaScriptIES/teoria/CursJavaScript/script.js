	function CreateWindow(Tittle, Width, Height) {
		var htmlpage = " ";
		var win_opt = "toolbar=0, location=0, directories=0, status=0,";
		win_opt += "menubar=0, scrollbars=0, resizable=0, copyhistory=0,";
		win_opt += "width=" + Width + ",height=" + Height;		// Crear una nueva ventana
		NewWindow = window.open("","Tittle",win_opt);
		// Generación del contenido de la página		
		NewWindow.document.open();
		htmlpage += "<HTML><HEAD><TITLE>" + Tittle + "</TITLE>";
		htmlpage += "</HEAD>";
		htmlpage += "<BODY background='bg1.jpg'>"; 
		htmlpage += "<h3><p>Este ha sido el resultado del programa Hola mundo.<br></h3>";
		htmlpage += "<h2>Su c&oacute;digo fuente es:</h2>";
		htmlpage += "<HR>";
		htmlpage += "<tt>";
		htmlpage += "&lt;SCRIPT language='JavaScript'&gt;<br>";
		htmlpage += "document.write('Hola mundo.')<br>";
		htmlpage += "&lt;/SCRIPT&gt;";
		htmlpage += "</tt>";
		htmlpage += "<p><hr>";
		htmlpage += "<FORM><CENTER>";
		htmlpage += "<INPUT type='button' value=' Cerrar ' onClick='close()'>";
		htmlpage += "</CENTER></FORM>";
		htmlpage += "</BODY></HTML>";		
		NewWindow.document.write(htmlpage);
		NewWindow.document.close();	
	}
