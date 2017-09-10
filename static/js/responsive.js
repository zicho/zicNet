$(function() {
  
  // Create the dropdown base
  $("<select />").appendTo("#menu_nav");

  // Populate dropdown with menu items
  $("nav a").each(function() {
    var el = $(this);
    $("<option />", {
      value: el.attr("href"),
      text: el.text()
    }).appendTo("nav select");
  });

  //  Grab the options
  var $select = $("#menu select");
  var options = $select.find("option");

  // turn the nodelist into an array and reverse it
  options = [].slice.call(options).reverse();

  // empty the select
  $select.empty();

  // add each option back
  $.each(options, function(i, el) {
    $select.append($(el));
  });

  // Create default option "Go to..."
  $("<option />", {
    selected: "selected",
    value: "",
    text: "Go to... "
  }).prependTo("nav select");

  // To make dropdown actually work
  $("nav select").change(function() {
    window.location = $(this).find("option:selected").val();
  });
  

});

