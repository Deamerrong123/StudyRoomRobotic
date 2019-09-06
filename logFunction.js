// https://www.baruch.cuny.edu/library/reservaroom/
// https://www.baruch.cuny.edu/library/reservaroom/

var newWin;
var newConsole;
var newDoc;
function loger(un,pw){
    this.username = un;
    this.password = pw;

    function getUsername(){
        return this.username;
    }
    function getPassword(){
        return this.password;
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

sel_u = loger(document.getElementById('usernamefield'),document.getElementById('passwordfield'));


function load (){
    url = "https://www.baruch.cuny.edu/library/reservaroom/";
    winName = "BaruchLogin Page";
    strWindowFeatures = "menubar = yes , locatioin = yes, resizable = yes,\
        scrollbar = yes , status = yes, width = 200, height = 100";

    newWin = window.open(url,"","width = 600 , height = 400");

    setTimeout(function (){
        newDoc = newWin.document();
       
    },1000);

    
}
