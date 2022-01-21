#
# @lc app=leetcode id=207 lang=python
#
# [207] Course Schedule
#

# @lc code=start
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        ################# DFS topological sorting ##############
        # 储存两个字典：
        # dict_pre = {课程：先修课}
        # dict_post = {课程：后续课}
        dict_pre, dict_post = defaultdict(list), defaultdict(list)
        for ai, bi in prerequisites:
            dict_pre[ai].append(bi)
            dict_post[bi].append(ai)
        # 每一节课程入度列表，记录该课程先修课的数量，若为0，该科即为最基础课
        indegree = [len(dict_pre[i]) for i in range(numCourses)]
        # 队列记录可选择的课程，初始化为所有入度为0的课程（不需要任何先修）
        queue = [i for i in range(numCourses) if indegree[i]==0]
        undertaken = 0
        while queue:
            curr = queue.pop()
            undertaken += 1
            for curr_post in dict_post[curr]:
                indegree[curr_post] -= 1
                if indegree[curr_post] == 0:
                    queue.append(curr_post)
        return undertaken == numCourses
    
    
    ################### DFS #########################
    
    
    
    
    ################### BFS ####################
    
    
    
        
        
# @lc code=end

