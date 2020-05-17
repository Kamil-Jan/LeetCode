class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        if not needle in haystack:
            return -1
        needle_len = len(needle)
        for i in range(len(haystack) - needle_len):
            if haystack[i:i + needle_len] == needle:
                return i
        return len(haystack) - needle_len

