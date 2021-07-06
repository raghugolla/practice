"""
You are given an array of integers nums (0-indexed) and an integer k.

The score of a subarray (i, j) is defined as min(nums[i], nums[i+1], ..., nums[j]) * (j - i + 1). A good subarray is a subarray where i <= k <= j.

Return the maximum possible score of a good subarray.



Example 1:

Input: nums = [1,4,3,7,4,5], k = 3
Output: 15
Explanation: The optimal subarray is (1, 5) with a score of min(4,3,7,4,5) * (5-1+1) = 3 * 5 = 15.
Example 2:

Input: nums = [5,5,4,5,4,1,1,1], k = 0
Output: 20
Explanation: The optimal subarray is (0, 4) with a score of min(5,5,4,5,4) * (4-0+1) = 4 * 5 = 20.


Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 2 * 104
0 <= k < nums.length

"""
from typing import List


class Solution:
    def max_score(self, nums: List[int], k: int) -> int:
        lo = hi = k
        max_score = mi = nums[k]
        n = len(nums)

        while lo > 0 or hi < n - 1:
            if (nums[lo - 1] if lo > 0 else 0) < (nums[hi + 1] if hi < n - 1 else 0):
                hi += 1
            else:
                lo -= 1

            mi = min(mi, min(nums[lo], nums[hi]))
            max_score = max(max_score, mi * (hi - lo + 1))

        return max_score
