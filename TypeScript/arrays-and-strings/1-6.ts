// String compression

function compressString(word: string): string {
  let compressed = '';

  let i = 1;
  let count = 1;
  let char = word.charAt(0);

  compressed += char;
  while (i < word.length) {
    if (word.charAt(i) === char) {
      count ++;
    } else {
      compressed += count;
      compressed += word.charAt(i);
      char = word.charAt(i);
      count = 1;
    }
    i++;
  }

  return compressed.length < word.length ? compressed : word;
}

console.log(
  'String compression',
  compressString('aabcccccaaa'), //a2b1c5a3
)
