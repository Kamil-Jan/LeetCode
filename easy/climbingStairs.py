from math import sqrt


class Solution:
    def climbStairs(self, n: int) -> int:
        # Fibonacci formula
        sqrt5 = sqrt(5)
        fibn = ((1 + sqrt5) / 2)**(n+1) - ((1 - sqrt5) / 2)**(n+1)
        return int(fibn / sqrt5)

x = Solution()
print(x.climbStairs(5))

