#
# @lc app=leetcode id=893 lang=python3
#
# [893] Groups of Special-Equivalent Strings
#

# @lc code=start
class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        # visited = set()
        # res = 0
        # for w in words:
        #     queue = deque([w])
        #     while queue:
        #         word = queue.popleft()
        #         neighbors = set()
        #         for i in range(len(word)):
        #             j = i+2
        #             while j<len(word):
        #                 new_word = word[:i]+word[j]+word[i+1:j]+word[i]+word[j+1:]
        #                 neighbors.add(new_word)
        #         print(neighbors)
        #         for nei in neighbors:
        #             if nei not in visited:
        #                 if nei in words:
        #                     res += 1
        #                 queue.append(nei)
        #                 visited.add(nei)
        # return res
        
        
        """https://leetcode.com/problems/groups-of-special-equivalent-strings/discuss/358795/python3-detail-explanation-of-special-equivalent"""
        res = set()
        for s in words:
            sort_odd_even = ''.join(sorted(s[1::2]) + sorted(s[::2]))
            res.add(sort_odd_even)
        return len(res)

# @lc code=end

