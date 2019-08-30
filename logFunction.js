
function loger(un,pw){
    this.username = un;
    this.passward = pw;

    function getUsername(){
        return this.username;
    }
    function getPassward(){
        return this.passward;
    }
}

loger(document.getElementById('usernamefield'),document.getElementById('passwardfield'));


function log(){
    
}
