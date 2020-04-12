import BinaryTreeNode from './BinaryTreeNode';
import BinaryTree from './BinaryTree';

export default class BinarySearchTree extends BinaryTree {

  insert(data) {
    if (!this._root) {
      const node = new BinaryTreeNode(data);
      this._root = node;
      return;
    }

    const _insert = (data, node) => {
      if (data < node.data && node.left) {
        _insert(data, node.left);
      } else if (data < node.data) {
        const child = new BinaryTreeNode(data);
        node.left = child;
      } else if (data > node.data && node.right) {
        _insert(data, node.right);
      } else if (data > node.data) {
        const child = new BinaryTreeNode(data);
        node.right = child;
      }
    }

    _insert(data, this._root);
  }

  search(data) {
    const _search = (data, node) => {
      if (!node) {
        return false;
      }

      if (node.data === data) {
        return true;
      } else if (data < node.data) {
        return _search(data, node.left);
      } else {
        return _search(data, node.right);
      }
    }

    return _search(data, this._root);
  }

  getMinimum() {
    if (!this._root) {
      return null;
    }

    const getMin = (node) => {
      if (node.isLeaf()) {
        return node.data;
      }

      return getMin(node.left);
    };

    return getMin(this._root);
  }

  getMaximum() {
    if (!this._root) {
      return null;
    }

    const getMax = (node) => {
      if (node.isLeaf()) {
        return node.data;
      }

      return getMax(node.right);
    };

    return getMax(this._root);
  }
}