const operator = prompt('Enter operator: either +, -, *, / ');
const number1 = parseFloat(prompt('Enter first number: '));
const number2 = parseFloat(prompt('Enter second number: '));

function math (num1,num2,op){
    let result;
    if (operator == '+') {
        result = number1 + number2;
    }else if (operator == '-') {
        result = number1 - number2;
    }else if (operator == '*') {
        result = number1 * number2;
    }else {
        result = number1 / number2;
    }
    console.log(number1, operator , number2,"=",result);
}

math(number1, number2, operator)
