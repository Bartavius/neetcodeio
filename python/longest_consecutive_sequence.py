class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_length = 0
        lookup = set(nums)

        for n in nums:
            if (n - 1) not in lookup:
                length = 1
                
                # keep searching for next increasing
                while (n + length) in lookup:
                    length += 1
                
                max_length = max(length, max_length)

        return max_length