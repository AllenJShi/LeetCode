#
# @lc app=leetcode id=189 lang=python
#
# [189] Rotate Array
#

# @lc code=start
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        ############## 我的答案 ###############
        # n = len(nums)
        # k = k%n
        # if k==0: return
        # # 最后的k个将被移动到开头
        # # 前面的n-k个移动到末尾
        # nums[:] = nums[-k:] + nums[0:n-k]
        
        
        ############ 参考答案 ##############
        ### 方法：三次反转
        # 将所有的元素反转 ==》反向的序列
        # 将【0，k%n-1】，【k%n，n-】各自反转
        def reverse(start, end):
            while start < end:
                nums[start],nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        n = len(nums)
        k = k%n
        reverse(0,n-1)
        reverse(0,k-1)
        reverse(k,n-1)
    
# @lc code=end

