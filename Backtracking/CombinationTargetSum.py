def combinationSum(self, nums, target: int):
    res = []
    nums.sort()

    def backtrack(i, current, total):
        if total == target:
            res.append(current.copy())
            return

        for f in range(i, len(nums)):
            if total + nums[f] > target:
                return
            else:
                current.append(nums[f])
                backtrack(f, current, total + nums[f])
                current.pop() # remove if doesn't work out
    
    backtrack(0, [], 0)
    return res