class Solution:
    def twoSum(self, nums, target: int):
        # One pass solution.
        hash_table = dict()
        for i, v in enumerate(nums):
            comp = target - v
            if comp in hash_table:
                return [hash_table[comp], i]
            hash_table[v] = i
        # First accept.
        # for key, num in enumerate(nums):
            # num2 = target - num
            # right_part = nums[key + 1:]
            # left_length = len(nums) - len(right_part)
            # if num2 in right_part:
                # return [key, left_length + right_part.index(num2)]

