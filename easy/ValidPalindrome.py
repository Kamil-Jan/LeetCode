import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r"\W", "", s).lower()
        return s == s[::-1]

