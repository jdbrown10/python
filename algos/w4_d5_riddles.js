
// Word/Logic Problems!


//PIRATES

// There are 5 pirates, they must decide how to distribute 100 gold coins among them. The pirates have seniority levels, the senior-most is A, then B, then C, then D, and finally the junior-most is E. 


// Rules of distribution are: 

//     The most senior pirate proposes a distribution of coins.
//     All pirates vote on whether to accept the distribution.
//     The distribution is approved if at least half of the pirates agree (including the proposer)
//     If the distribution is accepted, the coins are disbursed and the game ends.
//     If not, the proposer is nixxed (un-alived), and the next most senior pirate makes a new proposal to begin the system again.
//     In case of a tie vote, the proposer can have the casting vote

// Rules every pirate follows.

//     Every pirate wants to survive
//     Given survival, each pirate wants to maximize the number of gold coins he receives.







// What is the maximum number of coins that pirate A might get? And why?


// =======================================================

//HORSES

// Find the Fastest Horse!

// There are 25 horses among which you need to find out the fastest 3 horses. You can conduct race among at most 5 to find out their relative speed. At no point you can find out the actual speed of the horse in a race. Find out the minimum no. of races which are required to get the top 3 horses. 

//horses 1-5 race each other and select the fastest one
//fastest horse races horses 6-9
//that winner races 10-13
//that winner races 14-17
//that winner races 18-21
//that winner races 22-25

//then we know the fastest horse, remove them from group of 25

//now there are 24 horses

//horses 1-5 race each other and select the fastest one
//fastest horse races horses 6-9
//that winner races 10-13
//that winner races 14-17
//that winner races 18-21
//that winner races 22-24

//then we know the second fastest horse, remove them from group of 24

//now there are 23 horses

//horses 1-5 race each other and select the fastest one
//fastest horse races horses 6-9
//that winner races 10-13
//that winner races 14-17
//that winner races 18-21
//that winner races 22-23

//now we know the third fastest horse

//this is 18 races total (how can we do this faster though?)








// =======================================================

//ZEBRAS

// The Zebra Puzzle:

// The puzzle consists of five different-colored houses in a row, each lived in by a resident of a different nationality.
//  Each resident owns a different pet, prefers a different drink, and smokes a different brand of cigarettes than the others.

// You’re given 15 other facts:

// There are five houses.
// The Englishman lives in the red house.
// The Spaniard owns the dog.
// Coffee is drunk in the green house.
// The Ukrainian drinks tea.
// The green house is immediately to the right of the ivory house (to your right as you stand facing the row of five houses).
// The Old Gold smoker owns snails.
// Kools are smoked in the yellow house.
// Milk is drunk in the middle house.
// The Norwegian lives in the first house.
// The man who smokes Chesterfields lives in the house next to the man with the fox.
// Kools are smoked in a house next to the house where the horse is kept.
// The Lucky Strike smoker drinks orange juice.
// The Japanese smokes Parliaments.
// The Norwegian lives next to the blue house.
// To solve the puzzle, tell me:

// 1) Which man likes to drink water

// 2) Which man owns a zebra