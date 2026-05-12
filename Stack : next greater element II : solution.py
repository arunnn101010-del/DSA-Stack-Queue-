# Promblem - next greater element II 
# Appraoch - stack 
# Time and space complexity - 0(n) & 0(n) 
# Leetcode and diffculty level - 503 & medium
class Solution {
public:
    vector<int> nextGreaterElements(vector<int>& nums) {
        
        int n = nums.size();

        vector<int> ans(n,-1);

        stack<int> st;

        for(int i = 0; i < 2*n; i++) {

            int num = nums[i%n];

            while(!st.empty() && nums[st.top()] < num) {

                ans[st.top()] = num;
                st.pop();
            }

            if(i < n) {
                st.push(i);
            }
        }
        return ans;
    }
};
