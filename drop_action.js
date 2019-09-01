const Tm = 27; // the time for executing
const Ts = 05;
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

function ClkThchRoom(TimeStr,TimeEnd){

    // elem = TechRoom;
    // triggerEvent(elem,'click');
    // dayviewer('1567310400','1567396799','13','');
    dayviewer(TimeStr,TimeEnd,'13','');
}

function ReserveWin(Room,T_S,rn,T){
    showPopUpReserve(this,'Room 5','3:30 pm','13','','184','1567366200','8','1','<option value=\'60\'>60 mins</option><option value=\'30\'>30 mins</option>','1-8','');
    // showPopUpReserve(this,Room,T_S,'13','',rn,T,'8','1','<option value=\'60\'>60 mins</option><option value=\'30\'>30 mins</option>','1-8','')
    // showPopUpReserve(obj,roomname,time_str,group,altusernamestr,roomid,currentmdyandtime,capacity,maxdur,durationhtml,capacity_string,optionalfields_string){}
    // showPopUpReserve('Room 5','3:30 pm','13','','184','1567366200','8','1','<option value=\'60\'>60 mins</option><option value=\'30\'>30 mins</option>','1-8','');
}

function act(b,e,t = 1000){
    // setTimeout(ClkTomor,t);
    begin = ''.concat(b);
    end = ''.concat(e);
    T = Time.getTime(true,3,30);
    // setTimeout(ClkThchRoom,t,begin,end);
    setTimeout(ReserveWin,t,'Room 5','3:30 pm','184',T);
    // ReserveWin('Room 5','3:30 pm','184',T);
}

dT = ((Tm-time.getMinutes())*60 + (Ts - time.getSeconds()))*1000;
Today = Time.Today();
TodayEnd = Time.EndofToday();

act(Today,TodayEnd,t = dT)



