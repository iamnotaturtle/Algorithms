// isUnique
// O(nlogn + n)
function isUnique(word: string): boolean {
  const sorted = word.split('').sort();
  for (let i = 0; i < sorted.length - 1; i++) {
    if (sorted[i] == sorted[i + 1]) {
      return false;
    }
  }

  return true;
}

console.log(
  'Sort',
  isUnique('aabbss'), // false
  isUnique(''), // true
  isUnique('abcdee'), // false
);

// O(n), space: O(1)
function isUniqueHash(word: string): boolean {
  const dictionary: {[key: string]: boolean} = {};

  for (let i = 0; i < word.length; i++) {
    const letter = word.charAt(i);
    if (dictionary[letter]) {
      return false;
    }

    dictionary[letter] = true;
  }

  return true;
}

console.log(
  'Hash',
  isUniqueHash('aabbss'), // false
  isUniqueHash(''), // true
  isUniqueHash('abcdee'), // false
);
