'''
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
'''

def isAnagram(self, s: str, t: str) -> bool:
    chars = {}
    for c in s:
        if c not in chars:
            chars[c] = 1
        else:
            chars[c] += 1
    
    for c in t:
        if c in chars:
            chars[c] -= 1
            if chars[c] < 0:
                return False
        else:
            return False
    return sum(chars.values()) == 0