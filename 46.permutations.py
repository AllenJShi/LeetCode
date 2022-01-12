#
# @lc app=leetcode id=46 lang=python
#
# [46] Permutations
#

# @lc code=start
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ############### 回溯 #####################
        # def swap(a,b):
        #     nums[a], nums[b] = nums[b], nums[a]
        # ans = []
        # def backtracking(start):
        #     if start==len(nums):
        #           # 当指针移动到最后一个元素时，终止
        #         ans.append(nums[:])
        #     for i in range(start,len(nums)):
        #         swap(start,i)
        #         backtracking(start+1)
        #         swap(i,start)
        # backtracking(0)
        # return ans
        ###########################################
        
        ans = []
        path = []
        visited = [False]*len(nums)
        
        def backtracking(depth):
            if depth == len(nums):
                return ans.append(path[:])
            
            for i in range(len(nums)):
                if not visited[i]:
                    visited[i] = True
                    path.append(nums[i])
                    backtracking(depth+1)
                    path.pop()
                    visited[i] = False
                
        backtracking(0)
        return ans
        
        
        
        ############### 迭代 #####################
        # if len(nums)<=1:
        #     # 如果只剩下和一个元素，直接返回该元素
        #     return [nums]
        # ans = []
        # for i, num in enumerate(nums):
        #     n = nums[:i] + nums[i+1:]
        #     for y in self.permute(n):
        #         ans.append([num]+y)
        # return ans
        
# @lc code=end

