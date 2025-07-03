const Solution = require('../ValidAnagram.js');

describe('isValidAnagram', () => {
    let solution;

    beforeEach(() => {
        solution = new Solution();
    });

    test('should return true for valid anagrams', () => {
        expect(solution.isValidAnagram('anagram', 'nagaram')).toBe(true);
        expect(solution.isValidAnagram('a', 'a')).toBe(true);
        expect(solution.isValidAnagram('racecar', 'racecar')).toBe(true);
        expect(solution.isValidAnagram('abcde', 'edcba')).toBe(true);
        expect(solution.isValidAnagram('test', 'sett')).toBe(true);
        expect(solution.isValidAnagram('listen', 'silent')).toBe(true);
        expect(solution.isValidAnagram('triangle', 'integral')).toBe(true);
    });

    test('should return false for non-anagrams', () => {
        expect(solution.isValidAnagram('hello', 'world')).toBe(false);
        expect(solution.isValidAnagram('a', 'b')).toBe(false);
        expect(solution.isValidAnagram('hellor', 'hello')).toBe(false);
        expect(solution.isValidAnagram('abcde', 'edcbfa')).toBe(false);
    });

    test('should return false for non-anagrams with the same letters', () => {
        expect(solution.isValidAnagram('apple', 'pale')).toBe(false);
        expect(solution.isValidAnagram('sstress', 'stress')).toBe(false);
    })

    test('should handle empty strings', () => {
        expect(solution.isValidAnagram('', '')).toBe(true);
        expect(solution.isValidAnagram('', 'a')).toBe(false);
        expect(solution.isValidAnagram('a', '')).toBe(false);
    });
});