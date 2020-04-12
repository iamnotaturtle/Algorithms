// Urlify

function urlify(word: string): string {
  // Work backwards and replace
  // if space add %20 and move up
  
  let current: number = word.length - 1;
  let position: number = word.length - 1;
  while(word.charAt(position) === ' ') {
    position -= 1;
  }

  const array: string[] = word.split('');
  while (current >= 0) {
    if (array[position] === ' ') {
      array[current] = '0';
      current -= 1;
      array[current] = '2';
      current -= 1;
      array[current] = '%';
      current -= 1;
    } else {
      array[current] = array[position];
      current -= 1;
    }
    position -= 1;
  }

  return array.join('');

}

console.log(
  urlify('Mr John Smith      '), // Mr%20John%20Smith
  urlify('  Mr      ') // %20%20Mr
  ) 