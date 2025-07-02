'''
Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first.
'''

class Solution:
    def two_sum(nums, target):

        # define l r
        sorted_nums = []
        for i, item in enumerate(nums):
            sorted_nums.append((item, i))

        sorted_nums.sort()
        l, r = 0, len(sorted_nums) - 1

        while l < r:
            if sorted_nums[l][0] + sorted_nums[r][0] == target:
                first = sorted_nums[l][1]
                second = sorted_nums[r][1]
                return [min(first, second), max(first, second)]

            elif sorted_nums[l][0] + sorted_nums[r][0] < target:
                l += 1
            else:
                r -= 1
        return []