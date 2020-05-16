class Solution:
    def reverse(self, x: int) -> int:
        reversed_num = ""
        start = 0
        end = len(str(x))
        while str(x).endswith("0") and x != 0:
            x //= 10

        if x < 0:
            sign = "-"
            x = abs(x)
        else:
            sign = ""

        for i in reversed(str(x)[start:end]):
            reversed_num += i
        x = int(sign + reversed_num)

        neg_limit= -0x80000000
        pos_limit= 0x7fffffff
        if not(neg_limit < x < pos_limit):
            x = 0
        return x

