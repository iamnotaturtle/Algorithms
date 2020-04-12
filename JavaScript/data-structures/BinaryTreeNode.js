export default class BinaryTreeNode {
  constructor(data) {
    this.data = data;
    this.left = null;
    this.right = null;
  }

  height() {
    return Math.max(
      this.right ? this.right.height() + 1 : 0,
      this.left ? this.left.height() + 1 : 0,
    );
  }

  size() {
    const right = this.right ? this.right.size() : 0;
    const left = this.left ? this.left.size() : 0;
    return right + left + 1;
  }

  isLeaf() {
    return !this.left && !this.right;
  }
}