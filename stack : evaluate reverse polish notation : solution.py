# Promblem - evaluate reverse polish notation 
# Appraoch - stack 
# Time and space complexity - 0(n) & 0(n) 
# Leetcode and diffculty level - 150 & medium 
class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> st;

        for(string t : tokens) {

            if(t == "+" || t == "-" || t == "*" || t == "/") {

                int b = st.top();
                st.pop();

                int a = st.top();
                st.pop();

                if(t == "+") 
                    st.push(a+b);
                
                else if(t == "-") 
                    st.push(a-b);
                
                else if(t == "*") 
                    st.push(a*b);
                else
                    st.push(a/b);
            }
            else {
                st.push(stoi(t));
            }
        }
        return st.top();
    }
};
