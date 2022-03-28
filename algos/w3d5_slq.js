class Node {
    constructor(value) {
        this.value = value
        this.next = null
    }
}

// a queue operates on the principal of "First In, First Out" like waiting in line for something
class SLQueue {
    constructor() {
        this.head = null
        this.tail = null
    }

    // add a node with the given value to the queue
    // similar to SLL - add to back
    enqueue(value) {
        var newNode = new Node(value);

        if (this.head == null) {
            this.head = newNode;
            this.tail = newNode;
        } else {
            this.tail.next = newNode;
            this.tail = this.tail.next;
        }
        return this;
    }

    // remove and return the front value from the queue
    // similar to SLL - remove from front
    dequeue() {
        if (!this.head) {
            console.log("Nothing in this queue!");
            return null;
        }
        var temp = this.head;
        this.head = this.head.next;
        temp.next = null;
        return temp.value;
    }

    //return true/false based on whether you find the given value in a queue
    // same as contains in SLL
    contains(value) {
        if (!this.head) {
            return false;
        }
        var runner = this.head;
        while (runner) {
            if (runner.value === value) {
                return true;
            }
            runner = runner.next;
        }
        return false;
    }

    // remove the minimum value in the queue (remember your edgecases and pointers!)
    removeMin() {
        if (this.head == null) {
            console.log("Nothing in this queue!")
            return null
        }

        var runner = this.head;
        var min = runner.value;

        while (runner != null) {
            if (runner.value < min) {
                min = runner.value
            }
            runner = runner.next
        }

        runner = this.head;
        // if the min is at the front
        if (runner.value == min) {
            this.dequeue();
        }
        // if the min is in the queue
        while (runner.next.next != null) {
            if (runner.next.value === min) {
                runner.next = runner.next.next
                return this;
            }
            else {
                runner = runner.next
            }
        }
        // if the min is at the end of the queue
        if (runner.next.value == min) {
            this.tail = runner
            runner.next == null
        }
    }

    displayQueue() {
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
        // if(!this.head) {
        //     return null;
        // } else {
        //     return this.head.value;
        // }

        return this.head == null ? null : this.head.value;
    }

    // return whether or not a list is empty
    isEmpty() {
        // if(!this.head) {
        //     return "It's empty!"
        // } else {
        //     return "It's not empty!"
        // }

        // evaluates to the opposite of what you are expecting
        // if this.head exists, we are returning the 'not' of that, so it would output false
        // if this.head is null, we are returning the 'not' of that as well, so it would return true
        return this.head === null;
        // return !this.head;
    }


    // given a queue, determine whether or not the values therein are a pallindrome 
    // Ex: 1 --> 2 --> 3 --> 2 --> 1 --> null
    // any values that are in the same order going forwards as backwards is a pallindrome, doesn't need to just be letters
    isPallindrome() {
        if (!this.head || !this.head.next) {
            console.log("technically true cuz nothing or 1 thing is the same to and fro...")
            return true
        }
        // collect values into a array so I can compare them to the items in the list
        var runner = this.head;
        var comparer = [];
        while (runner) {
            comparer.push(runner.value);
            runner = runner.next;
        }

        // compare items in the array starting from the end, to the items in the queue starting from the front
        var newRunner = this.head;
        // only need to go halfway through
        for (var i = comparer.length - 1; i > Math.floor(comparer.length / 2); i--) {
            if (comparer[i] != newRunner.value) {
                return false
            }
            newRunner = newRunner.next
        }
        console.log("Neato! It's a palli :)")
        return true
    }

    size() {
        var runner = this.head;
        var count = 0;
        while (runner) {
            count++;
            runner = runner.next;
        }
        return count;
    }


    // Reorder SLQueue values to alternate first half values with second half values, in order. For example: (1,2,3,4,5) becomes (1,4,2,5,3). You may create one additional SLQueue, if needed.

    // 1 --> 2 --> 3 --> 4 --> 5 --> 6
    // 1 --> 2 --> 3 -->    |      4 --> 5 --> 6 -->
    // 1 --> 4 --> 2 --> 5 --> 3 --> 6 -->
    // INSTRUCTOR SOLUTION
    // Interleave() {
    //     /* make a new queue */
    //     let q = new Queue();
    //     /* make two runners */
    //     let node1 = this.head;
    //     let node2 = this.head;
    //     /* make second runner start at the halfway point */
    //     for (let i = 0; i < this.size >> 1; i++) {
    //         node2 = node2.next;
    //     }
    //     /* until we have the same amount of elements as the original, keep iterating */
    //     for (; q.size < this.size;) {
    //         /* push first runner value */
    //         q.Push(node1.value);
    //         /* push second runner value */
    //         q.Push(node2.value);
    //         /* update first runner */
    //         node1 = node1.next;
    //         /* update second runner */
    //         node2 = node2.next;
    //     }
    //     return q;
    // }

    // instructor solution
    HasLoop() {
        for (let node = this.head; node; node = node.next) {
            /* if we have visited the node before, we know we have an infinite loop. */
            if (node.visited) return true;
            /* store a visited bool as we iterate each node. */
            node.visited = true;
        }
        /* if we got here, there is not an infinite loop. */
        return false;
    }

    interleaveQueue() {
        // get every other node in the queue put them into their own new queue
        // change the pointers of the remaining nodes to skip over those nodes
        // create a new queue by taking one node from each queue at a time and changing its .next pointer to the next node in the other queue
        if (!this.head) {
            console.log("This queue is empty.");
        }
        else {
            var middle = this.head
            var length_finder = this.head
            var runner = this.head
            var final_runner
            var final_middle
            var queue_length = 0
            //get queue_length
            while (length_finder.next != null) {
                length_finder = length_finder.next
                queue_length += 1
            }
            queue_length += 1
            //iterate to get one past the middle
            for (let i = 0; i < queue_length / 2; i++) {
                middle = middle.next;
            }
            while (middle.next != null) {
                var temp_runner = runner.next
                var temp_middle = middle.next
                runner.next = middle
                middle.next = temp_runner
                runner = temp_runner
                middle = temp_middle
                final_runner = runner
                final_middle = middle
                // if (middle.next != null)
                //     console.log("runner: [" + runner.value + "] runner.next [" + runner.next.value + "] middle: [" + middle.value + "] middle.next [" + middle.next.value + "]")
                // else
                //     console.log("runner: [" + runner.value + "] runner.next [" + runner.next.value + "] middle: [" + middle.value + "]")
            }
            final_runner.next = final_middle
            this.tail = final_middle

            //     var testRun = this.head
            //     for (var i = 0; i < 6; i++)
            //         console.log (testRun)
            //         testRun = testRun.next
        }
    }

    // return true/false if the queue has a loop!
    // this one is mostly intended for white boarding, but if you can figure out how to create a loop in your code, you may do that as well!
    //     hasLoop() {
    //     }


}


var q = new SLQueue();
q.enqueue(1);
q.enqueue(2);
q.enqueue(3);
q.enqueue(4);
q.enqueue(5);
q.enqueue(6);
q.interleaveQueue();


// q.isPallindrome();