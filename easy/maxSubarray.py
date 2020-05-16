class Solution:
    def maxSubArray(self, nums):
        best_max = -float("inf")
        cur_max = 0

        for i in range(0, len(nums)):
            cur_max = cur_max + nums[i]
            if (best_max < cur_max):
                best_max = cur_max

            if cur_max < 0:
                cur_max = 0
        return best_max

