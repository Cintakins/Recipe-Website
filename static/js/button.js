var instructionsButton = document.getElementsByClass("add-step");
instructionsButton.addEventListener("click", function {
  document.getElementsByClass("step-div").innerHTML = `
  <div class='input-field col s12'>
  <textarea id='textarea1' class='materialize-textarea' name='instructions1'></textarea>
  <label for='instructions1'>Instructions: Step 1</label>
  <a class='waves-effect waves-light btn red darken-1 btn-small add-step'>
      <i class='material-icons right'>add_circle_outline</i>Add Step
  </a>
</div>`;
});