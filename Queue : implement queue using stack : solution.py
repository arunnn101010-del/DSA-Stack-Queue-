# Promblem - implement stack using queue 
# Appraoch - queue + stack 
# Time and space complexity - 0(1) & 0(n)
# Leetcode and diffculty level - 232 & easy 
class MyQueue {
public:

    stack<int> input;
    stack<int>output;

    MyQueue() {
        
    }
    
    void push(int x) {
        input.push(x);
    }
    
    int pop() {
        peek();
        int val = output.top();
        output.pop();
        return val;
    }
    
    int peek() {
        if(output.empty()) {
            while(!input.empty()) {
                output.push(input.top());
                input.pop();
            }
        }
        return output.top();
    }
    
    bool empty() {
        return input.empty() && output.empty();
    }
};
