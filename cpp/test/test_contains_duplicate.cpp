#include <gtest/gtest.h>
#include <vector>
#include <unordered_set>

// If you have a header file
// #include "solutions/contains_duplicate.h"

// Or include the implementation directly
class Solution {
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

// Test fixture
class ContainsDuplicateTest : public ::testing::Test {
protected:
    Solution solution;
};

// Actual test cases
TEST_F(ContainsDuplicateTest, EmptyArray) {
    std::vector<int> nums = {};
    EXPECT_FALSE(solution.hasDuplicate(nums));
}

TEST_F(ContainsDuplicateTest, SingleElement) {
    std::vector<int> nums = {1};
    EXPECT_FALSE(solution.hasDuplicate(nums));
}

TEST_F(ContainsDuplicateTest, NoDuplicates) {
    std::vector<int> nums = {1, 2, 3, 4, 5};
    EXPECT_FALSE(solution.hasDuplicate(nums));
}

TEST_F(ContainsDuplicateTest, WithDuplicates) {
    std::vector<int> nums = {1, 2, 3, 2, 4};
    EXPECT_TRUE(solution.hasDuplicate(nums));
}

TEST_F(ContainsDuplicateTest, AllDuplicates) {
    std::vector<int> nums = {5, 5, 5, 5};
    EXPECT_TRUE(solution.hasDuplicate(nums));
}
