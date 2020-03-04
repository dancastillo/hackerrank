class Stack {
    constructor () {
        this.items = [];
    }

    push(item) {
        this.items.push(item);
    }

    pop() {
        this.items.pop();
    }

    largest() {
         return Math.max( ...this.items );
    }
}
function processData(input) {
    //Enter your code here
    const inputArray = input.split('\n').slice(1);
    const stack = new Stack();

    inputArray.forEach(line => {
        const operation = line.split(' ');

        if (operation[0] === '1') {
            stack.push(+operation[1]);
        } else if (operation[0] === '2') {
            stack.pop();
        } else if (operation[0] === '3') {
            console.log(stack.largest());
        }
    });
} 

process.stdin.resume();
process.stdin.setEncoding("ascii");
_input = "";
process.stdin.on("data", function (input) {
    _input += input;
});

process.stdin.on("end", function () {
   processData(_input);
});
