function valida_campi(){
	if (document.getElementById("err_proponi") !== "") 
	{
	    document.getElementById("err_proponi").innerHTML = "";
	}
	
	var nomepiatto = document.getElementById("n_piatto").value;	
	var nomeauthore = document.getElementById("n_author").value;
	var descrizione = document.getElementById("n_desc").value;
	var tempoprep = document.getElementById("n_tempo").value;
	var numpersone = document.getElementById("n_persone").value;
	var procedimento = document.getElementById("n_proc").value;

	if(!nomepiatto.replace(/^\s+/g, '').length) {
            document.getElementById("err_proponi").innerHTML = "Il campo  nome piatto e' obbligatorio*";
	    document.getElementById("n_piatto").focus();
	    document.getElementById("n_piatto").select();
	    return false;
	} 

	if (!nomeauthore.replace(/^\s+/g, '').length) {
            document.getElementById("err_proponi").innerHTML = "Il campo autore e' obbligatorio*";
	    document.getElementById("n_author").focus();
	    document.getElementById("n_author").select();
	    return false;
	}

	if (!descrizione.replace(/^\s+/g, '').length) {
            document.getElementById("err_proponi").innerHTML = "Il campo descrizione e' obbligatorio*";
	    document.getElementById("n_desc").focus();
	    document.getElementById("n_desc").select();
	    return false;
	}

	if (!tempoprep.replace(/^\s+/g, '').length) {
            document.getElementById("err_proponi").innerHTML = "Il campo tempo preparazione e' obbligatorio*";
	    document.getElementById("n_tempo").focus();
	    document.getElementById("n_tempo").select();
	    return false;
	}

	if (!numpersone.replace(/^\s+/g, '').length) {
            document.getElementById("err_proponi").innerHTML = "Il campo numero persone e' obbligatorio*";
	    document.getElementById("n_persone").focus();
	    document.getElementById("n_persone").select();
	    return false;
	}

	if (!procedimento.replace(/^\s+/g, '').length) {
            document.getElementById("err_proponi").innerHTML = "Il campo procedimento e' obbligatorio*";
	    document.getElementById("n_proc").focus();
	    document.getElementById("n_proc").select();
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
			document.getElementById("err_proponi").innerHTML = "campo ingredienti errato, controlla di aver aggiunto un ; al termine di ogni riga!";
			return false;
		}	
	} 

	return true;
}
 
//Last update by Luca 26/05/2016
