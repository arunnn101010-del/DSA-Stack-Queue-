# Promblem - validate stack sequence 
# appraoch - stack
# Time and space complexity - 0(n) & 0(n) 
# Leecode and diffculty level - 946 & easy
class Solution {
public:
    bool validateStackSequences(vector<int>& pushed, vector<int>& popped) {
        stack<int> st;
        int j = 0;

        for(int x : pushed) {
            st.push(x);

            while(!st.empty() && st.top() == popped[j]) {
                st.pop();
                j++;
            }
        }
        return st.empty();
    }
};
