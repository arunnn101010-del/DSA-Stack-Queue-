# Promblem - number of recent calls
# Appraoch - queue 
# Time and space complexity - 0(1) & 0(n) 
# Leetcode and diffculty level - 933 & medium 
class RecentCounter {
public:
    queue<int> q;

    RecentCounter() {
        
    }
    
    int ping(int t) {
        q.push(t);
        while(q.front() < t - 3000) {
            q.pop();
        }
        return q.size();
    }
};
