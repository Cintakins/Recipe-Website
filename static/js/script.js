$(document).ready(function () {
  $('.sidenav').sidenav();
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

var counter = 0

// code from https://www.quirksmode.org/dom/domform.html
function addStep() {
  counter++;
  var newSteps = document.getElementById('step-div').cloneNode(true);
  newSteps.id = ''
  newSteps.style.display = 'block';
  var newStep = newSteps.childNodes;
  for (var i=0;i<newStep.length;i++) {
		var step = newField[i].name
		if (step)
			newField[i].name = step + counter;
	}

  var insertHere = document.getElementById('create-step');
	insertHere.parentNode.insertBefore(newSteps,insertHere);
};