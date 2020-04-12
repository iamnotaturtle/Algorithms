// One away

function isOneAway(word1: string, word2: string): boolean {
  
  if (word1.length - word2.length > 1) {
    return false;
  }
  
  let i = 0, j = 0;
  let char1: string, char2: string;
  let count = 0;
  while(i < word1.length && j < word2.length) {
    char1 = word1.charAt(i);
    char2 = word2.charAt(j);

    if (char1 === char2) {
      i++;
      j++;
    } else if (word1.length === word2.length && char1 !== char2) {
      count++;
      i++;
      j++;
    } else if (word1.length > word2.length) {
      count++;
      i++;
    } else {
      count++;
      j++;
    }
  }

  return count <= 1;
}
/* pales, pale

 */


console.log(
  'One Away',
  isOneAway('pale', 'ple'), // true
  isOneAway('pales', 'pale'), // true
  isOneAway('pale', 'bale'), // true
  isOneAway('pale', 'bake'), // false
)