const Tm = 27; // the time for executing
const Ts = 05; 

// const Et = 1567396800000 + 500; // the true executing time, Sep 2 , 2019 , 00:00:00

const Et = 1567396800000 + 1000 * 60 * 20; // the true executing time, Sep 2 , 2019 , 00:20:00


var dT; // Time before execution
var logInField = document.querySelector("input[id = 'loginsubmitbutton']");
var TomorrowButton = document.querySelector("input[value = 'TOMORROW']");
// var TechRoom = document.querySelector('a[onclick]'); // this is not working


var time = new Date();


var Time = {
   getDate : function(){
    t = time.toString().split(' ');
    Str = t[1] + ' '+t[2] + ','+t[3];
    return Str;
   },
   Today : function(){
       s = this.getDate();
       return Date.parse(s)/1000;
   },

   getTime : function(n,h,m){
       var tem = this.Today();
       if (n){
           h  = h + 12;
           tem = tem + h * 60 * 60 + m*60;
       }
       else{
           tem = tem + h * 60 * 60 + m * 60;
       }
       return tem;
   },

   Tomorrow : function (){
       h = 24*60*60;
       tem = this.Today();
       return h+ tem;
   },

   TomorrowAhead : function(){
       h = 24*60*60;
       tem = this.Tomorrow();
       return h + tem;
   },

   EndofToday : function(){
       return this.Tomorrow - 1;
   },

   EndofTomorr : function(){
       return this.TomorrowAhead() -1 ;
   }

};

function triggerEvent(el, type){
    if ('createEvent' in document) {
    // modern browsers, IE9+
    var e = document.createEvent('HTMLEvents');
    e.initEvent(type, false, true);
    el.dispatchEvent(e);
    } else {
    // IE 8
    var e = document.createEventObject();
    e.eventType = type;
    el.fireEvent('on'+e.eventType, e);
    }
}

function ClkTomor(){
    // elem = document.querySelector('a[href="33386988.html"]');
    elem = TomorrowButton;
    triggerEvent(elem,'click'); 
}

function ClkThchRoom(){

    // elem = TechRoom;
    // triggerEvent(elem,'click');
    // dayviewer('1567310400','1567396799','13','');
    self.location.reload();
    begin = ''.concat(Time.Tomorrow());
    end = ''.concat(Time.EndofTomorr());
    dayviewer(begin,end,'13','');
}

var PopUpReserve = {
    popup : document.getElementById('popup'),
    visibility : this.popup.style.visibility,
    display : this.popup.style.display,
};

function ShowPopUpReserve(popleft,poptop,roomname,time_str,group,altusernamestr,roomid,currentmdyandtime,capacity,maxdur,durationhtml,capacity_string,optionalfields_string){
    PopUpReserve.visibility = 'visible';
    PopUpReserve.display = 'inline';

    //style="left: 151px; top: 912px

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



function showReserveWin(Room,T_S,rn,T){
    //showPopUpReserve(this,'Room 5','3:30 pm','13','','184','1567366200','8','1','<option value=\'60\'>60 mins</option><option value=\'30\'>30 mins</option>','1-8','');
    // showPopUpReserve(this,Room,T_S,'13','',rn,T,'8','1','<option value=\'60\'>60 mins</option><option value=\'30\'>30 mins</option>','1-8','')
    // showPopUpReserve(obj,roomname,time_str,group,altusernamestr,roomid,currentmdyandtime,capacity,maxdur,durationhtml,capacity_string,optionalfields_string){}
    // showPopUpReserve('Room 5','3:30 pm','13','','184','1567366200','8','1','<option value=\'60\'>60 mins</option><option value=\'30\'>30 mins</option>','1-8','');
    ShowPopUpReserve(151,912,'Room 5','3:30 pm','13','','184','1567366200','8','1','<option value=\'60\'>60 mins</option><option value=\'30\'>30 mins</option>','1-8','')
}

function act(t){
    // // setTimeout(ClkTomor,t);
    // begin = ''.concat(b);
    // end = ''.concat(e);
    // T = Time.getTime(true,3,30);


    setTimeout(ClkThchRoom,t);
    // setTimeout(ReserveWin,t,'Room 5','3:30 pm','184',T);
    // ReserveWin('Room 5','3:30 pm','184',T);
}

// dT = ((Tm-time.getMinutes())*60 + (Ts - time.getSeconds()))*1000;
self.location.reload();
dT = Et - time.getTime();
// Tomor = Time.Tomorrow();
// TomorEnd = Time.EndofTomorr();

// act(Tomor,TomorEnd,t = dT)
act(dT);



