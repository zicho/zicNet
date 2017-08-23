// pass the div id and the html string to the "fade_effect" function using the functions below
// this is to make use of a generic fade effect function and thus reduce redundancy
// just create the correct variables for various fade effects and pass them to the fade_effect function!

function feed_error_fade() {

div_id = "feed_error";
html = "<p class='red'>You cannot submit an empty message! Please enter a message body.</p>";

fade_effect(div_id, html);
}

function fade_effect(div_id, html) {
	
	document.getElementById(div_id).innerHTML ="<p class='red'>You cannot submit an empty message! Please enter a message body.</p>";
	$('#'+div_id).finish().fadeIn("fast").delay(1600).fadeOut(400);
}