// Write a function that given a sorted array of page numbers, return a string representing a book index. 
// Combine consecutive pages to create ranges.

// Example: [1,3,4,5,7,8,10,12] --> "1, 3-5, 7-8, 10, 12"


function bookIndex(arr) {
    var temp = []
    var finalStr = ""
    for (let i = 0; i < arr.length; i++) {
        if (arr[i + i] == arr[i] + 1) {
            temp.push(arr[i]);
        }
        else if (temp.length > 0) {
            temp.push(arr[i]);
            finalStr += temp[0] + "-" + temp[temp.length - 1] + ','
            temp = [];
        }
        else
            finalStr += arr[i] + ','
    }
    return finalStr;
}

console.log(bookIndex([1, 3, 4, 5, 7, 8, 10, 12]))


/////////

function bookIndex(arr){
    var str = "";
    
    for (let i = 0; i < arr.length; i++) {
        if (i < arr.length && i !== 0){
            str += ", "
        };
        
        if (arr[i+1] === arr[i] + 1){
            var start = arr[i];
            while(arr[i+1] === arr[i] + 1){
                i++
            }
            var end = arr[i];
            str += start + "-" + end;
        }
        
        else{
            str += arr[i]
        }
    }
    return str
}

console.log(bookIndex([1, 3, 4, 5, 7, 8, 10, 12]))