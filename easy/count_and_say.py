class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        else:
            prev = self.countAndSay(n - 1)
            say = ""
            count = 0
            last = prev[0]
            for i in range(len(prev)):
                if prev[i] == last:
                    count += 1
                else:
                    say += f"{count}{last}"
                    count = 1
                last = prev[i]
            say += f"{count}{last}"
            return say

