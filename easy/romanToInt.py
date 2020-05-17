class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
                "I": 1,
                "V": 5,
                "X": 10,
                "L": 50,
                "C": 100,
                "D": 500,
                "M": 1000,
                }
        exc = {
                "I": ["V", "X"],
                "X": ["L", "C"],
                "C": ["D", "M"]
                }
        integer = 0
        for key, symbol in enumerate(s):
            arabic = roman[symbol]
            if key - 1 >= 0:
                prev = s[key - 1]
                if prev in exc and symbol in exc[prev]:
                    continue
            if symbol in exc:
                try:
                    next_sym = s[key + 1]
                except:
                    return integer + arabic
                if next_sym in exc[symbol]:
                    arabic = roman[next_sym] - arabic
            integer += arabic
        return integer

