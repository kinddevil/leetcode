#include<iostream>
#include<vector>
#include<map>
#include<set>
#include<string>
#include<list>

using namespace std;

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
	nums1.insert(nums1.end(), nums2.begin(), nums2.end());
        sort(nums1.begin(), nums1.end());
	for (vector<int>::iterator it = nums1.begin(); it!=nums1.end(); it++){
	    cout<<*it<<endl;
	}
	return nums1.size()%2? nums1[nums1.size()/2] : (nums1[nums1.size()/2]+nums1[nums1.size()/2-1])/2.0;
    }
    double findMedianSortedArrays2(vector<int>& nums1, vector<int>& nums2) {
	int cnt = nums1.size() + nums2.size();
	cout<<"size:"<<cnt<<endl;
	if (cnt & 0x1)
	    return findKth(&nums1[0], nums1.size(),  &nums2[0], nums2.size(), cnt/2+1);
	else
	    return (findKth(&nums1[0], nums1.size(), &nums2[0], nums2.size(), cnt/2) + findKth(&nums1[0], nums1.size(),  &nums2[0], nums2.size(), cnt/2+1) )/2.0;
    }
    double findKth(int a[],int m, int b[], int n,  int k){
	cout<<m<<" "<<n<<endl;
        if (m>n){
	    return findKth(b,n, a, m, k);
	}
	if (m == 0){
	    return b[k-1];
	}
        if (k == 1){
	    return min(a[0], b[0]);
	}
	int pa = min(k/2, m), pb = k-pa;
	if (a[pa-1] < b[pb-1])
	    return findKth(a+pa, m - pa , b, n, k-pa);
	else if (a[pa-1] > b[pb-1] ){
	    return findKth(a, m, b+pb, n-pb, k-pb);
	}else
	    return a[pa-1];
    }
};

int main(){
    Solution s;
    vector<int> a, b;
    a.push_back(1);
    a.push_back(3);
    b.push_back(2);
    b.push_back(4);
    for (auto v : a)
       cout<<v<<endl;
    for (vector<int>::iterator it = b.begin(); it!=b.end(); it++)
	cout<<*it<<endl;
    cout<<s.findMedianSortedArrays2(a, b)<<endl;
}
