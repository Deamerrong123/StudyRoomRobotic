const Tm = 41; // the time for executing
const Ts = 05;
var dT; // Time before execution
var logInField = document.querySelector("input[id = 'loginsubmitbutton']");
var TomorrowButton = document.querySelector("input[value = 'TOMORROW']");
var TechRoom = document.querySelector('a[onclick]'); // this is not working

var time = new Date();


let Time = {
   getDate : function(){
    t = time.toString().split(' ');
    Str = t[1] + ' '+t[2] + ','+t[3];
    return Str;
   }
   

}

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
    dayviewer('1567310400','1567396799','13','');
}

function act(b,e,t){
    // setTimeout(ClkTomor,t);
    begin = b;
    end = e;
    setTimeout(ClkThchRoom(begin,end),t);
}

dT = ((Tm-time.getMinutes())*60 + (Ts - time.getSeconds()))*1000;

act(dT);



