// Create a function that, given an input string, returns a boolean true/false whether parentheses in that string are valid.

// Example 1:"y(3(p)p(3)r)s" --> true
// Example 2: "n(0(p)3" --> false
// Example 3: "n)0(t(o)k" --> false

// hint: consider using an array or object to solve

// check entire string, return true/false
// every single opening parens has a closing
// never hit an closing parens before a opening parens
// ONLY care about the parens in the string


function parensValid(str) {
    var tempArray = Array.from(str);
    // console.log(tempArray);
    var openCounter = 0
    var closedCounter = 0
    for (let i = 0; i < tempArray.length; i++) {
        if (tempArray[i] == "(") {
            openCounter += 1
        }
        else if (tempArray[i] == ")") {
            closedCounter += 1
        }
    }
    if (openCounter == closedCounter){
        for (let j = 0; j < array.length; j++) {
        //// need to create condition where the loop returns false if parentheses are not in the correct order
        }
    }
    else (openCounter != closedCounter)
        return false;
    }

//////



console.log(parensValid("y(3(p)p(3)r)s"));
console.log(parensValid("n(0(p)3"));
console.log(parensValid("n)0(t(o)k"));
console.log(parensValid("((()))"));
console.log(parensValid("()()()()()()("));

// Given a string, returns whether the sequence of various parentheses, braces and brackets within it are valid. 

// Example 1: "({[({})]})" --> true
// Example 2: "d(i{a}l[t]o)n{e!" --> false
// Example 2: "{{[a]}}(){bcd}{()}" --> true

// hint: consider using an array or object to solve

function bracesValid(str) {
    // your code here
}

console.log(bracesValid("({[({})]})"));
console.log(bracesValid("d(i{a}l[t]o)n{e!"));
console.log(bracesValid("{{[a]}}(){bcd}{()}"));
console.log(bracesValid("{(})")); // false