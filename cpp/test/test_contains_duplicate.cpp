#include <gtest/gtest.h>
#include "../solutions/contains_duplicate.h"

class HasDuplicateTest : public ::testing::Test {
protected:
    ContainsDuplicate solution;
};

// Basic functionality tests
TEST_F(HasDuplicateTest, EmptyArray) {
    std::vector<int> nums = {};
    EXPECT_FALSE(solution.hasDuplicate(nums));
}

TEST_F(HasDuplicateTest, SingleElement) {
    std::vector<int> nums = {1};
    EXPECT_FALSE(solution.hasDuplicate(nums));
}

TEST_F(HasDuplicateTest, NoDuplicates) {
    std::vector<int> nums = {1, 2, 3, 4, 5};
    EXPECT_FALSE(solution.hasDuplicate(nums));
}

TEST_F(HasDuplicateTest, WithDuplicates) {
    std::vector<int> nums = {1, 2, 3, 2, 4};
    EXPECT_TRUE(solution.hasDuplicate(nums));
}

TEST_F(HasDuplicateTest, AdjacentDuplicates) {
    std::vector<int> nums = {1, 2, 2, 3, 4};
    EXPECT_TRUE(solution.hasDuplicate(nums));
}

TEST_F(HasDuplicateTest, DuplicateAtEnds) {
    std::vector<int> nums = {1, 2, 3, 4, 1};
    EXPECT_TRUE(solution.hasDuplicate(nums));
}

// Edge cases
TEST_F(HasDuplicateTest, AllSameElements) {
    std::vector<int> nums = {5, 5, 5, 5, 5};
    EXPECT_TRUE(solution.hasDuplicate(nums));
}

TEST_F(HasDuplicateTest, WithZeros) {
    std::vector<int> nums = {0, 1, 2, 0};
    EXPECT_TRUE(solution.hasDuplicate(nums));
}

TEST_F(HasDuplicateTest, NegativeNumbers) {
    std::vector<int> nums = {-1, -2, -3, -1};
    EXPECT_TRUE(solution.hasDuplicate(nums));
}

TEST_F(HasDuplicateTest, MixedPositiveNegative) {
    std::vector<int> nums = {-5, -3, 0, 3, 5};
    EXPECT_FALSE(solution.hasDuplicate(nums));
}

// Boundary value tests
TEST_F(HasDuplicateTest, IntMaxMin) {
    std::vector<int> nums = {INT_MAX, INT_MIN, 0, INT_MAX};
    EXPECT_TRUE(solution.hasDuplicate(nums));
}

// Parameterized tests for multiple test cases
struct TestCase {
    std::vector<int> nums;
    bool expected;
};

class HasDuplicateParamTest : public ::testing::TestWithParam<TestCase> {
protected:
    ContainsDuplicate solution;
};

TEST_P(HasDuplicateParamTest, VariousCases) {
    TestCase test = GetParam();
    EXPECT_EQ(solution.hasDuplicate(test.nums), test.expected);
}

INSTANTIATE_TEST_SUITE_P(
    HasDuplicateTests,
    HasDuplicateParamTest,
    ::testing::Values(
        TestCase{{}, false},
        TestCase{{1}, false},
        TestCase{{1, 1}, true},
        TestCase{{1, 2, 3, 4, 5}, false},
        TestCase{{1, 2, 3, 4, 1}, true},
        TestCase{{INT_MAX, INT_MIN}, false},
        TestCase{{0, 0, 0}, true},
        TestCase{{-1, 0, 1, 2, -1}, true}
    )
);

// Performance test
TEST(HasDuplicatePerformance, LargeArrayNoDuplicates) {
    ContainsDuplicate solution;
    const int size = 100000;
    std::vector<int> nums(size);
    
    // Fill with unique values
    for (int i = 0; i < size; ++i) {
        nums[i] = i;
    }
    
    auto start = std::chrono::high_resolution_clock::now();
    bool result = solution.hasDuplicate(nums);
    auto end = std::chrono::high_resolution_clock::now();
    
    auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(end - start);
    
    EXPECT_FALSE(result);
    EXPECT_LT(duration.count(), 1000) << "Operation took too long: " << duration.count() << "ms";
}

// Custom assertion for better error messages
testing::AssertionResult ArrayHasDuplicate(const std::vector<int>& nums) {
    std::unordered_set<int> seen;
    for (size_t i = 0; i < nums.size(); ++i) {
        if (seen.count(nums[i])) {
            return testing::AssertionSuccess() 
                << "Found duplicate value " << nums[i] 
                << " at index " << i;
        }
        seen.insert(nums[i]);
    }
    return testing::AssertionFailure() << "No duplicates found";
}

TEST(HasDuplicateCustom, CustomAssertion) {
    std::vector<int> nums1 = {1, 2, 3, 1};
    EXPECT_TRUE(ArrayHasDuplicate(nums1));
    
    std::vector<int> nums2 = {1, 2, 3, 4};
    EXPECT_FALSE(ArrayHasDuplicate(nums2));
}

// Main function (optional - can use gtest_main instead)
int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}