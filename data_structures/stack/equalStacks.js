'use strict';

const fs = require('fs');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

class Stack {
    constructor() {
        this.size = 0;
        this.items = [];
    }

    push(item) {
        this.items.push(item);
        this.size += item;
    }

    pop() {
        const item = this.items.pop();
        // console.log('size:', this.size)
        this.size -= item;
        // console.log('size:', this.size)
    }

    total() {
        return this.size;
    }
}

function loadStack(items) {
    const stack = new Stack();
    for (let i = items.length -1 ; i >= 0; i--) {
        stack.push(items[i]);
    }
    return stack;
}

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(str => str.trim());

    main();
});

function readLine() {
    return inputString[currentLine++];
}

/*
 * Complete the equalStacks function below.
 */
function equalStacks(h1, h2, h3) {
    /*
     * Write your code here.
     */
    const s1 = loadStack(h1);
    const s2 = loadStack(h2);
    const s3 = loadStack(h3);

    while (true) {
        if (s1.total() === 0 || s2.total() === 0 || s3.total() === 0) {
            return 0;
        }

        if (s1.total() === s2.total() && s2.total() === s3.total()) {
            return s1.total();
        }

        if (s1.total() >= s2.total() && s1.total() >= s3.total()) {
            s1.pop();
        } else if (s2.total() >= s1.total() && s2.total() >= s3.total()) {
            s2.pop()
        } else if (s3.total() >= s1.total() && s3.total() >= s2.total()) {
            s3.pop();
        }

    }
}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const n1N2N3 = readLine().split(' ');

    const n1 = parseInt(n1N2N3[0], 10);

    const n2 = parseInt(n1N2N3[1], 10);

    const n3 = parseInt(n1N2N3[2], 10);

    const h1 = readLine().split(' ').map(h1Temp => parseInt(h1Temp, 10));

    const h2 = readLine().split(' ').map(h2Temp => parseInt(h2Temp, 10));

    const h3 = readLine().split(' ').map(h3Temp => parseInt(h3Temp, 10));

    let result = equalStacks(h1, h2, h3);

    ws.write(result + "\n");

    ws.end();
}
