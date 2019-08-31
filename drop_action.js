const Tm = 05; // the time for executing
const Ts = 30;
var dT; // Time before execution

var time = new Date();

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

function myfunction(){
    elem = document.querySelector('a[href="33386988.html"]');
    triggerEvent(elem,'click'); 
}

function act(t){
    setTimeout(myfunction,t);
}

dT = ((Tm-time.getMinutes())*60 + (Ts - time.getSeconds()))*1000;

act(dT);



