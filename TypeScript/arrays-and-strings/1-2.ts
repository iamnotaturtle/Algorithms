// Permutations

// O(2nlogn + n)
function isPermutation(word1: string, word2: string): boolean {
  if (word1.length !== word2.length) {
    return false;
  }

  const sorted1 = word1.split('').sort();
  const sorted2 = word1.split('').sort();

  for (let i = 0; i < sorted1.length; i++) {
    if (sorted1[i] !== sorted2[i]) {
      return false;
    }
  }

  return true;
}

console.log(
  isPermutation('hey', 'yeah'), // false
  isPermutation('apple', 'pplea'), // true
  isPermutation('god   ', 'dog'), // false
);

// O(2n)
function isPermutationHash(word1: string, word2: string): boolean {
  if (word1.length !== word2.length) {
    return false;
  }

  const dict: {[key: string]: number} = {};

  for (let i = 0; i < word1.length; i++) {
    dict[word1.charAt(i)] += 1;
  }

  for (let i = 0; i < word2.length; i++) {
    dict[word1.charAt(i)] -= 1;

    if (dict[word1.charAt(i)] < 0) {
      return false;
    }
  }

  return true;
}

console.log(
  'Hash',
  isPermutationHash('hey', 'yeah'), // false
  isPermutationHash('apple', 'pplea'), // true
  isPermutationHash('god   ', 'dog'), // false
);
