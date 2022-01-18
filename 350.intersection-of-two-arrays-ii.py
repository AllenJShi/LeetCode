#
# @lc app=leetcode id=350 lang=python
#
# [350] Intersection of Two Arrays II
#

# @lc code=start
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ############### 我的答案 passed ##############
        # # 暴力查找
        # ans = []
        # for i in nums1:
        #     if i in nums2:
        #         ans.append(i)
        #         nums2.remove(i)
        # return ans
    
        
        # # 排序+双指针 （与参考答案完全一致！）
        # nums1.sort(); nums2.sort()
        # p1 = p2 = 0
        # ans = []
        # while p1 < len(nums1) and p2 <len(nums2):
        #     if nums1[p1] == nums2[p2]:
        #         ans.append(nums1[p1])
        #         p1 += 1
        #         p2 += 1
        #     elif nums1[p1] < nums2[p2]:
        #         p1 += 1
        #     else:
        #         p2 += 1                
        # return ans
        
        ################# 参考答案 - 哈希表 ######################
        # 将第一个数组存进哈希表中，每个元素出现次数记录
        # 读第二个数组，若出现哈希表中出现次数不为0的，加入答案，并-1
        hashmap = {}
        intersection = []
        for num in nums1:
            if num not in hashmap:
                hashmap[num] = 1
            else:
                hashmap[num] += 1
        for num in nums2:
            if num in hashmap and hashmap[num] != 0:
                hashmap[num] -= 1
                intersection.append(num)
        return intersection
# @lc code=end

