import Node from "./Node";

// Pay attention to both nodes
// Space: O(n)
export default class DoublyLinkedList {
  constructor() {
    this.length = 0;
    this._dummyHead = new Node();
    this._dummyTail = new Node();
    this._dummyHead.next = this._dummyTail;
    this._dummyTail.prev = this._dummyHead;
  }

  // Add to end
  // O(1)
  push(data) {
    const node = new Node(data);
    const prevNode = this._dummyTail.prev;
    prevNode.next = node;
    node.prev = prevNode;
    node.next = this._dummyTail;
    this._dummyTail.prev = node;
    this.length += 1;

    return this.length;
  }

  // Add to front
  // O(1)
  unshift(data) {
    const node = new Node(data);
    const nextNode = this._dummyHead.next;
    nextNode.prev = node;
    node.next = nextNode;
    this._dummyHead.next = node;
    this.length += 1;
    return this.length;
  }

  // Remove from front
  // O(1)
  shift() {
    if (this.isEmpty()) {
      return undefined;
    }
    const node = this._dummyHead.next;
    const firstNode = node.next;

    this._dummyHead.next = firstNode;
    firstNode.prev = this._dummyHead;

    this.length--;
    return node.data;
  }

  // Remove from end
  // O(1)
  pop() {
    if (this.isEmpty()) {
      return undefined;
    }

    const node = this._dummyTail.prev;
    const lastNode = node.prev;
    lastNode.next = this._dummyTail;
    this._dummyTail.prev = lastNode;
    this.length -= 1;

    return node.data;
  }

  // returns head node
  front() {
    return this._dummyHead.next.data;
  }

  // returns tail node
  back() {
    return this._dummyTail.prev.data;
  }

  isEmpty() {
    return this.length === 0;
  }

  toArray() {
    var currNode = this._dummyHead.next;
    const values = [];
    while (currNode !== this._dummyTail) {
      values.push(currNode.data);
      currNode = currNode.next;
    }
    return values;
  }

  static fromArray(array) {
    const list = new DoublyLinkedList();
    array.forEach(el => list.push(el));
    return list;
  }
}
