# Promblem - next gretaer element I 
# Appraoch - stack 
# Time and space complexity - 0(n) & 0(n)
# Leetcode and diffculty level - 496 & easy 
class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        
        stack<int> st;
        unordered_map<int,int> mp;

        for(int num : nums2) {

            while(!st.empty() && st.top() < num) {
                mp[st.top()] = num;
                st.pop();
            }
            st.push(num);
        }
        vector<int> res;

        for(int num : nums1) {

            if(mp.count(num)) 
                res.push_back(mp[num]);
            else
                res.push_back(-1);
        }
        return res;
    }
};
