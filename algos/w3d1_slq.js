//SINGLY LINKED QUEUE

class Node{
    constructor(value){
        this.value = value
        this.next = null
    }
}

// a queue operates on the principal of "First In, First Out" like waiting in line for something
class SLQueue{
    constructor() {
        this.head = null
        this.tail = null
    }

    // add a node with the given value to the queue
    enqueue(value) {
        // #1 - create new node
        var newNode = new Node(value);

        // #2 - connecting new node to the sll
        if (this.isEmpty()) { //in case the queue is empty
            console.log("Adding to list...")
            this.head = newNode;
            this.tail = newNode;
            return this
        }
        
        this.tail.next = newNode;

        // #3 - verify pointers are correct
        this.tail = newNode;
    }

    // remove and return the front value from the queue
    dequeue() {
        if (this.isEmpty()) {
            return this
        } else {
            var temp = this.head.value;
            this.head = this.head.next;
            // temp = null; //makes it so that if temp is accessed, it's pointing into nothingness and can't get into the list
            return temp
        }
    }

    //return true/false based on whether you find the given value in a queue
    contains(value) {
        if (this.isEmpty()) {
            return this
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

    displayQueue(){
        //what if the list is empty?
        if (this.isEmpty()) {
            return this
        } else { //we use a runner to check through the list
            var runner = this.head
            while (runner != null) { //as long as runner has some value...
                console.log(runner.value); //console.log the value of runner...
                runner = runner.next; //and then move to the next node in the queue!
            }
            console.log("This is the end of the list!")
            console.log("============================")
        }
    }
    
    // return the value of the front node without removing from list
    front() {
        return this.isEmpty() ? this : this.head.value
        // if (this.isEmpty()){
        //     return this
        // } else {
        //     return this.head.value
        // }
    }


    // return whether or not a list is empty
    isEmpty() {
        return this.head == null ? true : false
        // if (this.head == null){
        //     console.log("This queue is empty... f")
        //     return true
        // } else {
        //     return false
        // }
    }
}

var q = new SLQueue();
console.log(q.isEmpty());
console.log(q.front());
q.enqueue(1);
q.enqueue(2);
q.enqueue(3);
q.enqueue(4);
q.enqueue(5);
q.enqueue(6);
q.displayQueue();
console.log("==================================");
q.dequeue();
q.displayQueue();
q.dequeue();
q.displayQueue();
console.log("==================================");
console.log(q.front());
console.log(q.isEmpty());