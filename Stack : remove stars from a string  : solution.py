# Promblem - remove stars from a string 
# Approach - stack 
# Time and space complexity - 0(n) & 0(n)
# Leetcode and diffculty level - 2390 & easy 
class Solution {
public:
    string removeStars(string s) {
        string st = "";

        for(char c : s) {
            if(c == '*')
                st.pop_back();
            else 
                st.push_back(c);
        }
        return st;
    }
};
