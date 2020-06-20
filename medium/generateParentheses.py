from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if not n:
            return []
        self.solution = []
        self.backtrack(n)
        return self.solution

    def backtrack(self, n, prev_parentheses="", open=0, closed=0):
        if len(prev_parentheses) == 2 * n:
            self.solution.append(prev_parentheses)
            return
        if open < n:
            self.backtrack(n, prev_parentheses + "(",
                           open + 1, closed)
        if closed < open:
            self.backtrack(n, prev_parentheses + ")",
                           open, closed + 1)
