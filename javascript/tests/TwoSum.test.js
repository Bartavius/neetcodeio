const Solution = require('../TwoSum.js')

describe("twoSum", () => {

    let solution;

    beforeEach(() => {
        solution = new Solution()
    })

    test('basic functionality tests', () => {
        // only one solution
        expect(solution.twoSum([1, 0, 3, 4, 5], 6)).toEqual([0, 4])
        expect(solution.twoSum([3, 1, 4, 5], 6)).toEqual([1, 3])

        // no solution
        expect(solution.twoSum([0, 0, 0, 0], 1)).toEqual([])

        // one solution that uses two of the same numbers
        expect(solution.twoSum([5, 5], 10)).toEqual([0, 1])
    })

    test('Edge cases', () => {
        // not enough inputs
        expect(solution.twoSum([1], 0)).toEqual([])
        
        // even with one number returning target, it is an invalid solution
        expect(solution.twoSum([0], 0)).toEqual([])

        // target is zero and answers are zeros
        expect(solution.twoSum([0, 5, 0], 0)).toEqual([0, 2])

        // negative numbers
        expect(solution.twoSum([-2, 15, 100, -6, -25], 75)).toEqual([2, 4])
        expect(solution.twoSum([-20, -10, 0, 4, -6], 100)).toEqual([])
    })
})