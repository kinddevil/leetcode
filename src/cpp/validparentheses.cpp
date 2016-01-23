#include <iostream>
#include <map>
#include <stack>
using namespace std;

class Solution {
public:
    bool isValid(string s) {
    	map<char, char> m1 = {{'(', ')'}, {'[', ']'}, {'{', '}'}};
    	map<char, char> m2 = {{')', '('}, {']', '['}, {'}', '{'}};
    	stack<char> st;
    	// cout<<st.empty()<<endl;
    	// cout<<st.top()<<endl;
    	// cout<<sizeof(s)<<endl;
    	for (char c : s){
    		if (m1.find(c) != m1.end()){
    			st.push(c);
    		}else if (m2.find(c) != m2.end()){
    			cout<<m2[c]<<endl;
    			if (!st.empty() && st.top() == m2[c])
    				st.pop();
    			else
    				return false;
    		}
    	}
        if (st.empty())
        	return true;
        else
        	return false;
    }
};

int main(){
	Solution s;
	cout<<s.isValid("aaaaa[bb]()")<<endl;
	return 0;
}
