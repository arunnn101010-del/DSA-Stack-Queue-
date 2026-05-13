# Promblem - decode string
# Approach - stack
# Time and space complexity - 0(n log n) & 0(n)
# Leetcode and diffculty level - 394 & medium 
class Solution {
public:
    string decodeString(string s) {

        stack<int> numSt;
        stack<string> strSt;

        string curr = "";
        int num = 0;

        for(char c : s) {
            if(isdigit(c)) {
                num = num * 10 + (c - '0');
            }
            else if(c == '[') {
                numSt.push(num);
                strSt.push(curr);

                num=0;
                curr = "";
            }
            else if(c == ']') {
                int repeat = numSt.top();
                numSt.pop();

                string prev = strSt.top();
                strSt.pop();

                string temp = "";

                while(repeat--) {
                    temp += curr;
                }
                curr = prev + temp;
            }
            else {
                curr += c;
            }
        }
        return curr;
    }
};
