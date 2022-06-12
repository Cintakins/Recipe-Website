$(document).ready(function () {
  $('#textarea1');
  M.textareaAutoResize($('#textarea1'));
  $('.chips').chips();
  $('.chips-initial').chips({
    data: [{
      tag: 'Ingredient',
    }]
  });
  $('select').formSelect();
})
