import Node from "./Node";

// Singly Linked List
// Space: O(n)
export default class LinkedList {
  constructor() {
    this._dummyHead = new Node();
    this._length = 0;
  }

  // insert
  insert(data, index) {
    const newNode = new Node(data);
    const firstNode = this._dummyHead.next;
    newNode.next = firstNode;
    this._dummyHead.next = newNode;
    this._length++;
    return this._length;
  }

  // remove

  // get
}
