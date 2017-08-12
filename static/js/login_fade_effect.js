$(document).ready(function () {
    $("#login_btn").click(function(){
    
	login_test();
$('#error').finish().fadeIn("fast").delay(1200).fadeOut(400);
      
    });
});

function login_test() {
  
document.getElementById("error").innerHTML ="<p class='red'>Failed to authorize login.</p>"; 
}