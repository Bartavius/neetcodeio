class Solution {
    
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        // enumerate the nums
        let sortedList = []
        for (let i = 0; i < nums.length; i++) {
            sortedList.push([nums[i], i])
        }
        sortedList.sort((a, b) => a[0] - b[0])

        // two sum with sorted list
        let l = 0
        let r = sortedList.length - 1
        let result
        while (l < r) {
            result = sortedList[l][0] + sortedList[r][0]
            if (result === target) {
                return [Math.min(sortedList[l][1], sortedList[r][1]),
                        Math.max(sortedList[l][1], sortedList[r][1]),
                        ]
            } else if (result < target) {
                l++
            } else {
                r--
            }
        }
        return []
    }

    
}

module.exports = Solution;