class Solution:
    def binary_search(self, nums, target, low, high):
        if low == high:
            if nums[low] == target:
                return low
            return -1
        mid = (low + high) // 2
        if target < nums[mid]:
            if nums[mid] > nums[high] and nums[low] > target:
                return self.binary_search(nums, target, mid + 1, high)
            return self.binary_search(nums, target, low, mid)
        elif target > nums[mid]:
            if nums[mid] < nums[low] and nums[high] < target:
                return self.binary_search(nums, target, low, mid)
            return self.binary_search(nums, target, mid + 1, high)
        return mid

    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        return self.binary_search(nums, target, 0, len(nums) - 1)
