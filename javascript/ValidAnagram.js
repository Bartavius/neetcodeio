class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isValidAnagram(s, t) {

        // constraint: s and t consist of lowercase English letters.
        
        if (s.length !== t.length) return false;

        const charS = {};
        const charT = {};

        let sc, tc;

        // counting up
        for (let i = 0; i < s.length; i++) {
            sc = s[i];
            tc = t[i];

            charS[sc] = (charS[sc] || 0) + 1;
            charT[tc] = (charT[tc] || 0) + 1;
        }
        
        // check if each counter had the same count since JS === compares pointers
        for (const c in charS) {
            if (charS[c] !== charT[c]) {
                return false;
            }
        }
        return true;
    }
}

module.exports = Solution;
