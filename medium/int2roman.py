import random


class Solution:
    def intToRoman(self, num: int) -> str:
        roman_nums = {1000: "M",
                     500: "D",
                     100: "C",
                     50: "L",
                     10: "X",
                     5: "V",
                     1: "I"}
        exceptions = {4: "IV",
                      9: "IX",
                      40: "XL",
                      90: "XC",
                      400: "CD",
                      900: "CM"}
        output_num = ""
        prev_devider = "M"
        for devider in roman_nums.keys():
            if num // devider > 0:
                repeat_num, num = divmod(num, devider)
                roman_num = repeat_num * roman_nums[devider]
                if repeat_num == 4:
                    roman_num = roman_nums[devider] + prev_devider
                x = 10 ** (len(str(num)) - 1)
                if devider + num // x * x == 9 * x:
                    roman_num = exceptions[devider + num // x * x]
                    _, num = divmod(num, x)
                output_num += roman_num
            prev_devider = roman_nums[devider]
        return output_num

