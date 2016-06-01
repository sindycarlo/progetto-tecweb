function valida_campi(){
	//se settati svuoto gli span di errore
	if (document.getElementById("err_proponi") !== "") {
	    document.getElementById("err_proponi").innerHTML = "";
	}
	var nomepiatto = document.getElementById("n_piatto").value;	
	var nomeauthore = document.getElementById("n_author").value;
	var descrizione = document.getElementById("n_desc").value;
	var tempoprep = document.getElementById("n_tempo").value;
	var numpersone = document.getElementById("n_persone").value;
	var procedimento = document.getElementById("n_proc").value;

	//controllo se ciasscun campo è vuoto oppure ci sono degli spazi:	

	if(!nomepiatto.replace(/^\s+/g, '').length) {
            document.getElementById("err_proponi").innerHTML = "Il campo  \"Nome piatto\" e' obbligatorio!";
	    document.getElementById("err_proponi").focus();
	    return false;
	} 
	
	if (!nomeauthore.replace(/^\s+/g, '').length) {
            document.getElementById("err_proponi").innerHTML = "Il campo \"Autore\" e' obbligatorio!";
	    document.getElementById("err_proponi").focus();
	    return false;
	}
	
	if (!descrizione.replace(/^\s+/g, '').length) {
            document.getElementById("err_proponi").innerHTML = "Il campo \"Descrizione\" e' obbligatorio!";
	    document.getElementById("err_proponi").focus();
	    return false;
	}
	
	if (!tempoprep.replace(/^\s+/g, '').length) {
            document.getElementById("err_proponi").innerHTML = "Il campo \"Tempo di Preparazione\" e' obbligatorio!";
	    document.getElementById("err_proponi").focus();
	    return false;
	}
	
	if (!numpersone.replace(/^\s+/g, '').length) {
            document.getElementById("err_proponi").innerHTML = "Il campo \"Numero Persone\" e' obbligatorio!";
	    document.getElementById("err_proponi").focus();
	    return false;
	}
	
	if (!procedimento.replace(/^\s+/g, '').length) {
            document.getElementById("err_proponi").innerHTML = "Il campo \"Procedimento\" e' obbligatorio!";
	    document.getElementById("err_proponi").focus();
	    return false;
	}
	
	var areaIngredienti = document.getElementById("n_ingr").value;
	var arrayIngredienti = areaIngredienti.split("\n");
	var arrayLength = arrayIngredienti.length;

	for(var i=0; i < arrayLength; i++)
	{
		var currentIng = arrayIngredienti[i];
		var rigaLength = currentIng.length;
		var ultimoChar = currentIng.charAt(rigaLength - 1);
		if(ultimoChar != ";")
		{	
			document.getElementById("err_proponi").innerHTML = "Il campo \"Ingredienti\" è errato! Controlla di aver aggiunto un ; al termine di ogni riga!";
			document.getElementById("err_proponi").focus();
			return false;
		}	
	} 
 	
        return true;
}
//Last update by Luca 01/06/2016
//Solo correzioni minori (pulizia del codice)
