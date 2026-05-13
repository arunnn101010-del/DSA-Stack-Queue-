# Promblem - faltten nested list operator 
# Appraoch - recursion + stack 
# Time and space complexity - 0(n) & 0(n)
# Leetcode and diffculty level - 341 & medium 
class NestedIterator {
public:
    stack<NestedInteger> st;

    NestedIterator(vector<NestedInteger> &nestedList) {
        for(int i = nestedList.size() - 1; i>=0; i--) {
            st.push(nestedList[i]);
        }        
    }
    
    int next() {
        int val = st.top().getInteger();
        st.pop();
        return val;
    }
    
    bool hasNext() {
        while(!st.empty()) {
            NestedInteger curr = st.top();
            if(curr.isInteger()) {
                return true;
            }
            st.pop();

            vector<NestedInteger> list = curr.getList();

            for(int i = list.size() - 1; i>=0; i--) {
                st.push(list[i]);
            }
        }
        return false;
    }
};
