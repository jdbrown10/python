//LINKED LISTS
//like an array without indexes
//reverse linked list  is a common interview problem
//i.e., "which data type is the best?" and the answer is singly linked list.
//the array becomes a LOT less efficient at larger levels because every time you add to it, the computer has to find a new spot in its memory for it. so that's why linked lists can be a lot more efficient at larger levels. A linked list can find a different place in its memory for each individual node, rather than needing to find one place to story everything together.
//it's called a singly linked list because it's only linked going forwards
//spoiler: a doubly linked list is linked forwards and backwards


class Node {
    constructor(value) { //the init method inside python is a constructor -> every language has some kind of constructor
        this.value = value;
        this.next = null; //INSIDE of the SLL stuff -> this is what connects us from node to node. Without this, we cannot move through the list.
    }

    // python equivalent of what's happening above:
    // def __init__(self==this, value):
    //     self.value = value
    //     self.next = null
}

class SLList {
    constructor() {
        this.head = null; //the head pointer ALWAYS points to the first thing in the SLL
        this.tail = null; //the tail pointer ALWAYS points to the last thing in the SLL
    }

    addToFront(value) {
        // #1 create our new node
        var newNode = new Node(value);

        if (this.head == null) {
            this.head = newNode;
            this.tail = newNode;
            return this
        }

        // #2 connect the new node to the list
        newNode.next = this.head;

        // #3 verify that our pointers are correct
        this.head = newNode;
    }

    addToBack(value) {
        // #1 - create new node
        var newNode = new Node(value);
        // #2 - connecting new node to the sll
        this.tail.next = newNode;

        if (this.head == null) {
            this.head = newNode;
            this.tail = newNode;
            return this
        }

        // #3 - verify pointers are correct
        this.tail = newNode;
    }

    printValues() {
        //what if the list is empty?
        if (this.head == null) {
            console.log('This list is empty.')
        } else { //we use a runner to check through the list
            var runner = this.head
            while (runner != null) { //as long as runner has some value...
                console.log(runner.value); //console.log the value of runner...
                runner = runner.next; //and then move to the next node in the SLL!
            }
            console.log("This is the end of the list!")
        }
    }

    contains(value) {
        if (this.head == null) {
            console.log('This list is empty.')
        } else { //we use a runner to check through the list
            var runner = this.head
            while (runner != null) { //as long as runner has some value...
                if (runner.value == value) { //see if the value of runner is equal to the value from the function (on line 74)
                    return true
                }
                runner = runner.next; //and then move to the next node in the SLL!
            }
            return false
        }
    }
    removeFromFront() {
        if (this.head == null) {
            console.log('This list is empty.')
        } else {
            var temp = this.head;
            this.head = this.head.next;
            temp = null; //makes it so that if temp is accessed, it's pointing into nothingness and can't get into the list
            return this
        }
    }
    removeFromBack() {
        if (this.head == null) {
            console.log('This list is empty.')
        } else if (this.head==this.tail){
            console.log('This list only has one value!') //remember to talk to your interviewer and ask how they want you to handle edgecases
        } else {
            var runner = this.head
            var secondRunner = this.head.next
            while (secondRunner.next != null) {
                runner = runner.next;
                secondRunner = runner.next;
                // console.log('============')
                // console.log(runner)
                // console.log(secondRunner)
            }
            runner.next = null
            runner = this.tail
            return this
            // secondRunner = null
        }
    }
}

var sll = new SLList();

sll.addToFront(6);
sll.addToFront(1);
sll.addToFront(22);
sll.addToBack(9);
sll.addToBack(12);
sll.addToBack(47);
sll.printValues();
sll.removeFromBack();
sll.printValues();
sll.removeFromFront();
sll.printValues();

sll.printValues();
console.log('================')
console.log(sll.contains(9))
console.log(sll.contains(47))
console.log(sll.contains(25))



