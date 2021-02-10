const assert = require("assert");

/*
  pow(2, 5) => 32
 */
const pow = (number, exponent) => {
  let answer = 1;
  for (let i = 0; i < exponent; i++) {
    answer *= number;
  }
  return answer;
};

assert.equal(pow(2, 5), 32);
assert.equal(pow(0, 1), 0);
assert.equal(pow(1, 0), 1);
