import java.util.Stack;

// Design a stack class that supports the push, pop, top, and getMin operations.

// MinStack() initializes the stack object.
// void push(int val) pushes the element val onto the stack.
// void pop() removes the element on the top of the stack.
// int top() gets the top element of the stack.
// int getMin() retrieves the minimum element in the stack.
// Each function should run in O(1) time.

class MinStack {

    private final Stack<Integer> stack;
    private final Stack<Integer> minStack;

    public MinStack() {
        this.stack = new Stack<>();
        this.minStack = new Stack<>(); 
    }
    
    public void push(int val) {
        stack.push(val);
        if (minStack.empty() || val <= minStack.peek()) 
            minStack.push(val);
    }
    
    public void pop() {
        if (stack.empty()) return;
        int topElem = stack.pop();
        if (topElem == minStack.peek()) {
            minStack.pop();
        }
    }
    
    public int top() {
        return stack.peek();
    }
    
    public int getMin() {
        return minStack.peek();
    }
}
