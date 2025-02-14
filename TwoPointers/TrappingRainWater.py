'''
You are given an array non-negative integers height which represent an elevation map. Each value height[i] represents the height of a bar, which has a width of 1.

Return the maximum area of water that can be trapped between the bars.
'''

def trap(self, height: List[int]) -> int:
    total_water = 0
    l, r = 0, len(height) - 1
    maxl, maxr = height[l], height[r]

    while l < r:

        # move left forward if right is l <= r
        # move right in if left > r
        if height[l] <= height[r]:
            water = max(0, min(maxl, maxr) - height[l])
            l += 1
            maxl = max(maxl, height[l])
        else:
            water = max(0, min(maxl, maxr) - height[r])
            r -= 1
            maxr = max(maxr, height[r])
        total_water += water

        print(l, r)


        
    
    return total_water