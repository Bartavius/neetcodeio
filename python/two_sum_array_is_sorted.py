from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # non decreasing order
        # always a solution
        # O(1) space

        # two pointer approach
        l = 0
        r = len(numbers) - 1
        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]
            
            elif numbers[l] + numbers[r] > target:
                r -= 1
            
            else:
                l += 1
                