#include<iostream>
#include<vector>
#include<map>
#include<set>
#include<string>
#include<list>
#include<limits>
#include<algorithm>

using namespace std;

class Solution {
public:
    int maxArea(vector<int>& height) {
        int begin = 0, end = height.size() - 1, maxArea = INT_MIN;
        while (begin < end){
        	maxArea = max(maxArea, min(height[begin], height[end]) * (end - begin));
        	if (height[begin] < height[end]){
        		begin++;
        	}else{
        		end--;
        	}
        }
        return maxArea;
    }
};

int main(){
    Solution s;
    vector<int> a, b;
    a.push_back(3);
    a.push_back(1);
    // sort(a.begin(), a.end(), greater<int>());
    b.push_back(2);
    b.push_back(4);
 //    for (auto v : a)
 //       cout<<v<<endl;
 //    for (vector<int>::iterator it = b.begin(); it!=b.end(); it++)
	// 	cout<<*it<<endl;
	// cout<<min(1,2)<<endl;
	// cout<<a.size()<<endl;
	// cout<<a[1]<<endl;
	// cout<<*(--a.end())<<endl;
	// cout<<numeric_limits<int>::min()<<endl;
	// cout<<INT_MIN<<endl;
    // cout<<s.findMedianSortedArrays2(a, b)<<endl;
    cout<<s.maxArea(a)<<endl;
}
