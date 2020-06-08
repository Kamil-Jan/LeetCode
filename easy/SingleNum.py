from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash_table = dict()
        for num in nums:
            if num in hash_table:
                hash_table[num] += 1
            else:
                hash_table[num] = 1

        for num in nums:
            if hash_table[num] == 1:
                return num

