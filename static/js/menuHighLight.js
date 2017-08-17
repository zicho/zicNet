function menuHighLight() {

if(document.URL.indexOf("feed") >= 0){ 
    document.getElementById('menu_feed').className = 'active';
}

if(document.URL.indexOf("profile") >= 0){ 
    document.getElementById('menu_profile').className = 'active';
} 
 
}

window.onload = menuHighLight;