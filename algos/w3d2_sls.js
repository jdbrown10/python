//singly linked stack -- it's like a can of pringles!

class Node{
    constructor(value){
        this.value = value
        this.next = null
    }
}

// a stack operates on the principal of "First In, Last Out" like a pringles can
class SLStack{
    constructor() {
        this.top = null
    }

    // add a given value to your stack (add to the top)
    push(value){
        // #1 create our new node
        var newNode = new Node(value);

        if (this.top == null) {
            this.top = newNode;
            return this
        }

        // #2 connect the new node to the list
        newNode.next = this.top;

        // #3 verify that our pointers are correct
        this.top = newNode;
    }
    
    // remove and return the top value
    pop(){
        if (this.top == null) {
            console.log('This stack is empty.')
            return null
        } else {
            var temp = this.top.value;
            this.top = this.top.next;
            return temp
        }
    }

    // return (don't remove) the top value of a stack
    returnTop() {
        if (this.top == null) {
            console.log('This stack is empty.')
        } else {
            return this.top.value;
        }
    }

    printStack() {
        //what if the stack is empty?
        if (this.top == null) {
            console.log('This stack is empty.')
        } else { //we use a runner to check through the stack
            var runner = this.top
            while (runner != null) { //as long as runner has some value...
                console.log(runner.value); //console.log the value of runner...
                runner = runner.next; //and then move to the next node in the SLS!
            }
            console.log("This is the end of the stack!")
        }
    }
}

var sls = new SLStack()
sls.push(3)
push(18)
push(12)
sls.push(78)
sls.push(56)
sls.printStack()
console.log('==========')
console.log(sls.pop())
console.log('==========')
console.log(sls.returnTop())
console.log('==========')
sls.printStack()