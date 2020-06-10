def convert_border_row(s, i, numRows):
    convertion = ""
    step = 2 * (numRows - 1)
    for j in range(i, len(s), step):
        convertion += s[j]
    return convertion

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        convertion = convert_border_row(s, 0, numRows)
        big_step = 2 * (numRows - 1) - 2
        small_step = 2
        for i in range(1, numRows - 1):
            step = big_step
            j = i
            while j < len(s):
                convertion = convertion + s[j]
                j += step
                if step != small_step:
                    step = small_step
                else:
                    step = big_step
            big_step -= 2
            small_step += 2

        convertion = convertion + convert_border_row(s, numRows - 1, numRows)
        return convertion

