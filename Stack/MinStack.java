class MinStack {

    private Stack<Integer> stack;
    private Stack<Integer> minStack;

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
