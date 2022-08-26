#
# @lc app=leetcode id=349 lang=python3
#
# [349] Intersection of Two Arrays
#

# @lc code=start
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ############### hashmap ##############
        # hashmap = {}
        # res = []
        # for num1 in nums1:
        #     hashmap[num1] = hashmap[num1] + 1 if num1 in hashmap else 1
        # for num2 in nums2:
        #     if num2 in hashmap and hashmap[num2] > 0:
        #         res.append(num2)
        #         hashmap[num2] = 0
        # return res
        
        ############# two pointers ##############
        nums1.sort()
        nums2.sort()
        res = set()
        
        p1,p2 = 0,0
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] > nums2[p2]:
                p2 += 1
            elif nums1[p1] < nums2[p2]:
                p1 += 1
            else:
                res.add(nums1[p1])
                p1+=1; p2+=1
        return list(res)
# @lc code=end

