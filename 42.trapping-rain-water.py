#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        # n = len(height)
        # maxLeft = [0] * n
        # maxRight = [0] * n
        # minLR = [0] * n
        # tmpLeft = 0
        # for i in range(n):
        #     maxLeft[i] = max(tmpLeft,height[i])
        #     tmpLeft = max(maxLeft[i],tmpLeft)
        # tmpRight = 0
        # for j in range(n-1,-1,-1):
        #     maxRight[j] = max(tmpRight, height[j])
        #     tmpRight = max(maxRight[j],tmpRight)
        # for k in range(n):
        #     minLR[k] = min(maxLeft[k], maxRight[k])
        # res = 0
        # for p in range(n):
        #     res += max(minLR[p] - height[p],0)
        # return res
    
    
        left, right = 0, len(height)-1
        res, maxL, maxR = 0, height[left], height[right]
        while left < right:
            # this is the same as min(L,R) to find the bottleneck
            if maxL < maxR:
                left += 1
                # res += max(0, maxL - height[left])
                maxL = max(maxL, height[left])
                res += maxL - height[left]
            else:
                right -= 1
                # res += max(0, maxR - height[right])
                maxR = max(maxR, height[right])
                res += maxR - height[right]
        return res
# https://www.youtube.com/watch?v=ZI2z5pq0TqA
# @lc code=end

