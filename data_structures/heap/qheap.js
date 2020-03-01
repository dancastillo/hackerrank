class MinHeap {
  constructor() {
    this.items = [];
    this.size = 0;
  }

  getLeftChildIndex(index) {
    return 2 * index + 1;
  }

  getRightChildIndex(index) {
    return 2 * index + 2;
  }

  getParentIndex(index) {
    return Math.floor((index - 1) / 2);
  }

  hasLeftChild(index) {
    return this.getLeftChildIndex(index) < this.size;
  }

  hasRightChild(index) {
    return this.getRightChildIndex(index) < this.size;
  }

  hasParent(index) {
    return this.getParentIndex(index) >= 0;
  }

  leftChild(index) {
    return this.items[this.getLeftChildIndex(index)];
  }

  rightChild(index) {
    return this.items[this.getRightChildIndex(index)];
  }

  parent(index) {
    return this.items[this.getParentIndex(index)];
  }

  swap(indexOne, indexTwo) {
    const temp = this.items[indexOne];
    this.items[indexOne] = this.items[indexTwo];
    this.items[indexTwo] = temp;
  }

  peek() {
    if (this.size === 0) {
      return "None";
    }

    return this.items[0];
  }

  add(item) {
    this.items.push(item);
    this.size++;
    this.heapifyUp();
  }

  heapifyUp() {
    let index = this.size - 1;

    while (this.hasParent(index) && this.parent(index) > this.items[index]) {
      this.swap(this.getParentIndex(index), index);
      index = this.getParentIndex(index);
    }
  }

  heapifyDown() {
    let index = 0;

    while (this.hasLeftChild(index)) {
      let smallerChildIndex = this.getLeftChildIndex(index);

      if (
        this.hasRightChild(index) &&
        this.rightChild(index) < this.leftChild(index)
      ) {
        smallerChildIndex = this.getRightChildIndex(index);
      }

      if (this.items[index] < this.items[smallerChildIndex]) {
        break;
      } else {
        this.swap(index, smallerChildIndex);
      }

      index = smallerChildIndex;
    }
  }

  remove(value) {
    const index = this.items.indexOf(value);
    this.swap(index, this.size - 1);
    this.items.splice(this.size - 1, 1);
    this.size--;

    this.heapifyDown();
  }
}

heap = new MinHeap();

function processData(input) {
  const data = input.split("\n");
  const totalInputs = data[0];
  let index = 1;

  while (index <= data.length) {
    if (typeof data[index] !== "string") {
      break;
    }
    const dataInputs = data[index].split(" ");
    const command = +dataInputs[0];
    const value = dataInputs.length === 2 ? +dataInputs[1] : undefined;
    switch (command) {
      case 1:
        heap.add(value);
        break;
      case 2:
        heap.remove(value);
        break;
      case 3:
        console.log(heap.peek());
        break;
      default:
        break;
    }
    index++;
  }
}

process.stdin.resume();
process.stdin.setEncoding("ascii");
_input = "";
process.stdin.on("data", function(input) {
  _input += input;
});

process.stdin.on("end", function() {
  processData(_input);
});
