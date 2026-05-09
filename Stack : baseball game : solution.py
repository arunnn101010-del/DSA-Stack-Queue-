# Promblem - baseball game 
# Appraoch - stack 
# time and space complexity - 0(n) & 0(n)
# leetcode and diffculty level - 682 & easy
class Solution {
public:
    int calPoints(vector<string>& ops) {
        
        stack<int> st;

        for(string op : ops) {

            if(op == "C") {
                st.pop();
            }
            else if(op == "D") {
                st.push(st.top() * 2);
            }
            else if(op == "+") {
                int top1 = st.top();
                st.pop();

                int top2 = st.top();

                st.push(top1);

                st.push(top1 + top2);
            }
            else {
                st.push(stoi(op));
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

