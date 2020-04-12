import Node from './Node';

export default class Stack {
  constructor() {
    this._tail = null;
    this.length = 0;
  }

  push(data) {
    const node = new Node(data);
    node.next = this._tail;
    this._tail = node;
    this.length += 1;
  }

  pop() {
    if (this.isEmpty()) {
      return undefined;
    }
    const node = this._tail;
    this._tail = this._tail.next;
    this.length -= 1;
    return node.data;
  }

  peek() {
    if (this.isEmpty()) {
      return undefined;
    }

    return this._tail.data;
  }

  isEmpty() {
    return this.length === 0;
  }
}