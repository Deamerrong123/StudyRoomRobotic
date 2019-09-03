// https://www.baruch.cuny.edu/library/reservaroom/
// https://www.baruch.cuny.edu/library/reservaroom/


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
    window.location.href = "https://www.baruch.cuny.edu/library/reservaroom/";
    // if ($(document).ready()){
    //     username = document.getElementById('usernamefield');
    //     password = document.getElementById('passwordfild');
    //     logIn = document.getElementById('loginsubmitbutton');

    //     username.value = sel_u.getUsername();
    //     password.value = sel_u.getPassword();

    //     triggerEvent(logIn,'click');

    // }
    // else{
    //     pass;
    // }
}
