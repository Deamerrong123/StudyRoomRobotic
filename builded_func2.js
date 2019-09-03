{/* <script type="text/javascript"> */}
function ajaxAuthenticate(){
		var xmlHttp;
		try{
			// Firefox, Opera 8.0+, Safari
			xmlHttp=new XMLHttpRequest();
		}
		catch (e){
			// Internet Explorer
			try{
				xmlHttp=new ActiveXObject("Msxml2.XMLHTTP");
			}
			catch (e){
				try{
					xmlHttp=new ActiveXObject("Microsoft.XMLHTTP");
				}
				catch (e){
					alert("Your browser does not support AJAX!");
					return false;
				}
			}
		}
		
		xmlHttp.onreadystatechange=function(){
			if(xmlHttp.readyState==4){
				var xmldoc = xmlHttp.responseXML;
				var authenticated = xmldoc.getElementsByTagName('authenticated')[0].firstChild.nodeValue;
				var errormessage = xmldoc.getElementsByTagName('errormessage')[0].firstChild;
				
				if(authenticated == "false"){
					if(errormessage.nodeValue == "No such object") errormessage.nodeValue = "Incorrect username or password.";
                                        else if (errormessage.nodeValue == "binderr")
                                               {
					         errormessage.nodeValue = "</br>Your account can not be found. Please verify your Baruch Username and Password and try again." +
                                                       "</br></br><a target=\"_blank\" href=\"http://www.baruch.cuny.edu/bctc/username/BaruchUsername.htm\">Forgot your Baruch Username? </a>" +
                                                       "</br><a target=\"_blank\" href=\"http://www.baruch.cuny.edu/bctc/username/pin_faq.html\">Need Help with your Password? </a>";
                                               }
                                        else if (errormessage.nodeValue == "No Such User")
                                               {
					         errormessage.nodeValue = "</br>Your account can not be found. Please verify your Baruch Username and Password and try again." +
                                                       "</br></br><a target=\"_blank\" href=\"http://www.baruch.cuny.edu/bctc/username/BaruchUsername.htm\">Forgot your Baruch Username? </a>" +
                                                       "</br><a target=\"_blank\" href=\"http://www.baruch.cuny.edu/bctc/username/pin_faq.html\">Need Help with your Password? </a>";
                                               }
					document.getElementById('errormessage').style.visibility = "visible";
					document.getElementById('errormessage').innerHTML = ("<strong>LOGIN ERROR </br><\/strong>" + errormessage.nodeValue);
				}
				else{
					window.location.href = "index.php";
				}
			}
		}
		
		urlstring = "or-authenticate.php";

                var enc_passwd = encodeURI(document.getElementById("authentication").password.value);
		params = "username=" + document.getElementById("authentication").username.value + "&password=" + enc_passwd + "&ajax_indicator=TRUE";
		
		xmlHttp.open("POST",urlstring,true);
		xmlHttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");	
		xmlHttp.send(params);
	}
	
	function init(){
		document.getElementsByTagName('input')[0].focus();
	}
	
	window.onload = init;
	
// </script>