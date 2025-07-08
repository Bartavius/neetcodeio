#include <gtest/gtest.h>
#include "../solutions/two_sum.h"

class TwoSumTest : public ::testing::Test {
    protected:
        TwoSum solution;
};

TEST_F(TwoSumTest, BasicFunctionality) {
    // only one solution (target is 6 for both)
    std::vector<int> a = {1, 0, 3, 4, 5};
    std::vector<int> expected = {0, 4};
    EXPECT_EQ(solution.twoSum(a, 6), expected);
    a = {3, 1, 4, 5};
    expected = {1, 3};
    EXPECT_EQ(solution.twoSum(a, 6), expected);

    // no solution (target is 1)
    a = {0, 0, 0, 0};
    expected = {};
    EXPECT_EQ(solution.twoSum(a, 1), expected);

    // one solution that uses two of the same numbers (target is 10)
    a = {5, 5};
    expected = {0, 1};
    EXPECT_EQ(solution.twoSum(a, 10), expected);
};

TEST_F(TwoSumTest, EdgeCases) {
    std::vector<int> a;
    std::vector<int> expected;
    int target;

    // not enough inputs
    a = {1};
    target = 0;
    EXPECT_EQ(solution.twoSum(a, target), expected);

    // even with one number returning target, it is an invalid solution
    a = {0};
    target = 0;
    EXPECT_EQ(solution.twoSum(a, target), expected);

    // target is zero and answers are zeros
    a = {0, 5, 0};
    target = 0;
    expected = {0, 2};
    EXPECT_EQ(solution.twoSum(a, target), expected);

    // negative numbers
    a = {-2, 15, 100, -6, -25};
    target = 75;
    expected = {2, 4};
    EXPECT_EQ(solution.twoSum(a, target), expected);

    a = {-20, -10, 0, 4, -6};
    target = 100;
    expected = {};
    EXPECT_EQ(solution.twoSum(a, target), expected);
};