# Promblem - Minimum Add to Make Parentheses Valid
# Appraoch - stack
# Time and space complexity - 0(n) & 0(n) 
# Leetcode & diffculty level - 921 & easy
class Solution {
public:
    int minAddToMakeValid(string s) {
        
        stack<char> st;
        int ans = 0;

        for(char c : s) {
            if(c == '(') {
                st.push(c);
            }
            else {
                if(!st.empty())
                st.pop();
                else
                    ans++;
            }
        }
        return ans + st.size();
    }
};
