from typing import List
from collections import Counter


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        count = Counter(nums)
        # (0, 0, 0)
        if count[0] > 2:
            output.append([0, 0, 0])

        # (a, a, -2a)
        for key in count.keys():
            if count[key] > 1 and count[-key*2] > 0 and key != 0:
                output.append([key, key, -2 * key])

        # (a, b, -a - b)
        nums = list(count.keys())
        nums.sort()
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                target = -nums[i] - nums[j]
                if target <= nums[j]: # we checked left half
                    break
                if target in count:
                    output.append([nums[i], nums[j], target])
        return output

