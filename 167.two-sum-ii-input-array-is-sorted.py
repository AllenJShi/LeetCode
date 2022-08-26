#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ################# two pointers #################
        # left, right = 0, len(numbers)-1
        # while left < right:
        #     if numbers[left] + numbers[right] > target:
        #         right -= 1
        #     elif numbers[left] + numbers[right] < target:
        #         left += 1
        #     else:
        #         return [left+1, right+1]
        
        ################ hashmap ####################
        # hashmap = {}
        # for i, number in enumerate(numbers):
        #     if target - number in hashmap:
        #         return [hashmap[target - number]+1, i+1]
        #     hashmap[number] = i
            
        ################# binary search #####################
        for i in range(len(numbers)):
            left, right = i+1, len(numbers)-1
            tmp = target - numbers[i]
            while left <= right:
                mid = (left+right)//2
                if numbers[mid] > tmp:
                    right = mid - 1
                elif numbers[mid] < tmp:
                    left = mid + 1
                else:
                    return [i+1, mid+1]
                
# @lc code=end

