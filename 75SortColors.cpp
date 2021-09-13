class Solution {
public:
    void sortColors(vector<int>& nums) {
        /*
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
        */

        //two pointers, much faster
        int n = nums.size();
        int p0=0, p2=n-1;
        for(int i=0; i<=p2;++i){
            while(i<=p2 && nums[i]==2){
                int tmp = nums[i];
                nums[i]=nums[p2];
                nums[p2]=tmp;
                p2--;
            }
            if(nums[i]==0){
                int tmp = nums[i];
                nums[i]=nums[p0];
                nums[p0]=tmp;
                p0++;
            }
        }


    }
};