from typing import List


class Solution:
    def createHashTables(self, board):
        row_table = dict()
        col_table = dict()
        box_table = dict()
        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col] == ".":
                    continue

                num = board[row][col]
                if row_table.get(row):
                    if not row_table[row].get(num):
                        row_table[row][num] = 1
                    else:
                        return False
                else:
                    row_table[row] = {num: 1}

                if col_table.get(col):
                    if not col_table[col].get(num):
                        row_table[col][num] = 1
                    else:
                        return False
                else:
                    col_table[col] = {num: 1}

                box_index = (row // 3, col // 3)
                if box_table.get(box_index):
                    if not box_table[box_index].get(num):
                        box_table[box_index][num] = 1
                    else:
                        return False
                else:
                    box_table[box_index] = {num: 1}
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.createHashTables(board)

