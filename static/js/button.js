var instructionsButton = document.getElementsByClass("add-step");


for (let i = 0; i < instructionsButton.length; i++) {
    instructionsButton[i].addEventListener('click', addStep());
}

function addstep() {
    document.getElementById("step-div").innerHTML = `
  <div class='input-field col s12'>
  <textarea id='textarea1' class='materialize-textarea' name='instructions1'></textarea>
  <label for='instructions1'>Instructions: Step 1</label>
  <a class='waves-effect waves-light btn red darken-1 btn-small add-step'>
      <i class='material-icons right'>add_circle_outline</i>Add Step
  </a>
</div>`
};