
function valida_campi(){



  var errore = "err_login";
   //estraggo tutte le variabili:
   var nomepiatto = document.getElementById("n_piatto").value;   
   var nomeautore=document.getElementById("n_author").value;
   var descrizione = document.getElementById("n_desc").value;   
   var tempo=document.getElementById("n_tempo").value;
   var numpersone=document.getElementById("n_persone").value;
   var procedura=document.getElementById("n_proc").value;
         


///verifico che i campi non abbiano caratteri speciali:



   var  regexp= /!@#$%^&*()+=-[]\\\';,.{}|\":<>?/;//controllo espressione regolare caratteri speciali


        if ((regexp.test(n_piatto) || regexp.test(n_author) || regexp.test(n_desc) || regexp.test(n_tempo) || regexp.test(n_persone)
         || regexp.test(n_proc)))
        {
           document.getElementById(errore).innerHTML = "non sono accettati caratteri speciali*";
           return false;
   }
   else if(!nomepiatto.replace(/^\s+/g, '').length  || !nomeautore.replace(/^\s+/g, '').length || !descrizione.replace(/^\s+/g, '').length
   			|| !tempo.replace(/^\s+/g, '').length || !numpersone.replace(/^\s+/g, '').length || !procedura.replace(/^\s+/g, '').length)
  
   			{
   				document.getElementById(errore).innerHTML = "tutti i campi sono obbligatori*";
           	return false;
   			}
   			else {//tutti i controlli sono stati effettuati
   					return true;
   			}



   
}
