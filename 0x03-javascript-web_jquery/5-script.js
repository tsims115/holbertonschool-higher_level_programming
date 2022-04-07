#!/usr/bin/node
$(function () {

  $("DIV#add_item").css({
    color: '#FF0000',
  });

  $('DIV#add_item').on('click', function () {
    $("UL.my_list").html("<li>Item</li>");
  })

});
