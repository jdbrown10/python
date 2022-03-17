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
        } else if (this.head == this.tail) {
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

    //locate the node with lowest value, remove it from its current location, move it to the front of the SLL
    //consider edge cases-- if list is empty, if it has one item, if there are two with the same value, if it's already the first or if it's the last (will need to move the tail marker as well)
    minToFront() {
        var min = this.head;
        var runner = this.head;
        var walker;

        while (runner.next != null) { //find the location of the minimum within the list
            if (runner.next.value < min.value) { //if the next node value is less than the current min node...
                min = runner.next; //...then set the min node to be the next node...
                walker = runner;//...and put the walker wherever the runner is (right before the new min node)
            }
            runner = runner.next;
        }
        if (min == this.head) { //edge case: if the min is already at the front-- never changed during while loop
            console.log("This min is already at the front!")
            return this //terminates the function right here!
        }
        if (this.tail == min) { //edge case: if the tail is the min-- need to handle the tail attribute
            this.tail = walker; //set the tail equal to the walker -- the walker is one before the tail, so if the tail is the min and we are moving it, the walker needs to becme the new tail
        }

        walker.next = min.next; // this stops us from having a circle that cuts off everything after the min-- it changes the walker pointer (which was before the min) to point at the node after the min
        min.next = this.head; //points the min at the head of the list (moving it to the front)
        this.head = min //change the head marker to the min (which is now at the front because of the above line of code)
    }


    //
    maxToBack() {
        var max = this.head;
        var runner = this.head;
        var walker;

        while (runner.next != null) {
            if (runner.next.value > max.value) { //if the next value is GREATER than the current max node...
                max = runner.next;//...then set the max node to be the next node...
                walker = runner;//...and put the walker wherever the runner is (right before the new max node)
            }
            runner = runner.next; //move to the next node in the SLL
        }

        if (max == this.tail) {//edge case-- if the max is already at the end
            console.log("Max is already at the end!")
            return this;
        }

        if (max == this.head) { //edge case- if the max is the head, have to deal with head marker
            this.tail.next = max; //points the tail to the max (which makes a loop)
            this.head = this.head.next; //changes the head to be one AFTER where the head was (which was originally the max) -> the head is now effectively the second node in the SLL
            this.tail = max; //gives the max node (which is at the end) the tail marker
            this.tail.next = null; //points the tail (which is now also the max node) out into nothingness, stopping the loop
            return this;
        }

        walker.next = max.next; //leapfrog over the max node. points the node BEFORE the max node to the node AFTER the max node. Max node is now floating by itself
        this.tail.next = max; //points the tail node of the SLL at the max node, moving it to the end
        max.next = null; //sets the next node after max node to be nothingness
        this.tail = max; //moves the tail marker to the max node, which is now at the end
    }

    //find the location in the list and add a node with the given value AFTER that location
    appendVal(value, loc) { // loc = 2, this is the 3rd position in the list

        //we already have a function for this! just use it! this is in case the list is shorter than the location value, or if we land on the tail-- just add it to the back
        if(this.length <= loc) {
            this.addToBack(value) 
            return
            }

        if (this.head == null){
            console.log("This list is empty!")
            return this
        }
        //create a new node, set runner equal to head, and initialize sentry for the while loop
        var newNode = new Node(value);
        var runner = this.head;
        var i = 0
        while (i < loc) { //get to the location
            i++;
            runner = runner.next; //move to the next node in the SLL
        }
        
        // change the pointers around so the new node is in the proper place in the list
        newNode.next = runner.next
        runner.next = newNode
    }


    //find the location in the list and add a node with the given value BEFORE that location
    prependVal(value, loc) {
        
        //edge case for if we're prepending to the start of the list-- use the function we already built
        if(loc = 0) {
            this.addToFront(value) 
            return
            }

        var newNode = new Node(value);
        var runner = this.head;
        var i = 0

        while(i < loc - 1) { //get to one before the location (but stop once we get to the end)
            i++;
            runner = runner.next; // increment to the next node in the SLL
        }
        newNode.next = runner.next
        runner.next = newNode

    }
    
}

var sll = new SLList();

sll.addToFront(6);
sll.addToFront(1);
sll.addToFront(22);
sll.addToBack(9);
sll.addToBack(12);
sll.addToBack(47);
sll.prependVal(100, 0)
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