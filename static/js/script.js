$(document).ready(function () {
  $('.sidenav').sidenav();
  $('#textarea1');
  M.textareaAutoResize($('#textarea1'));
  $('.chips').chips();
  $('.chips-initial').chips({
    data: [{
    tag: 'Ingredient',
    }],
    onChipAdd: ingredientsData(),
  });
  $('select').formSelect();
  $('.modal').modal();
  ingredients = [];
  function ingredientsData(){
    ingredients.append(M.Chips.getInstance($('.chips')).chipsData);
    console.log(ingredients)
    for (var i=0; i<ingredients.length; i++) { 
      newChips = document.getElementsByClassName('.input');
      for (var i=0; i<newChips.length; i++) {
        newChips[i].setAttribute('name', 'ingredient');
      }
      }
  };
})


// code from https://www.quirksmode.org/dom/domform.html
window.onload = addStep();

var counter = 0

function addStep() {
  counter++;
  var newSteps = document.getElementById('step-div').cloneNode(true);
  newSteps.id = '';
  newSteps.style.display = 'block';
  // var newStep = newSteps.childNodes;
  // for (var i=0;i<newStep.length;i++) {
	// 	var step = newStep[i].name;
  //   console.log(newStep);
	// 	if (step)
	// 		newStep[i].name = step + counter;
	// }
  var insertHere = document.getElementById('create-step');
	insertHere.parentNode.insertBefore(newSteps,insertHere);
  labels = document.getElementsByClassName("instructions-label");
    for (var i=0; i<labels.length; i++) {
      labels[i].innerHTML = `Instructions: Step ${i++}`
    }
};

function removeStep() {
  document.getElementById("create-step").previousSibling.remove();
}

addButtons = document.getElementsByClassName("add-step");
for (var i=0; i<addButtons.length; i++) {
  addButtons[i].addEventListener("click", addStep);
}
removeButtons = document.getElementsByClassName("remove-step")
for (var i=0; i<removeButtons.length; i++) {
  removeButtons[i].addEventListener("click", removeStep);
}

