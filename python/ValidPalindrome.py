'''
Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.
'''
def isPalindrome(self, s: str) -> bool:
    left_ptr = 0
    right_ptr = len(s) - 1

    while left_ptr < right_ptr:

        # moves pointer to next alphabet
        if not s[left_ptr].isalnum():
            left_ptr += 1
            continue
            
        if not s[right_ptr].isalnum():
            right_ptr -= 1
            continue

        if s[left_ptr].lower() != s[right_ptr].lower():
                return False
        else:
            left_ptr += 1
            right_ptr -= 1

    return True