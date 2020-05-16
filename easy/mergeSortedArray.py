class Solution:
    def merge(self, nums1: list, m: int, nums2: list, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        insert_pos = m + n - 1
        i, j = m - 1, n - 1
        while i >= 0 and j >= 0:
            if nums1[i] >= nums2[j]:
                nums1[insert_pos] = nums1[i]
                i -= 1
            else:
                nums1[insert_pos] = nums2[j]
                j -= 1
            insert_pos -= 1

        while j >= 0:
            nums1[insert_pos] = nums2[j]
            j -= 1
            insert_pos -= 1

