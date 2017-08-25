/* $(document).ready(function () {
$('textarea').keyup(updateCount);
});

function updateCount() {
    var cs = $(this).val().length;
    $('#counter').text(cs);
	
	if(cs > 0 && (!$(this).hasClass("hide"))){
		document.getElementById("counter_wrapper").classList.remove('hide');
		$('#counter_wrapper').finish().fadeIn("fast").delay(1600);
	} else {
		document.getElementById("counter_wrapper").classList.add('hide');
		$('#counter_wrapper').finish().fadeIn("fast").fadeOut(400);
	}
} */

$(document).ready(function () {
$('#feed_entry_textfield').keyup(function () {
  
  var max = 420;
  var len = $(this).val().length;
  $('#counter').text(len);
  
  	if(len != 0 && (!$(this).hasClass("hide"))){
		document.getElementById("counter_wrapper").classList.remove('hide');
		$('#counter_wrapper').finish().fadeIn("fast").delay(1600);
	} else {
		document.getElementById("counter_wrapper").classList.add('hide');
		$('#counter_wrapper').finish().fadeIn("fast").fadeOut(400);
	}
	
});
});