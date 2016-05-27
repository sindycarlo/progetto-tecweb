function valida_commento(){


	//se settati svuoto gli span di errore
	if (document.getElementById("err_commento") !== "") {
	    document.getElementById("err_commento").innerHTML = "";
	}

	var commento = document.getElementById("form_commento").value;	
        var nome=document.getElementById("user").value;

        
	//Effettua il controllo sui campi, se sono vuoti o composti da soli spazi
	if (!commento.replace(/^\s+/g, '').length  || !nome.replace(/^\s+/g, '').length || (commento === "Inserisci un commento")) {
            document.getElementById("err_commento").innerHTML = "Il campo nome e il commento sono obbligatori*";
	    document.getElementById("form_commento").focus();
	    document.getElementById("form_commento").select();
	    return false;
	}
	else { 
            return true;
	}
}
