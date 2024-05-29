$(document).ready(function () {
  $('INPUT#btn_translate').on('click', function () {
    translatehello();
  });

  $('INPUT#language_code').on('keypress', function (event) {
    if (event.which === 13) {
      translatehello();
    }
  });

  function translatehello () {
    const language = $('INPUT#language_code').val();
    const apiurl = `https://hellosalut.stefanbohacek.dev/?lang=${language}`;
    $.get(apiurl, function (data) {
      $('DIV#hello').text(data.hello);
    });
  }
});
