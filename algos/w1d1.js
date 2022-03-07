// Create a function that, given a string, returns the string's acronym (first letter's only, capitalized) in string form.
// Example: "there's no free lunch - gotta pay yer way" --> "TNFL-GPYW""

// Things to consider: how to move through a string? How to capitalize letters? how to create/add to a new string?

// ===================================
// with Array?
// ===================================


// ===================================
// with new String only?
// ===================================
function acronym(str) {
    var temp = str[0]
    for (let i = 1; i < str.length; i++) {
        if (str[i]==" "){
            temp+= str[i+1]
        }
    }
    return temp.toUpperCase()
}

console.log(acronym("there's no free lunch - gotta pay yer way"));

// ==================================================================================================================
// Implement reverseString(str) that takes in a String, and then returns a string of the same length, but with the characters reversed.
// Example: "creature" ---> "erutaerc"
// ** Don't use the built-in reverse() method!

// ===================================
// with Array
// ===================================


// ===================================
// with new String only
// ===================================
function reverseString(str) {
    var temp = ""
    for (let i = str.length-1; i >= 0; i--) {
        temp += str[i]
    }
    return temp
}

console.log(reverseString("creature")); // "erutaerc"