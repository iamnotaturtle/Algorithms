const assert = require("assert");

/*
  Given encoded string 3[a]2[b] return aaabb
 */
const decode = word => {
  if (!word || word.length <= 1) {
    return word;
  }

  let stack = [];
  let alphas = "",
    digits = "";
  let c;

  for (let i = 0; i < word.length; i++) {
    c = word.charAt(i);

    if (!isNaN(c)) {
      digits += c;
    } else if (c === "[") {
      stack.push([alphas, digits]);
      alphas = "";
      digits = "";
    } else if (c === "]") {
      [prev, n] = stack.pop();
      alphas = prev + alphas.repeat(n);
    } else {
      alphas += c;
    }
  }

  return alphas;
};

assert.equal(decode("3[a]2[b]"), "aaabb");
assert.equal(decode("0"), "0");
assert.equal(decode("3[ab]2[bb]"), "abababbbbb");
assert.equal(decode("3[2[3[a]b]c]"), "aaabaaabcaaabaaabcaaabaaabc");
