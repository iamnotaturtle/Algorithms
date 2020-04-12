
// Time complexity: O(n)
// Space complexity: O(1)
export const maxSubArray = (nums) => {
  if (!nums || nums.length === 0) {
    return;
  }

  let globalMax = nums[0],
    localMax = nums[0];

  for (let i = 1; i < nums.length; i++) {

    // Either the current index is max or the sum is max
    localMax = Math.max(nums[i], localMax + nums[i]);
    globalMax = globalMax > localMax ? globalMax : localMax;
  }

  return globalMax;
};