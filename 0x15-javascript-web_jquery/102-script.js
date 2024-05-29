$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    const language = $('INPUT#language_code').val();
    const apiurl = `https://hellosalut.stefanbohacek.dev/?lang=${language}`;
    $.get(apiurl, function (data) {
      $('DIV#hello').text(data.hello);
    });
  });
});
