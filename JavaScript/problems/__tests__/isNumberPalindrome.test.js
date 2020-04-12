import {isNumberPalindrome} from '../isNumberPalindrome';

describe('isNumberPalindrome', () => {
  it('should return true for palindrome, false otherwise', () => {
    expect(isNumberPalindrome(1221)).toEqual(true);
    expect(isNumberPalindrome(1)).toEqual(true);
    expect(isNumberPalindrome(33)).toEqual(true);
    expect(isNumberPalindrome(1234)).toEqual(false);
    expect(isNumberPalindrome('')).toEqual(false);    
  });
});