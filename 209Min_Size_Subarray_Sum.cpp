class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        """
        Think of a sliding window. sum up consecutive elements until the sum reaches the target. 
        Then must move the head to the next element and the subsequent sum will be reduced by the first element.
        sublength keeps track of the subarray and result records the overall best solution (initialize it as max and then reduced to the possible min). 
        return 0 if result not been updated or the reduced min
        """
        int sublength = 0, i = 0;
        int result = INT32_MAX, sum = 0;
        for(int j = 0; j<nums.size(); j++){
            sum += nums[j];
            while(sum>=target){
                sublength = j-i+1;
                result = result < sublength ? result : sublength;
                sum -= nums[i++];
            }
        }
        return result == INT32_MAX ? 0 : result;
    }
};