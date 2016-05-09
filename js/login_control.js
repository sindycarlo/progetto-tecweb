
function valida_campi(){


	var errore = "err_login";

	//se settati svuoto gli span di errore
	if (document.getElementById(errore) !== "") {
	    document.getElementById(errore).innerHTML = "";
	}

	var username = document.getElementById("username").value;	
        var password=document.getElementById("password").value;
        
        if (!username.replace(/^\s+/g, '').length || !password.replace(/^\s+/g, '').length)
        {
           document.getElementById(errore).innerHTML = "tutti i campi sono obbligatori.";
           return false;
	}
	else { //Finiti i controlli do l'ok
                return true;
	}
}

function caratterispecial()
{

var iChars = "!@#$%^&*()+=-[]\\\';,./{}|\":<>?";
var errore = "err_proponi";

//se settati svuoto gli span di errore
	if (document.getElementById(errore) !== "") {
	    document.getElementById(errore).innerHTML = "";
	}

var nomepiatto = document.getElementById("n_piatto").value;	
var autore=document.getElementById("n_author").value;
var  brevedesc= document.getElementById("n_desc").value;	
var tempoprep=document.getElementById("n_tempo").value;
var numpersone = document.getElementById("n_persone").value;	
var procedimento=document.getElementById("n_proc").value;

	if (iChars.indexOf(autore) != -1)
     {
        document.getElementById(errore).innerHTML = "il campo nomePiatto contiene caratteri speciali. Rimuovili e riprova";
        return false;
    }
    if (iChars.indexOf(autore) != -1) {
        document.getElementById(errore).innerHTML = "il campo Autore contiene caratteri speciali. \n Rimuovili e riprova";
        return false;
    }
    if (iChars.indexOf(brevedesc) != -1) {
        document.getElementById(errore).innerHTML = "il campo breve descrizione contiene caratteri speciali. \n Rimuovili e riprova";
        return false;
    }
    if (iChars.indexOf(tempoprep) != -1) {
        document.getElementById(errore).innerHTML = "il campo tempo preparazione contiene caratteri speciali. \n Rimuovili e riprova";
        return false;
    }
    if (iChars.indexOf(numpersone) != -1) {
        document.getElementById(errore).innerHTML = "il campo numero persone contiene caratteri speciali. \n Rimuovili e riprova";
        return false;
    }
    if (iChars.indexOf(procedimento) != -1) {
        document.getElementById(errore).innerHTML = "il campo procedimento contiene caratteri speciali. \n Rimuovili e riprova";
        return false;
    }
    {
    return true;}

}
