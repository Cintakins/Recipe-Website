$(document).ready(function () {
  $('.sidenav').sidenav();
  $('#textarea1');
  M.textareaAutoResize($('#textarea1'));
  $('select').formSelect();
  $('.modal').modal();
})


// code inspired by https://www.quirksmode.org/dom/domform.html

function addIngredient() {
  var newIngredients = document.getElementById('ingredient-div').cloneNode(true);
  newIngredients.id = '';
  newIngredients.style.display = 'block';
  var insertHere = document.getElementById('create-ingredient');
	insertHere.parentNode.insertBefore(newIngredients,insertHere);
};

function removeIngredient() {
  document.getElementById("create-ingredient").previousSibling.remove();
}

addIngredientButtons = document.getElementsByClassName("add-ingredient");
for (var i=0; i<addIngredientButtons.length; i++) {
  addIngredientButtons[i].addEventListener("click", addIngredient);
}
removeIngredientButtons = document.getElementsByClassName("remove-ingredient")
for (var i=0; i<removeIngredientButtons.length; i++) {
  removeIngredientButtons[i].addEventListener("click", removeIngredient);
}

function addStep() {
  var newSteps = document.getElementById('step-div').cloneNode(true);
  newSteps.id = '';
  newSteps.style.display = 'block';
  var insertHere = document.getElementById('create-step');
	insertHere.parentNode.insertBefore(newSteps,insertHere);
};

function removeStep() {
  document.getElementById("create-step").previousSibling.remove();
}

addStepButtons = document.getElementsByClassName("add-step");
for (var i=0; i<addStepButtons.length; i++) {
  addStepButtons[i].addEventListener("click", addStep);
}
removeStepButtons = document.getElementsByClassName("remove-step")
for (var i=0; i<removeStepButtons.length; i++) {
  removeStepButtons[i].addEventListener("click", removeStep);
}

