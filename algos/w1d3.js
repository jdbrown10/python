//Create a function that returns a boolean t/f for whether or not an input string is a strict palindrome--same casing and spaces

// function isPallindrome(str){
//     var ogStr = str
//     for (let i = str.length - 1; i > str.length/2; i--) {
//         var j = 0;
//         var temp = str[j];
//         str[j] = str[i]
//         str[i] = temp
//         j++;
//     }
//     if (str == ogStr) {
//         return true
//     }
//     else
//         return false
// }

function isPallindrome(str) {
    var verdict = "true"
    for (let i = 0; i < str.length / 2; i++) {
        if (str[i] == str[str.length - 1 - i]) {
            verdict = "true"
            // console.log("first")
        }
        else {
            // console.log("second")
            return false
        }
    }
    if (verdict == "true") {
        return true
    }
}
console.log(isPallindrome("racecar")) //true
console.log(isPallindrome("e tacocat e")) //true
console.log(isPallindrome("Dud")) //false
console.log(isPallindrome("oho!")) //false
console.log(isPallindrome(" to ")) //false




// Given a String, return the longest pallindromic substring. Given "hello dada", return "dad". Given "not much" return "n". Include spaces as well!

// Example 1: "my favorite racecar erupted" --> "e racecar e"
// Example 2: "nada" --> "ada"
// Example 3: "nothing to see" --> "ee"

//PSEUDOCODE
//1. newArray[i] -> check if it occurs at another index within the array, starting from the end of the array, and then checking inwards
//2. IF it does occur, loop will pause at first occurance, and range will be set between newArray[i] and newArray[occurance]
//3. check if it's a palindrome -> if it is, push the palindrome into an array
//4. go to next occurance of newArray[i] if it exists within the array and set new range
//5. if the new palindrome is bigger than the previous, replace it in the array
//6. repeat 3+4 until there are more occurances
//7. i++, re-iterate the loop
//8. return the array holding the palindrome
//9. OR, if there's no palindrome, return the first character in the string

function longestPallindrome(str) {
    var newArray = str.split('')
    for (let i = 0; i < newArray.length; i++) {
        //code here
    }
}

console.log(longestPallindrome("nada"));
console.log(longestPallindrome("my favorite racecar erupted"));
console.log(longestPallindrome("nothing to see"));