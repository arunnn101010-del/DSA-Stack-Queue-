# Promblem - implement stack using queue 
# Appraoch - queue 
# Time and space complexity - 0(1) & 0(n) 
# Leetcode and diffculty level - 225 & easy 
class MyStack {
public:
    queue<int> q;

    MyStack() {
        
    }
    
    void push(int x) {
        q.push(x);
        int n = q.size();
        for(int i = 0; i<n-1; i++) {
            q.push(q.front());
            q.pop();
        }
    }
    
    int pop() {
        int val = q.front();
        q.pop();
        return val;
    }
    
    int top() {
        return q.front();
    }
    
    bool empty() {
        return q.empty();
    }
};
