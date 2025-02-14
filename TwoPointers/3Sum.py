def threeSum(nums):
    nums.sort()
    triplets = set()

    for i, n in enumerate(nums):
        l, r = 0, len(nums) - 1

        while l < r:
            print(nums[l], nums[r], n)
            if l < i and i < r and nums[l] + nums[r] + n == 0:
                triplets.add((nums[l], n, nums[r]))
                l += 1
            elif nums[l] + nums[r] + n < 0:
                l += 1
            else:
                r -= 1
    
    return [list(i) for i in triplets]