#
# @lc app=leetcode id=387 lang=python
#
# [387] First Unique Character in a String
#

# @lc code=start
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # # 两遍
        # frequency = collections.Counter(s)
        # for i, char in enumerate(s):
        #     if frequency[char] == 1:
        #         return i
        # return -1
    
        # # 排队
        position = dict()
        queue = collections.deque()
        for i, char in enumerate(s):
            if char not in position:
                position[char] = i
                queue.append((char,i))
            else:
                position[char] = -1
                while queue and position[queue[0][0]] == -1:
                    queue.popleft()
            print(char)
            print(queue)
            print(position)
        # print(f"{char},{queue},{position}")
            
        return -1 if not queue else queue[0][1]
        
# @lc code=end

