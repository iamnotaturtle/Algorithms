import BinaryTreeNode from './BinaryTreeNode';

export default class BinaryTree {
  constructor(data) {
    if (data) {
      this._root = new BinaryTreeNode(data);
    }
  }

  getRoot() {
    return this._root;
  }

  size() {
    return this._root ? this._root.size() : 0;
  }

  height() {
    return this._root ? this._root.height() : 0;
  }

  inOrder() {
    let array = [];
    const inOrder = (node) => {
      if (!node) {
        return;
      }

      node.left ? inOrder(node.left) : null;
      array.push(node.data);
      node.right ? inOrder(node.right) : null;
    }
    inOrder(this._root);
    return array;
  }

  preOrder() {
    let array = [];
    const preOrder = (node) => {
      if (!node) {
        return;
      }

      array.push(node.data);
      node.left ? preOrder(node.left) : null;
      node.right ? preOrder(node.right) : null;
    }
    preOrder(this._root);
    return array; 
  }

  postOrder() {
    let array = [];
    const postOrder = (node) => {
      if (!node) {
        return;
      }

      node.left ? postOrder(node.left) : null;
      node.right ? postOrder(node.right) : null;
      array.push(node.data);
    }
    postOrder(this._root);
    return array; 
  }
}