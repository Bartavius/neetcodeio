def fourSum(nums, target: int):
    nums.sort()
    results = set()

    def threeSum(nums, d, d_i):
        for i, n in enumerate(nums):
            l, r = 0, len(nums) - 1

            while l < r:
                if l < i < r < d_i and nums[l] + nums[r] + n - target == -d:
                    results.add((nums[l], n, nums[r], d))
                    l += 1
                elif nums[l] + nums[r] + n - target < -d:
                    l += 1
                else:
                    r -= 1

    
    for i, d in enumerate(nums):
        threeSum(nums, d, i)

    
    return [list(i) for i in results]