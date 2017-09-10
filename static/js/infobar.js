$(document).ready(function() {
  var div = document.getElementById("info_bar");

  $("#menu_main li").hover(
    function() {
      $("#info_bar").finish().fadeIn("fast");
    },
    function() {
      $("#info_bar").finish().fadeOut("fast");
    }
  );
  
  $("#menu_feed").hover(function() {
    div.innerHTML =
      'View latest <span class="red" style="font-size: 100%">feed</span> entries';
  });

  $("#menu_profile").hover(function() {
    div.innerHTML =
      'View and edit your <span class="red" style="font-size: 100%">profile</span>';
  });

  $("#menu_messages").hover(function() {
  
    if(js_data == 0) { 
    message =
    'View and send <span class="red" style="font-size: 100%">messages</span>';
	} else if(js_data == 1) {
	message = 'You have a new message!';
	}
	else { 
	message = 'You have ' + js_data + ' new messages!';
	}
	
    div.innerHTML = message;
  });

  $("#menu_events").hover(function() {
    div.innerHTML =
      'View upcoming <span class="red" style="font-size: 100%">events</span>';
  });

  $("#menu_friends").hover(function() {
    div.innerHTML =
      'View your <span class="red" style="font-size: 100%">friend</span> list';
  });

  $("#menu_logout").hover(function() {
    div.innerHTML = 'Log out from <span class="red" style="font-size: 100%">zicNet</span>';
  });
});