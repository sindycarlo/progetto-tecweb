
function valida_campi(){


  var errore = "err_email";


  //se settati svuoto gli span di errore
  if (document.getElementById(errore) !== "") {
      document.getElementById(errore).innerHTML = "";
  }

  var nome = document.getElementById("nome").value; 
  var email=document.getElementById("email").value;      
  var quesion = document.getElementById("question").value; 

        
        if (!nome.replace(/^\s+/g, '').length || !email.replace(/^\s+/g, '').length  || !question.replace(/^\s+/g, '').length)
        {
           document.getElementById(errore).innerHTML = "tutti i campi sono obbligatori*";
           return false;
  }
  else if(/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(email))  
         {  
            return true

         }else 
           { document.getElementById(errore).innerHTML = "indirizzo email non valido*";
            return false 
            }
      

       return true 
}
