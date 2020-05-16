import re

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = re.findall(r"\w+", s)
        if len(words) == 0:
            return 0
        return len(words[-1])

