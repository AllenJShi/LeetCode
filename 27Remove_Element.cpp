class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int len = nums.size();
        int ptr1 = 0;
        for(int ptr2=0; ptr2<len; ptr2++){
            if(nums[ptr2]!=val){
                nums[ptr1] = nums[ptr2];
                ptr1++;
            }
        }
        return ptr1;
    }；

    // Method 2: dual pointers, left to move and check each elements, right to be the last element and in place the match val
    int removeElement2(vector<int>& nums, int val){
        int right = nums.size();
        int left = 0;
        while(left<right){ //when left not reach the last element (normally size - 1)
            if(nums[left]==val){//if the current element is the val, then inplace with the last element and let the right pointer points to the second last one
                nums[left] = nums[right-1]; 
                right--;
            }else{//increment left, move pointer to the next element if the current position not match
                left++; 
            }
        }
        return left;
    }
};


