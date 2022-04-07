#!/usr/bin/node
$(function () {
  let $movies = $('UL#list_movies');
  $.ajax({
    type: 'Get',
    url: 'https://fourtonfish.com/hellosalut/?lang=fr',
    success: function (data) {
      $('DIV#hello').html(data.hello)
    }
  });
});
