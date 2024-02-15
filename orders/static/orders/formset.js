let posForm = document.querySelectorAll(".pos-form")
let container = document.querySelector("#form-container")
let addButton = document.querySelector("#add-form")
let totalForms = document.querySelector("#id_form-TOTAL_FORMS")

let formNum = posForm.length - 1 // get the number of the last form with zero-based indexing

addButton.addEventListener('click', addForm)

function addForm(e) {
    e.preventDefault()

    let newForm = posForm[0].cloneNode(true) //Clone the position form
    let formRegex = RegExp(`form-(\\d){1}-`,'g') //Regex to find all instances of the form number

    formNum++ //Increment the form number
    newForm.innerHTML = newForm.innerHTML.replace(formRegex, `form-${formNum}-`) //Update the new form to have the correct form number
    container.insertBefore(newForm, addButton) //Insert the new form at the end of the list of forms

    totalForms.setAttribute('value', `${formNum+1}`) //Increment the number of total forms in the management form
    console.log('Done')
}