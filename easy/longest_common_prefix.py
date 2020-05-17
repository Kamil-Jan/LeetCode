class Solution:
    def longestCommonPrefix(self, strs) -> str:
        prefix = ""
        for symbol in zip(*strs):
            last_sym = symbol[0]
            for s in symbol[1:]:
                if s == last_sym:
                    pass
                else:
                    return prefix
            prefix = f"{prefix}{last_sym}"
        return prefix

