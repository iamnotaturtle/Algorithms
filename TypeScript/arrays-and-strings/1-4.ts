function isPermutationOfPalindrome(word: string): boolean {
  const letters: {[key: string]: number} = {};
  let count: number = 0;

  for (let i = 0; i < word.length; i++) {
    const letter = word.charAt(i);

    // Ignore spaces
    if (letter !== ' ') {
      if (!letters[letter]) {
        letters[letter] = 1;
      } else {
        letters[letter] = letters[letter] + 1;
      }
      count += 1;
    }
  }

  const isEven = count % 2 === 0;
  let numOfOdds = 0;
  for (let key in letters) {
    if (letters[key] % 2 !== 0) {
      if (isEven) {
        return false;
      }
      numOfOdds += 1;
    }
  }

  if (!isEven && numOfOdds !== 1) {
    return false;
  } else {
    return true;
  }
}

console.log(
  'isPermutationOfPalindrome',
  isPermutationOfPalindrome('taco cat'), // true
  isPermutationOfPalindrome('ape catc'), // false
  isPermutationOfPalindrome('aabb'), // true
)