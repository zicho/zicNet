// pass the div id and the html string to the "fade_effect" function using the functions below
// this is to make use of a generic fade effect function and thus reduce redundancy
// just create the correct variables for various fade effects and pass them to the fade_effect function!

function login_error_fade() {

div_id = "login_error";
html = "<p class='red'>User credentials could not be verified!</p>";

fade_effect(div_id, html);
}

function pw_error_fade() {

div_id = "pw_change_error";
html = "<p class='red'>Passwords do not match.</p>";

fade_effect(div_id, html);
}

function feed_success_fade() {

div_id = "message";
html = "<p class='green'>Feed entry added!</p>";

fade_effect(div_id, html);
}

function feed_error_fade() {

div_id = "message";
html = "<p class='red'>You cannot submit an empty message! Please enter a message body.</p>";

fade_effect(div_id, html);
}

function comment_success_fade() {

div_id = "message";
html = "<p class='green'>Comment added!</p>";

fade_effect(div_id, html);
}

function comment_error_fade() {

div_id = "message";
html = "<p class='red'>You cannot submit an empty comment! Please enter a comment body.</p>";

fade_effect(div_id, html);
}

function fade_effect(div_id, html) {
	
	document.getElementById(div_id).innerHTML = html;
	$('#'+div_id).finish().fadeIn("fast").delay(1600).fadeOut(400);
}