function changeFunc() {
    const elem = document.getElementById("height");
    const value = elem.value;
    if(value == 1) {
        const parentSec = document.getElementById("second")
        parentSec.innerHTML = "";

        const label = document.createElement("label");
        label.setAttribute('for', 'feet');
        label.innerHTML = "Feet";
        const input = document.createElement("input");
        input.setAttribute('type', 'number')
        input.setAttribute('id', 'feet')
        input.setAttribute('class', 'form-control')
        input.setAttribute('name', 'feet')
        input.setAttribute('placeholder', 'Feet')
        input.setAttribute('min', '3')
        input.setAttribute('max', '7')
        input.setAttribute('step', '1')
        input.setAttribute('required', true)


        const labelInch = document.createElement("label");
        labelInch.setAttribute('for', 'inches');
        labelInch.innerHTML = "Inches";
        const inputInch = document.createElement("input");
        inputInch.setAttribute('type', 'number')
        inputInch.setAttribute('id', 'inches')
        inputInch.setAttribute('class', 'form-control')
        inputInch.setAttribute('name', 'inches')
        inputInch.setAttribute('placeholder', 'Inches')
        inputInch.setAttribute('min', '0')
        inputInch.setAttribute('max', '11')
        inputInch.setAttribute('step', '1')
        inputInch.setAttribute('required', true)

        const parentFeet = document.getElementById("feet")
        const parentInch = document.getElementById("inch")

        parentFeet.appendChild(input)
        parentFeet.appendChild(label)
        parentInch.appendChild(inputInch)
        parentInch.appendChild(labelInch)
    } else if (value == 2) {
        const parentFirst = document.getElementById("first")
        parentFirst.innerHTML = "";

        const labelCent = document.createElement("label");
        labelCent.setAttribute('for', 'cent');
        labelCent.innerHTML = "Centimeters";
        const input = document.createElement("input");
        input.setAttribute('type', 'number')
        input.setAttribute('id', 'cent')
        input.setAttribute('class', 'form-control')
        input.setAttribute('name', 'cent')
        input.setAttribute('placeholder', 'Centimeters')
        input.setAttribute('min', '100')
        input.setAttribute('max', '230')
        input.setAttribute('step', '1')
        input.setAttribute('required', true)

        const labelWeight = document.createElement("label");
        labelWeight.setAttribute('for', 'weight');
        labelWeight.innerHTML = "Weight (KG)";
        const weightInput = document.createElement("input");
        weightInput.setAttribute("type", "number")
        weightInput.setAttribute("id", "weight")
        weightInput.setAttribute("class", "form-control")
        weightInput.setAttribute("name", "weight")
        weightInput.setAttribute("placeholder", "Weight (KG)")
        weightInput.setAttribute('required', true)


        const parentOne = document.getElementById("second-one")
        parentOne.appendChild(input)
        parentOne.appendChild(labelCent)
        const parentTwo = document.getElementById("second-two")
        parentTwo.appendChild(weightInput)
        parentTwo.appendChild(labelWeight)
    } else {
        const parentFirst = document.getElementById("first")
        const parentSec = document.getElementById("second")
        if(parentFirst) {
            parentFirst.innerHTML = "";
        }
        if (parentSec) {
            parentSec.innerHTML = "";
        }
    }
}