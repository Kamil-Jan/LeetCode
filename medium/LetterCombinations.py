from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {"2": ["a","b","c"],
                   "3": ["d","e","f"],
                   "4": ["g","h","i"],
                   "5": ["j","k","l"],
                   "6": ["m","n","o"],
                   "7": ["p","q","r","s"],
                   "8": ["t","u","v"],
                   "9": ["w","x","y","z"]}
        if not digits:
            return []
        return list(self.generateCombinations(letters, digits))

    def generateCombinations(self, letters_dict, digits, prev_digits="", i=0):
        if i >= len(digits):
            yield prev_digits
        else:
            digit = digits[i]
            for char in letters_dict[digit]:
                yield from self.generateCombinations(letters_dict, digits,
                                                     prev_digits + char, i + 1)

