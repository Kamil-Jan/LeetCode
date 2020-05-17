class Solution:
    def plusOne(self, digits):
        digits[-1] = last = digits[-1] + 1
        i = -1
        while last >= 10:
            digits[i] = 0
            try:
                last = digits[i - 1] = digits[i - 1] + 1
            except IndexError:
                digits.insert(0, 1)
                break
            i -= 1
        return digits

