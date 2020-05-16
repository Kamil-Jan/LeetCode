class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
                "(": ")",
                "[": "]",
                "{": '}'
                }
        stack = []
        for b in s:
            if b in brackets:
                stack.append(b)
            elif stack and b == brackets[stack[-1]]:
                stack.pop()
            else:
                return False
        return stack == []

