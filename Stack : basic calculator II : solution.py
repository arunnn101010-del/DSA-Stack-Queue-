# Promblem - basic calcultor II 
# Appraoch - stack 
# Time and space complexity - 0(n) & 0(n) 
# leetcode and diffulty level - 227 & medium 
class Solution {
public:
    int calculate(string s) {
        
        stack<int> st;

        int num = 0;
        char sign = '+';

        for(int i=0; i<s.size(); i++) {

            char c = s[i];

            if(isdigit(c)) {
                num = num * 10 + (c - '0');
            }

            if((!isdigit(c) && c != ' ') || i == s.size() - 1) {

                if(sign == '+') {
                    st.push(num);
                }
                else if(sign == '-') {
                    st.push(-num);
                }
                else if(sign == '*') {
                    int top = st.top();
                    st.pop();
                    st.push(top*num);
                }
                else if(sign == '/') {
                    int top = st.top();
                    st.pop();
                    st.push(top/num);
                }

                sign = c; 
                num = 0;
            } 
        }
        int sum = 0;

        while(!st.empty()) {

            sum += st.top();
            st.pop();
        }
        return sum;
    }
};
