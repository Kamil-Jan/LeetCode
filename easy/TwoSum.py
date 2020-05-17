class Solution:
    def twoSum(self, nums, target: int):
        hash_table = dict()
        for i, v in enumerate(nums):
            comp = target - v
            if comp in hash_table:
                return [hash_table[comp], i]
            hash_table[v] = i

