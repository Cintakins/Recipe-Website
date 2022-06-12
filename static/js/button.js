document.getElementById("add-step").addEventListener('click', addStep());

function addStep() {
    instructionStep = `
    <textarea id='textarea1' class='materialize-textarea' name='instructions1'></textarea>
    <label for='instructions1'>Instructions: Step 1</label> `
    document.getElementById("step-div").appendChild(instructionStep);
};