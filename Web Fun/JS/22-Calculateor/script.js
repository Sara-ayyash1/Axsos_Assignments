let displayVariable = document.querySelector("#display");
let currentInput = "";
let firstOperand = null;
let operator = null;

function press(num) {
  currentInput += num;
  displayVariable.innerHTML = currentInput;
}

function setOP(op) {
  if (currentInput === "") return;

  firstOperand = parseFloat(currentInput);
  operator = op;
  currentInput = "";
}

function calculate() {
  if (operator === null || currentInput === "") return;

  let secondOperand = parseFloat(currentInput);
  let result = 0;

  switch (operator) {
    case "+":
      result = firstOperand + secondOperand;
      break;
    case "-":
      result = firstOperand - secondOperand;
      break;
    case "*":
      result = firstOperand * secondOperand;
      break;
    case "/":
      result = firstOperand / secondOperand;
      break;
  }

  displayVariable.innerHTML = result;
  currentInput = result.toString();
  operator = null;
}

function clr() {
  currentInput = "";
  firstOperand = null;
  operator = null;
  displayVariable.innerHTML = "0";
}