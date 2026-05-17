# Promblem - sliding window maximum 
# Approach - deque
# Time and space complexity - 0(n) & 0(k) 
# Leetcode and diffculty level - 239 & medium 
class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        deque<int> dq;
        vector<int> ans;

        for(int i=0; i<nums.size(); i++) {
            if(!dq.empty() && dq.front() <= i-k) {
                dq.pop_front();
            }
            while(!dq.empty() && nums[dq.back()] < nums[i]) {
                dq.pop_back();
            }
            dq.push_back(i);

            if(i >= k-1) {
                ans.push_back(nums[dq.front()]);
            }
        }
        return ans;
    }
};
