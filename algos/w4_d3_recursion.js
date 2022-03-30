// Write a function that, given a sorted array and a value, determines whether the value is found within the array through 
// recursively searching, and returns the index. Binary Search works by checking whether the value given is greater than or 
// less than a midway point, which is why the given array must be sorted. 
// Also, even though there's only an array and value given, you can add additional parameters to your function.
// Return -1 if the number is not in the array

// val = 9
// arr = [1,2,3,5,7,9,10 ,11,13,14,15,56,78]

// [1,2,3,5,7,9,10      |        11,13,14,15,56,78] <----- 9 is less than halfway so now you can search the left side only
// [1,2,3,5,       |        7,9,10] <------  9 is greater than halfway so you can search the right side only
// [7,      |       9,10] <------ depending on where you split,9 is greater than halfway
// [9,     |      10] <------ whittle down to 1 or 2 items to check and solve!




// make sure the function returns the index and not the value -- so part of the challenge is to keep track of the original index
// don't use splice or slice functions


function recursiveBinarySearch(val, arr, start_index = 0, end_index = arr.len-1) {
    midpoint = Math.floor((start_index + end_index) / 2)
    
    if (arr[midpoint] == val) {
        console.log(midpoint)
        return midpoint
    } else if (arr[midpoint] > val) {
        end_index = midpoint
        recursiveBinarySearch(val, arr, start_index, end_index)
    } else if (arr[midpoint] < val) {
        start_index = midpoint + 1
        recursiveBinarySearch(val, arr, start_index, end_index)
    } else if (start_index == end_index && arr[start_index] != val) {
        console.log(-1)
        return -1
    }
}


recursiveBinarySearch(3, [-1, 0, 1, 2, 3, 4, 5, 6])



function iterativeBinarySearch(val, arr) {
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] == val) {
            console.log(i)
            return i
        }
    }
    console.log(-1)
    return -1
}

iterativeBinarySearch(10, [2, 3, 4, 5, 6, 7, 8])



// [1, 2], ---> -2
// [1, 2], ---> 4
// [1, 2], ---> 1
// [1,2,2], ---> 2
// [], ---> 7
// [1,2,2,2,2,2,2,4,5,5,5,5,6,6,6], ---> 2
// [1, 1, 1, 1, 1], ---> 1
// [1, 2, 3, 3, 4, 4, 5, 6, 7, 8, 8, 9, 10], ---> 8
// make sure to test all given scenarios!
// extra challenge: don't use built-in functions such as splice() or slice(), 
// with the exception of rounding functions (Math.floor(), Math.ceil())