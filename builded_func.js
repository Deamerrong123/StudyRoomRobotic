{/* <script language="javascript" type="text/javascript"> */}
	//findPos(object)
	//Returns position of object for use with dayview popup
	//Source: http://www.quirksmode.org/js/findpos.html
	function findPos(obj){
			var curleft = curtop = 0;
			if(obj.offsetParent){
				do{
					curleft += obj.offsetLeft;
					curtop += obj.offsetTop;
				}while(obj = obj.offsetParent);
				return [curleft,curtop];
			}
	}

	
	function showPopUp(obj,content){
		var popup = document.getElementById("popup");
		popup.style.visibility = "visible";
		popup.style.display = "inline";
		var popleft = (findPos(obj)[0] + ((obj.width/3)*2));
		var poptop = (findPos(obj)[1] + ((obj.height/3)*2));
		//determine browser window width
		var myWidth = 0, myHeight = 0;
		if( typeof( window.innerWidth ) == 'number' ) {
			//Non-IE
			myWidth = window.innerWidth;
			myHeight = window.innerHeight;
		} else if( document.documentElement && ( document.documentElement.clientWidth || document.documentElement.clientHeight ) ) {
			//IE 6+ in 'standards compliant mode'
			myWidth = document.documentElement.clientWidth;
			myHeight = document.documentElement.clientHeight;
		} else if( document.body && ( document.body.clientWidth || document.body.clientHeight ) ) {
			//IE 4 compatible
			myWidth = document.body.clientWidth;
			myHeight = document.body.clientHeight;
		}
		//limit is the width of the browser window minus the width of the popup
		var limit = myWidth - popup.clientWidth -20;
		//If popup is too far to the right, shift it left by its width
		if(popleft >= limit){
			popleft = popleft - popup.clientWidth;
		}
		popup.style.left = popleft + "px";
		popup.style.top = poptop + "px";
		//popup.innerHTML = "<div id=\"popupClose\"><span onClick=\"closePopUp()\">Close<\/span><\/div>" + content;
		popup.innerHTML = content;
	}
	
	function showPopUpReserve(obj,roomname,time_str,group,altusernamestr,roomid,currentmdyandtime,capacity,maxdur,durationhtml,capacity_string,optionalfields_string){
		var popup = document.getElementById("popup");
		popup.style.visibility = "visible";
		popup.style.display = "inline";
		var popleft = (findPos(obj)[0] + ((obj.width/3)*2));
		var poptop = (findPos(obj)[1] + ((obj.height/3)*2));
		//determine browser window width
		var myWidth = 0, myHeight = 0;
		if( typeof( window.innerWidth ) == 'number' ) {
			//Non-IE
			myWidth = window.innerWidth;
			myHeight = window.innerHeight;
		} else if( document.documentElement && ( document.documentElement.clientWidth || document.documentElement.clientHeight ) ) {
			//IE 6+ in 'standards compliant mode'
			myWidth = document.documentElement.clientWidth;
			myHeight = document.documentElement.clientHeight;
		} else if( document.body && ( document.body.clientWidth || document.body.clientHeight ) ) {
			//IE 4 compatible
			myWidth = document.body.clientWidth;
			myHeight = document.body.clientHeight;
		}
		//limit is the width of the browser window minus the width of the popup
		var limit = myWidth - popup.clientWidth -20;
		//If popup is too far to the right, shift it left by its width
		if(popleft >= limit){
			popleft = popleft - popup.clientWidth;
		}
		popup.style.left = popleft + "px";
		popup.style.top = poptop + "px";

                if (maxdur == 24)
                  {
//popup.innerHTML = "<div id=\"popupClose\"><span onClick=\"closePopUp()\">Close<\/span><\/div><strong>Room</strong>: "+ roomname +"<br/><strong>Start Time</strong>: "+ time_str +"<br/><form name=\'reserve\' action=\'javascript:reserve("+ group +");\'>"+ altusernamestr +"<input type=\'hidden\' name=\'roomid\' value=\'"+ roomid +"\' /><input type=\'hidden\' name=\'starttime\' value=\'"+ currentmdyandtime +"\' /><input type=\'hidden\' name=\'fullcapacity\' value=\'"+ capacity +"\' /><strong><span class=\'requiredmarker\'>*</span>Duration</strong>: <input type=\'text\' name=\'duration\' value=\'"+ "0 mins" +"\' /><br/><strong><span class=\'requiredmarker\'>*</span>Number in group</strong>: <select name=\'capacity\'>"+ capacity_string +"</select><br/>"+ optionalfields_string +"<br/><center><strong>Reserve this room?</strong>: <a href=\'javascript:reserve("+ group +");\'>Yes</a> <a href=\'javascript:closePopUp();\'>No</a></center></form><br/><span class=\'requirednote\'><span class=\'requiredmarker\'>*</span> denotes a required field</span>";
//popup.innerHTML = "<strong>Room</strong>: "+ roomname +"<br/><strong>Start Time</strong>: "+ time_str +"<br/><form name=\'reserve\' action=\'javascript:reserve("+ group +");\'>"+ altusernamestr +"<input type=\'hidden\' name=\'roomid\' value=\'"+ roomid +"\' /><input type=\'hidden\' name=\'starttime\' value=\'"+ currentmdyandtime +"\' /><input type=\'hidden\' name=\'fullcapacity\' value=\'"+ capacity +"\' /><strong><span class=\'requiredmarker\'>*</span>Duration</strong>: <input type=\'text\' name=\'duration\' value=\'"+ "0 mins" +"\' /><br/><strong><span class=\'requiredmarker\'>*</span>Number in group</strong>: <select name=\'capacity\'>"+ capacity_string +"</select><br/>"+ optionalfields_string +"<br/><center><strong>Reserve this room?</strong>: <a href=\'javascript:reserve("+ group +");\'>Yes</a> <a href=\'javascript:closePopUp();\'>No</a></center></form><br/><span class=\'requirednote\'><span class=\'requiredmarker\'>*</span> denotes a required field</span>";
popup.innerHTML = "<strong>Room</strong>: "+ roomname +"<br/><strong>Start Time</strong>: "+ time_str +"<br/><form name=\'reserve\' action=\'javascript:reserve("+ group +");\'>"+ altusernamestr +"<input type=\'hidden\' name=\'roomid\' value=\'"+ roomid +"\' /><input type=\'hidden\' name=\'starttime\' value=\'"+ currentmdyandtime +"\' /><input type=\'hidden\' name=\'fullcapacity\' value=\'"+ capacity +"\' /><strong><span class=\'requiredmarker\'>*</span>Duration</strong>: <input type=\'text\' name=\'duration\' value=\'"+ "0 mins" +"\' /><br/><strong><span class=\'requiredmarker\'></span>Required group size: <label >"+capacity_string+"</label></strong><br/>"+ optionalfields_string +"<br/><center><strong>Reserve this room?</strong>: <a href=\'javascript:reserve("+ group +");\'>Yes</a> &nbsp; &nbsp; &nbsp;<a href=\'javascript:closePopUp();\'>No</a></center></form><br/><span class=\'requirednote\'><span class=\'requiredmarker\'>*</span> denotes a required field</span>";
//popup.innerHTML = "<strong>Room</strong>: "+ roomname +"<br/><strong>Start Time</strong>: "+ time_str +"<br/><form name=\'reserve\' action=\'javascript:reserve("+ group +");\'>"+ altusernamestr +"<input type=\'hidden\' name=\'roomid\' value=\'"+ roomid +"\' /><input type=\'hidden\' name=\'starttime\' value=\'"+ currentmdyandtime +"\' /><strong><span class=\'requiredmarker\'>*</span>Duration</strong>: <input type=\'text\' name=\'duration\' value=\'"+ "0 mins" +"\' /><br/><strong><span class=\'requiredmarker\'>*</span><br/>"+ optionalfields_string +"<br/><center><strong>Reserve this room?</strong>: <a href=\'javascript:reserve("+ group +");\'>Yes</a> <a href=\'javascript:closePopUp();\'>No</a></center></form><br/><span class=\'requirednote\'><span class=\'requiredmarker\'>*</span> denotes a required field</span>";
                  }
                else
                  {
//popup.innerHTML = "<div id=\"popupClose\"><span onClick=\"closePopUp()\">Close<\/span><\/div><strong>Room</strong>: "+ roomname +"<br/><strong>Start Time</strong>: "+ time_str +"<br/><form name=\'reserve\' action=\'javascript:reserve("+ group +");\'>"+ altusernamestr +"<input type=\'hidden\' name=\'roomid\' value=\'"+ roomid +"\' /><input type=\'hidden\' name=\'starttime\' value=\'"+ currentmdyandtime +"\' /><input type=\'hidden\' name=\'fullcapacity\' value=\'"+ capacity +"\' /><strong><span class=\'requiredmarker\'>*</span>Duration</strong>: <select name=\'duration\'>"+ durationhtml +"</select><br/><strong><span class=\'requiredmarker\'>*</span>Number in group</strong>: <select name=\'capacity\'>"+ capacity_string +"</select><br/>"+ optionalfields_string +"<br/><center><strong>Reserve this room?</strong>: <a href=\'javascript:reserve("+ group +");\'>Yes</a> <a href=\'javascript:closePopUp();\'>No</a></center></form><br/><span class=\'requirednote\'><span class=\'requiredmarker\'>*</span> denotes a required field</span>";
//popup.innerHTML = "<strong>Room</strong>: "+ roomname +"<br/><strong>Start Time</strong>: "+ time_str +"<br/><form name=\'reserve\' action=\'javascript:reserve("+ group +");\'>"+ altusernamestr +"<input type=\'hidden\' name=\'roomid\' value=\'"+ roomid +"\' /><input type=\'hidden\' name=\'starttime\' value=\'"+ currentmdyandtime +"\' /><input type=\'hidden\' name=\'fullcapacity\' value=\'"+ capacity +"\' /><strong><span class=\'requiredmarker\'>*</span>Duration</strong>: <select name=\'duration\'>"+ durationhtml +"</select><br/><strong><span class=\'requiredmarker\'>*</span>Number in group</strong>: <select name=\'capacity\'>"+ capacity_string +"</select><br/>"+ optionalfields_string +"<br/><center><strong>Reserve this room?</strong>: <a href=\'javascript:reserve("+ group +");\'>Yes</a> <a href=\'javascript:closePopUp();\'>No</a></center></form><br/><span class=\'requirednote\'><span class=\'requiredmarker\'>*</span> denotes a required field</span>";
popup.innerHTML = "<strong>Room</strong>: "+ roomname +"<br/><strong>Start Time</strong>: "+ time_str +"<br/><form name=\'reserve\' action=\'javascript:reserve("+ group +");\'>"+ altusernamestr +"<input type=\'hidden\' name=\'roomid\' value=\'"+ roomid +"\' /><input type=\'hidden\' name=\'starttime\' value=\'"+ currentmdyandtime +"\' /><input type=\'hidden\' name=\'fullcapacity\' value=\'"+ capacity +"\' /><strong><span class=\'requiredmarker\'>*</span>Duration</strong>: <select name=\'duration\'>"+ durationhtml +"</select><br/><strong><span class=\'requiredmarker\'></span>Required group size: <label >"+capacity_string+"</label></strong> <br/>"+ optionalfields_string +"<br/><center><strong>Reserve this room?</strong>: <a href=\'javascript:reserve("+ group +");\'>Yes</a>&nbsp; &nbsp; &nbsp; <a href=\'javascript:closePopUp();\'>No</a></center></form><br/><span class=\'requirednote\'><span class=\'requiredmarker\'>*</span> denotes a required field</span>";
//popup.innerHTML = "<strong>Room</strong>: "+ roomname +"<br/><strong>Start Time</strong>: "+ time_str +"<br/><form name=\'reserve\' action=\'javascript:reserve("+ group +");\'>"+ altusernamestr +"<input type=\'hidden\' name=\'roomid\' value=\'"+ roomid +"\' /><input type=\'hidden\' name=\'starttime\' value=\'"+ currentmdyandtime +"\' /><strong><span class=\'requiredmarker\'>*</span>Duration</strong>: <select name=\'duration\'>"+ durationhtml +"</select><br/><strong><span class=\'requiredmarker\'>*</span><br/>"+ optionalfields_string +"<br/><center><strong>Reserve this room?</strong>: <a href=\'javascript:reserve("+ group +");\'>Yes</a> <a href=\'javascript:closePopUp();\'>No</a></center></form><br/><span class=\'requirednote\'><span class=\'requiredmarker\'>*</span> denotes a required field</span>";
                  }
	}
	
	function closePopUp(){
		document.getElementById("popup").style.visibility = "hidden";
		document.getElementById("popup").style.display = "none";
	}
	
	function dummyF(){
                 alert("I am an alert box!");
	}
	

	function cancel(reservationid,groupid){
                 var answer = confirm("Please confirm cancellation of this reservation.");
              if (answer)
                {
		//Cancel reservation using or-cancel.php
		try{
			req = new XMLHttpRequest();
		} catch(err1){
			try{
				req = new ActiveXObject("Msxm12.XMLHTTP");
			} catch(err2){
				try{
					req = new ActiveXObject("Microsoft.XMLHTTP");
				} catch(err3){
					req = false;
				}
			}
		}
		if(req != false) var xmlhttp = req;
		
		xmlhttp.onreadystatechange=function(){
			if(xmlhttp.readyState==4){
				var brokenstring = xmlhttp.responseText.split("|");
				if(brokenstring[0] == "Error: User is not logged in.") location.reload(true);
				document.getElementById("popup").innerHTML = "<div id=\"popupClose\"><span onClick=\"closePopUp()\">Close<\/span><\/div>" + brokenstring[0];
				dayviewer(brokenstring[1],brokenstring[2],groupid,'');
                                ajaxFunction(0,0); //All params = 0 for current date to appear
			}
			else{
				document.getElementById("popup").innerHTML = "Cancelling...";
			}
		};
		
		urlstring = "or-cancel.php";

		params = "reservationid="+ reservationid;
		
		xmlhttp.open("POST",urlstring,true);
		xmlhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");	
		xmlhttp.send(params);
                }
	}
	
	function checkin(reservationid,groupid){
		//Check-in or Check-out from a reservation using or-checkin.php
		try{
			req = new XMLHttpRequest();
		} catch(err1){
			try{
				req = new ActiveXObject("Msxm12.XMLHTTP");
			} catch(err2){
				try{
					req = new ActiveXObject("Microsoft.XMLHTTP");
				} catch(err3){
					req = false;
				}
			}
		}
		if(req != false) var xmlhttp = req;
		
		xmlhttp.onreadystatechange=function(){
			if(xmlhttp.readyState==4){
				var brokenstring = xmlhttp.responseText.split("|");
				if(brokenstring[0] == "Error: User is not logged in.") location.reload(true);
				document.getElementById("popup").innerHTML = "<div id=\"popupClose\"><span onClick=\"closePopUp()\">Close<\/span><\/div>" + brokenstring[0];
				//dayviewer(brokenstring[1],brokenstring[2],groupid,'');
				dayviewer(0,0,groupid,'');
                                ajaxFunction(0,0); //All params = 0 for current date to appear
			}
			else{
				document.getElementById("popup").innerHTML = "Cancelling...";
			}
		};
		
		urlstring = "or-checkin.php";

		params = "reservationid="+ reservationid;
		
		xmlhttp.open("POST",urlstring,true);
		xmlhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");	
		xmlhttp.send(params);
	}
        
	
	function reserve(groupid){
              

		try{
			req = new XMLHttpRequest();
		} catch(err1){
			try{
				req = new ActiveXObject("Msxm12.XMLHTTP");
			} catch(err2){
				try{
					req = new ActiveXObject("Microsoft.XMLHTTP");
				} catch(err3){
					req = false;
				}
			}
		}
		if(req != false) var xmlhttp = req;
		
		var starttime = parseInt(document.reserve.starttime.value);
		var duration = parseInt(document.reserve.duration.value);
		if(document.reserve.altusername){
			var altusername = document.reserve.altusername.value;
		}
		else{
			var altusername = "";
		}
		if(document.reserve.altuseremail){
			var altuseremail = document.reserve.altuseremail.value;
		}
		else{
			var altuseremail = "";
		}
		if(document.reserve.emailconfirmation){
			var emailconfirmation = document.reserve.emailconfirmation.value;
		}
		else{
			var emailconfirmation = "";
		}
		var endtime = starttime + (duration*60);
		
		xmlhttp.onreadystatechange=function(){
			if(xmlhttp.readyState==4){
				var brokenstring = xmlhttp.responseText.split("|");
				if(brokenstring[0] == "Error: User is not logged in.") location.reload(true);
				document.getElementById("popup").innerHTML = "<div id=\"popupClose\"><span onClick=\"closePopUp()\">Close<\/span><\/div>" + brokenstring[0];
				dayviewer(starttime,brokenstring[2],groupid,'');
                                ajaxFunction(0,0); //All params = 0 for current date to appear
			}
			else{
				document.getElementById("popup").innerHTML = "Reserving...";
			}
		};
		
		urlstring = "or-reserve.php";

		params = "altusername="+ altusername + "&altuseremail="+ altuseremail + "&emailconfirmation="+ emailconfirmation +"&duration="+ document.reserve.duration.value +"&roomid="+ document.reserve.roomid.value +"&starttime="+ document.reserve.starttime.value +"&capacity="+  document.reserve.fullcapacity.value +"&fullcapacity="+ document.reserve.fullcapacity.value +"";
		
		xmlhttp.open("POST",urlstring,true);
		xmlhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");	
		xmlhttp.send(params);
	}
// </script>