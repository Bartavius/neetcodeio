'''
You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

The input string s is valid if and only if:

Every open bracket is closed by the same type of close bracket.
Open brackets are closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
Return true if s is a valid string, and false otherwise.

'''

def isValid(s: str) -> bool:
        
    stack = []
    paren = {
        '(' : ')',
        '{' : '}',
        '[' : ']'
    }

    for i in s:
        if i in paren:
            stack.append(paren[i])

        else:
            if not stack or i != stack.pop():
                return False
    
    return len(stack) == 0