import Node from './Node';

export default class Queue {
  constructor() {
    this.length = 0;
    this._head = undefined;
    this._tail = undefined;
  }

  enqueue(data) {
    const node = new Node(data);

    if (this.isEmpty()) {
      this._head = node;
      this._tail = node;
    } else {
      node.prev = this._tail;
      this._tail.next = node;
      this._tail = node;
    }
    this.length += 1;
  }

  dequeue() {
    if (!this.isEmpty()) {
      const data = this._head.data;
      this._head = this._head.next;
      this.length -= 1;
      return data;
    }
    return undefined;
  }

  front() {
    if (!this.isEmpty()) {
      return this._head.data;
    }
  }

  back() {
    if (!this.isEmpty()) {
      return this._tail.data;
    }
  }

  isEmpty() {
    return this.length === 0;
  }
}