#include <gtest/gtest.h>
#include "../solutions/valid_anagram.h"

class ValidAnagramTest : public ::testing::Test {
protected:
    ValidAnagram solution;
};

// Basic functionality tests
TEST_F(ValidAnagramTest, EmptyStrings) {
    std::string a = "";
    std::string b = "";
    std::string c = "1";
    EXPECT_TRUE(solution.isAnagram(a, a));
    EXPECT_TRUE(solution.isAnagram(a, b));
    EXPECT_FALSE(solution.isAnagram(a, c));
    EXPECT_FALSE(solution.isAnagram(c, b));
}

TEST_F(ValidAnagramTest, SameStrings) {
    std::string a = "abcde";
    std::string b = "abcde";
    EXPECT_TRUE(solution.isAnagram(a, a));
    EXPECT_TRUE(solution.isAnagram(a, b));
}

TEST_F(ValidAnagramTest, WithDuplicates) {
    std::string a = "aaaa";
    std::string b = "aaab";
    std::string c = "aaaa";
    EXPECT_TRUE(solution.isAnagram(a, c));
    EXPECT_FALSE(solution.isAnagram(a, b));
}

TEST_F(ValidAnagramTest, DifferentLengths) {
    std::string a = "abc";
    std::string b = "abcab";
    EXPECT_FALSE(solution.isAnagram(a, b));
}

TEST_F(ValidAnagramTest, AnagramStrings) {
    std::string a = "eagle";
    std::string b = "eealg";
    EXPECT_TRUE(solution.isAnagram(a, b));
    std::string c = "silent";
    std::string d = "listen";
    EXPECT_TRUE(solution.isAnagram(c, d));
}

TEST_F(ValidAnagramTest, InvalidAnagrams) {
    std::string a = "hello";
    std::string b = "world";
    EXPECT_FALSE(solution.isAnagram(a, b));
    std::string c = "blank";
    std::string d = "black";
    EXPECT_FALSE(solution.isAnagram(c, d));
}