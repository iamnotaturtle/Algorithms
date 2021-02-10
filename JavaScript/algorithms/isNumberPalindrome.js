
// Time: O(n)
// Space: O(n)
export const isNumberPalindrome = (num) => {
  if (!num || num.length === 0) {
    return false;
  }
  if (num.length === 1) {
    return true;
  }

  let temp = num;
  let reversed = '';
  while (temp > 0) {
    reversed += temp % 10;
    temp = Math.floor(temp / 10);
  }
  return Number(num) === Number(reversed);
};