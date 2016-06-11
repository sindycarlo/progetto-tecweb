
function valida_campi(){




	var username = document.getElementById("username").value;	
        var password=document.getElementById("password").value;
        
        if (!username.replace(/^\s+/g, '').length)
        {
           document.getElementById("err_username").innerHTML = "il campo username è obligatorio*";
           document.getElementById("username").focus();
           return false;
	}
	else 
		if( !password.replace(/^\s+/g, '').length){

			document.getElementById("err_password").innerHTML = "il campo password è obligatorio*";
			document.getElementById("password").focus();
           return false;
		}
		else

	//Finiti i controlli do l'ok
                return true;
		
}
