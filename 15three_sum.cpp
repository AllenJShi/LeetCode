class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        vector<vector<int>> ans;
        int n = nums.size();
        if(n<3){
            return ans;
        }
        for(int first=0; first<n; ++first){
            if(first>0 && nums[first]==nums[first-1]){
                continue;
            }
            int third = n-1;
            for(int second=first+1; second<n;++second){
                if(second>first+1 && nums[second]==nums[second-1]){
                    continue;
                }
                while(second<third && nums[first]+nums[second]+nums[third]>0){
                    --third;
                }
                if(second ==  third){
                    break;
                }
                if(nums[first]+nums[second]+nums[third]==0){
                    ans.push_back({nums[first],nums[second],nums[third]});
                }
            }
        }
        return ans;
    }


    //Method 2: time limit exceed
    vector<vector<int>> threeSum(vector<int>& nums){
        vector<vector<int>> ans;
        int n = nums.size();
        if(n<3){
            return ans;
        }
        sort(nums.begin(),nums.end());
        for(int first=0; first<n; first++){
            if(nums[first]>0){
                return ans;
            }
            if(first>0 && nums[first]==nums[first-1]){//和上一个出现重复，跳过
                continue;
            }
            int l = first + 1;
            int r = n - 1;
            while(l<r){
                if(nums[first]+nums[l]+nums[r]==0){
                    ans.push_back({nums[first],nums[l],nums[r]});
                    while(l<r && nums[l]==nums[l+1]){
                        l++;
                    }
                    while(l<r && nums[r]==nums[r-1]){
                        l--;
                    }
                    l++;
                    r--;
                }else if(nums[first]+nums[l]+nums[r]<0){
                    l++;
                }else{
                    r--;
                }
            }
        }
        return ans;
    }
};