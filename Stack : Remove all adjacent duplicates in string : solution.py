# Promblem - remove all adjacent duplicates in string 
# Approach - stack
# Time and space complexity - 0(n) & 0(n)
# Leetcode and diffculty level - 1047 & easy 
class Solution {
public:
    string removeDuplicates(string s) {
        string st = "";

        for(char c : s) {
            if(!st.empty() && st.back() == c) 
                st.pop_back();
        
            else 
                st.push_back(c);
        }
        return st;
    }
};
