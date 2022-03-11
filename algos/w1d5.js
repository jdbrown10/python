// Given a dollar amount with change (an integer w/decimal) convert to change. Make sure to count the largest denomination first!

// Example: 3.21 --> 12 quarters, 2 dimes, 1 penny

// function convertCoinChange(money) {
//     // declare variables for different denominations (quarter, dime, nickel, penny)
//     q = 0 // each variable holds the count of each coin
//     d = 0
//     n = 0
//     p = 0 

//     // multiply input by 100 : 3.21 == 321
    
//     // take new number (321) and divide by 25 to get the number of quarters
//     // make sure to round down to get a whole number
//     // subtract the (# of quarters * 25) from the overall input # and then check the next denomination
//     // repeat for different denominations
//     // print and then return the data you collected


// 3.21/.25 = 12 quarters 21 cents left over. subtract out 3 dollars worth of quarters 
// remainder .21 cents
//DIMES 
// remainder /.10 = 2 dimes => 0.01 penny
// NICKLES
// 0.01/ .05 => zero nick
// PENNIES
//# function checkRemainCoin():
// if remainder < .05: <= rewrite multiple times. 
// console.log(0 nickles)


// }

var money = 3.21
var money_2 = 42.05
function generateCoinChange(money) {
    q = 0 // each variable holds the count of each coin
    d = 0
    n = 0
    p = 0 
    //multiply input by 100 : 3.21 == 321
    money *= 100
// take new number (321) and divide by 25 to get the number of quarters
// 321/25 = 12.84
    q = Math.floor(money/25)
    console.log(q)
    money %= 25
    console.log(money)

    // dimes 
    d = Math.floor(money/10)
    console.log(d)
    money %= 10
    console.log(money)
    
    //nickles
    n = Math.floor(money/5)
    console.log(n)
    money %= 5
    console.log(money)

    //pennies
    p = Math.floor(money/1)
    console.log(p)
    money %= 1
    // console.log(money)

    //print statement 
    // Example: 3.21 --> 12 quarters, 2 dimes, 1 penny
    console.log(`${q} quarters, ${d} dimes, ${n} nickles, ${p} pennies`)

}






//REFACTOR
function generateCoinChange(money) {

    money = Math.floor(money*100)
    
    finalCoinValues = []

    const coins = {
        quarter:25, 
        dime:10, 
        nickel:5,
        penny:1
    };

    for (var key in coins) {
        finalCoinValues.push(Math.floor(money/coins[key]))
        money %= coins[key]
    }

    console.log(`${finalCoinValues[0]} quarters, ${finalCoinValues[1]} dimes, ${finalCoinValues[2]} nickles, ${finalCoinValues[3]} pennies`)
}

generateCoinChange(1.73)