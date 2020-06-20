class Solution:
    def binary_search(self, nums, target, low, high):
        if low >= high:
            if nums[low] == target:
                return [low, high]
            return [-1, -1]
        mid = (low + high) // 2
        if target < nums[mid]:
            return self.binary_search(nums, target, low, mid - 1)
        elif target > nums[mid]:
            return self.binary_search(nums, target, mid + 1, high)

        start_pos = end_pos = mid
        if mid - 1 >= 0:
            if nums[mid - 1] == target:
                start_pos = self.binary_search(nums, target,
                                               low, mid - 1)[0]

        if mid + 1 < len(nums):
            if nums[mid + 1] == target:
                end_pos = self.binary_search(nums, target,
                                             mid + 1, high)[-1]
        return [start_pos, end_pos]

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        return self.binary_search(nums, target, 0, len(nums) - 1)

