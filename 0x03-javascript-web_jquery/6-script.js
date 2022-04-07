#!/usr/bin/node
$(function () {
  $("DIV#update_header").on('click', function () {
    $('header').html("New Header");
  });
});
