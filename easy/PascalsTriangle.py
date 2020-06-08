from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        triangle = [[1]]
        for _ in range(numRows - 1):
            prev_level = triangle[-1]
            next_level = [1]
            for i in range(len(prev_level) - 1):
                next_level.append(prev_level[i] + prev_level[i + 1])
            next_level.append(1)
            triangle.append(next_level)
        return triangle

