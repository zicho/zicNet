function feed_error_fade() {
  
document.getElementById("feed_error").innerHTML ="<p class='red'>You cannot submit an empty message! Please enter a message body.</p>";

$('#feed_error').finish().fadeIn("fast").delay(1600).fadeOut(400);  
  
}
