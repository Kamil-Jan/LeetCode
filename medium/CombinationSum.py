from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.solution = []
        self.backtrack(candidates, target)
        return self.solution

    def backtrack(self, candidates, target, cur_sum=0, i=0, chosen_nums=[]):
        if cur_sum == target:
            self.solution.append(chosen_nums)
            return
        if i < len(candidates):
            num = candidates[i]
            repeat = (target - cur_sum) // num
            while repeat:
                self.backtrack(candidates, target,
                               cur_sum + repeat  * num,
                               i + 1, chosen_nums + [num] * repeat)
                repeat -= 1
            self.backtrack(candidates, target,
                           cur_sum, i + 1, chosen_nums)

