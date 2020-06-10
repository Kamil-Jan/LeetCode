import re


class Solution:
    def myAtoi(self, str: str) -> int:
        if not str:
            return 0

        INT_MIN = -2 ** 31
        INT_MAX = 2 ** 31 - 1

        s = str.lstrip()
        potential_nums = re.findall("[\+\-]{0,1}[0-9]+", s)
        if len(potential_nums) == 0:
            return 0
        if not s[0].isnumeric():
            if s[0] not in ['+', '-'] or not s[1].isnumeric():
                return 0

        number = int(potential_nums[0])
        if number < INT_MIN:
            return INT_MIN
        elif number > INT_MAX:
            return INT_MAX
        return number

