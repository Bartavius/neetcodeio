#include "valid_anagram.h"
#include <unordered_map>

bool ValidAnagram::isAnagram(std::string s, std::string t) {
    if (s.length() != t.length()) {
        return false;
    }
    std::unordered_map<char, int> charS;
    std::unordered_map<char, int> charT;
    
    for (size_t i = 0; i < s.size(); i++) {
        charS[s[i]]++;
        charT[t[i]]++;
    }

    return charS == charT; // since cpp std compares object equality
};
