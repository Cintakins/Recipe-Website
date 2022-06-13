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

// code from https://www.quirksmode.org/dom/domform.html
window.onload = addStep();

var counter = 0

function addStep() {
  counter++;
  var newSteps = document.getElementById('step-div').cloneNode(true);
  newSteps.id = ''
  newSteps.style.display = 'block';
  var newStep = newSteps.childNodes;
  for (var i=0;i<newStep.length;i++) {
		var step = newStep[i].name
		if (step)
			newStep[i].name = step + counter;
	}

  var insertHere = document.getElementById('create-step');
	insertHere.parentNode.insertBefore(newSteps,insertHere);
};

function removeStep() {
  document.getElementById("create-step").previousSibling.remove();
}

document.getElementById("add-step").addEventListener("click", addStep);
document.getElementById("remove-step").addEventListener("click", removeStep);

