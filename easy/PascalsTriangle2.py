from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        for _ in range(rowIndex):
            next_level = [1]
            for i in range(len(row) - 1):
                next_level.append(row[i] + row[i + 1])
            next_level.append(1)
            row = next_level
        return row

