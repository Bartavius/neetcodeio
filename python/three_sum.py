from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums_sorted = sorted(nums.copy())

        for i, n in enumerate(nums_sorted):
            l, r = 0, len(nums_sorted) - 1

            # running two-sum to get -n
            while l < r:

                # enforce distinct idx
                if not (l < i < r):
                    break

                total = nums_sorted[l] + nums_sorted[r]

                if total == -n:
                    res.add((nums_sorted[l], n, nums_sorted[r]))
                    l += 1
                elif total < -n:
                    l += 1
                else:
                    r -= 1
        
        return [list(i) for i in res]

