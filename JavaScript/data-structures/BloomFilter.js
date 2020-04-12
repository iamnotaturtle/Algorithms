const defaultHashFunctions = [
  x => (25 * x + 13) % 31,
  x => (109 * x + 71) % 139,
  x => (677 * x + 241) % 859,
  x => (547 * x + 383) % 997,
  x => (173 * x + 149) % 499,
];

export default class BloomFilter {
  constructor(size, hashFunctions) {
    this._size = size;
    this._bits = new Array(size).fill(false);
    this._hashFunctions = hashFunctions ? hashFunctions : defaultHashFunctions;
  }

  add(data) {
    this._hashFunctions.forEach(func => this._bits[func(data) % this._size] = true);
  }

  contains(data) {
    return this._hashFunctions.every(func => this._bits[func(data) % this._size]);
  }
}