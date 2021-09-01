class Solution {
public:
    bool canJump(vector<int>& nums) {
        int pos=0;
        int n = nums.size();
        for(int i=0; i<n; i++){
            if(i<=pos){
                pos = ((i + nums[i]) > pos)? (i+nums[i]) : pos;
                if(pos>=n-1){
                    return true;
                }
            }
            
        }
        return false;
    }
};