#include "contains_duplicate.h"

class ContainsDuplicate {
public:
    bool hasDuplicate(std::vector<int>& nums) {
        std::unordered_set<int> seen;
        for (int n : nums) {
            if (seen.count(n)) {
                return true;
            }
            seen.insert(n);
        }
        return false;
    }
};
