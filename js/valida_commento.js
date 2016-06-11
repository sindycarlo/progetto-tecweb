function valida_commento(){



	var commento = document.getElementById("commento").value;	
        var nome=document.getElementById("user").value;

        
	//Effettua il controllo sui campi, se sono vuoti o composti da soli spazi
	if (!nome.replace(/^\s+/g, '').length ){
            document.getElementById("err_user").innerHTML = "Il campo nome è obbligatorio*";
	    document.getElementById("user").focus();
	    return false;
	}else
	if(!commento.replace(/^\s+/g, '').length){
		      document.getElementById("err_commento").innerHTML = "Il campo commento è obbligatorio*";
	    document.getElementById("commento").focus();
	    return false;
	
	}


	else { 
            return true;
	}
}
