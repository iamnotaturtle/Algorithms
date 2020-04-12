import {maxSubArray} from '../maxSubArray';

describe('maxSubArray', () => {
  it('should handle empty arrays', () => {
    expect(maxSubArray()).toEqual(undefined);
    expect(maxSubArray([])).toEqual(undefined);
  });
  it('should return the max sub array using kadanes', () => {
    expect(maxSubArray([-2,1,-3,4,-1,2,1,-5,4])).toEqual(6);
  });
});