'''
Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller INDEX first.
'''

class TwoSum:
    def two_sum(self, nums, target):

        # enumerate the values of nums with their index
        sorted_list = []
        for i,n in enumerate(nums):
           sorted_list.append((n, i))
        sorted_list.sort()

        # two-sum search with a sorted list
        l, r = 0, len(sorted_list) - 1
        while l < r:
            res =  sorted_list[l][0] + sorted_list[r][0]
            if res == target:
                return sorted([sorted_list[l][1], sorted_list[r][1]]) # return the index with smallest first
            elif res < target:
                l += 1
            else:
                r -= 1

        return [] # return empty array if there's no two_sum