''' 
Given an integer array nums, return true if any value appears more than once in 
the array, otherwise return false.
'''

def hasDuplicate(nums) -> bool:
    seen = set()
    for i in nums:
        if i in seen:
            return True
        else:
            seen.add(i)
    return False
         