var dt;
const Tomorrow = 1568001600000;

function get_time_now(){
    let T = new Date();
    now = T.getTime();
    return now
}

dt = Tomorrow - get_time_now();

username = document.getElementById('usernamefield');
password = document.getElementById('passwordfield');

username.value = '';
password.value = '';

setTimeout(function(){
    ajaxAuthenticate();
},dt);
