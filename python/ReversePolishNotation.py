'''
You are given an array of strings tokens that represents a valid arithmetic expression in Reverse Polish Notation.

Return the integer that represents the evaluation of the expression.

The operands may be integers or the results of other operations.
The operators include '+', '-', '*', and '/'.
Assume that division between integers always truncates toward zero.
'''
def evalRPN(tokens) -> int:
    stack = []
    for i in tokens:
        if i == "+" or i == "-" or i == "*" or i == "/":
            last = stack.pop()
            penultimate = stack.pop()
            if i == "+":
                stack.append(penultimate + last)
            elif i == "-":
                stack.append(penultimate - last)
            elif i == "*":
                stack.append(penultimate * last)
            elif i == "/":
                stack.append(int(penultimate / last))
        else: # assuming that it is a valid number
            stack.append(int(i))
    return stack[0]