class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        vector<int> ans(m+n, 0);
        int i=m-1, j=n-1;
        int t = m+n-1;
        int cur;
        while(i>=0 || j>=0){
            if(i==-1){
                cur = nums2[j--];
            }else if(j==-1){
                cur = nums1[i--];
            }else if(nums1[i] < nums2[j]){
                cur = nums2[j--];
            }else{
                cur = nums1[i--];
            }
            nums1[t--] = cur;
        }
    }
};