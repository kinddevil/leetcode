#include <iostream>
#include <string>
#include <vector>
#include <list>
#include <map>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
    	map<int, int> m;
	vector<int> ret;
	for (int i=0; i<nums.size(); i++){
	    if (m.find(nums[i])== m.end()  )
		m[target-nums[i]] = i;
	    else {
		ret.push_back(m[nums[i]] + 1);
		ret.push_back(i+1);
		break;
	    }
	}  
	return ret;  
    }
};

int main(){
    vector<int> v ;
    v.push_back(2);
    v.push_back(7);
    v.push_back(11);
    v.push_back(15);
    int target = 9;
    Solution s ;
    vector<int> vv = s.twoSum(v, target);
    for (vector<int>::iterator it = v.begin(); it!=v.end(); it++)
	cout<<*it<<endl;    
    for (auto n:vv)
	cout<<n<<endl;
}
