function menuHighLight() {

if(document.URL.indexOf("feed") >= 0){ 
    document.getElementById('menu_feed').className = 'active';
}

if(document.URL.indexOf("profile") >= 0){ 
    document.getElementById('menu_profile').className = 'active';
}

if(document.URL.indexOf("messages") >= 0){ 
    document.getElementById('menu_messages').className = 'active';
}  
}

window.onload = menuHighLight;