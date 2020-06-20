from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.solution = []
        self.backtrack(candidates, target, sum(candidates))
        return self.solution

    def is_suitable(self, num, target, cur_sum, sum_left):
        if cur_sum + num > target:
            return False
        if cur_sum + sum_left < target:
            return False
        return True

    def backtrack(self, candidates, target, sum_left,
                  cur_sum=0, i=0, chosen_nums=[]):
        if cur_sum == target:
            self.solution.append(chosen_nums)
            return
        if i < len(candidates):
            for index in range(i, len(candidates)):
                if i < index and candidates[index] == candidates[index - 1]:
                    continue

                num = candidates[index]
                if self.is_suitable(num, target, cur_sum, sum_left):
                    self.backtrack(candidates, target, sum_left - num,
                                   cur_sum + num, index + 1, chosen_nums + [num])

