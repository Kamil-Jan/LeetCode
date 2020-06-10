class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_substring = cur_substring = ""
        for i in range(len(s)):
            if s[i] not in cur_substring:
                cur_substring += s[i]
            else:
                dupl_index = cur_substring.index(s[i])
                cur_substring = cur_substring[dupl_index + 1:] + s[i]

            if len(cur_substring) > len(max_substring):
                max_substring = cur_substring

        return len(max_substring)

