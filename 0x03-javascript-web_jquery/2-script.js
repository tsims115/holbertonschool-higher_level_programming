#!/usr/bin/node
$(function () {

  $('DIV#red_header').on('click', function () {
    $("header").css({
      color: '#FF0000',
    });
  })
});
