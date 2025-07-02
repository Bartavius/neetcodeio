const Solution = require('../ContainsDuplicate.js');

describe('hasDuplicate', () => {
    let solution;

    beforeEach(() => {
        solution = new Solution();
    });

    test('should return true for array with duplicates', () => {
        expect(solution.hasDuplicate([1, 2, 3, 1])).toBe(true);
        expect(solution.hasDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])).toBe(true);
    });

    test('should return false for array without duplicates', () => {
        expect(solution.hasDuplicate([1, 2, 3, 4])).toBe(false);
        expect(solution.hasDuplicate([1, 2, 3])).toBe(false);
    });

    test('should handle edge cases', () => {
        expect(solution.hasDuplicate([])).toBe(false);
        expect(solution.hasDuplicate([1])).toBe(false);
        expect(solution.hasDuplicate([0])).toBe(false);
    });

    test('should handle negative numbers', () => {
        expect(solution.hasDuplicate([-1, -2, -3, -1])).toBe(true);
        expect(solution.hasDuplicate([-1, -2, -3])).toBe(false);
    });

    test('should handle zeros', () => {
        expect(solution.hasDuplicate([0, 1, 2, 0])).toBe(true);
        expect(solution.hasDuplicate([0, 1, 2, 3])).toBe(false);
    });
});