$(document).ready(function () {
  // Ensure that code is executed only when document is fully loaded
  $.get(
    // UsejQuery GET method to make an AJAX request to the URL
    'https://swapi-api.alx-tools.com/api/people/5/?format=json',
    function (data) {
      $('#character').text(data.name);
    });
});
