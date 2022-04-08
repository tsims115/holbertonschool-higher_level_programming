$(function () {
  let $movies = $('UL#list_movies');
  $.ajax({
    type: 'Get',
    url: 'https://swapi-api.hbtn.io/api/films/?format=json',
    success: function (data) {
      $.each(data.results, function (i, movie) {
        $movies.append("<li>" + movie.title + "</li>")
      });
    }
  });
});
