class Solution {
public:
    void sortColors(vector<int>& nums) {
        if(nums.size()<2) return;
        //insertion sorts
        for(int i=1; i<nums.size(); i++){
            for(int j=0; j<nums.size();j++){
                if(nums[i]<nums[j]){
                    int temp = nums[j];
                    nums[j] = nums[i];
                    nums[i] = temp;
                }
            }
        }
    }
};