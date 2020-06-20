from typing import List


class Solution:
    def twoSum(self, nums, start, end, target_sum, i, j):
        res = []
        low = start
        high = end
        while low < high:
            cur_sum = nums[low] + nums[high]
            if cur_sum < target_sum or (low > start and nums[low] == nums[low - 1]):
                low += 1
            elif cur_sum > target_sum or (high < end and nums[high] == nums[high + 1]):
                high -= 1
            else:
                res.append([nums[i], nums[j],
                            nums[low], nums[high]])
                low += 1
                high -= 1
        return res

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        output = []
        n = len(nums)
        i_table = dict()
        for i in range(n - 1):
            if nums[i] in i_table:
                continue
            i_table[nums[i]] = i
            j_table = dict()
            for j in range(i + 1, n):
                if nums[j] in j_table:
                    continue
                j_table[nums[j]] = j
                target_sum = target - (nums[i] + nums[j])
                output.extend(self.twoSum(nums, j + 1, n - 1,
                                          target_sum, i, j))
        return output

class Solution2:
    def kSum(self, nums: List[int], target: int, k: int) -> List[List[int]]:
        res = []
        if len(nums) == 0 or nums[0] * k > target or target > nums[-1] * k:
            return res
        if k == 2:
            return self.twoSum(nums, target)
        for i in range(len(nums)):
            if i == 0 or nums[i - 1] != nums[i]:
                for set in self.kSum(nums[i + 1:], target - nums[i], k - 1):
                    res.append([nums[i]] + set)
        return res

    def twoSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        lo, hi = 0, len(nums) - 1
        while (lo < hi):
            sum = nums[lo] + nums[hi]
            if sum < target or (lo > 0 and nums[lo] == nums[lo - 1]):
                lo += 1
            elif sum > target or (hi < len(nums) - 1 and nums[hi] == nums[hi + 1]):
                hi -= 1
            else:
                res.append([nums[lo], nums[hi]])
                lo += 1
                hi -= 1
        return res

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        return self.kSum(nums, target, 4)

