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
        ################# BFS topological sorting ##############
        

        # # 储存两个字典：
        # # dict_pre = {课程：先修课}
        # # dict_post = {课程：后续课}
        # dict_pre, dict_post = defaultdict(list), defaultdict(list)
        # for ai, bi in prerequisites:
        #     dict_pre[ai].append(bi)
        #     dict_post[bi].append(ai)
        # # 每一节课程入度列表，记录该课程先修课的数量，若为0，该科即为最基础课
        # indegree = [len(dict_pre[i]) for i in range(numCourses)]
        # # 队列记录可选择的课程，初始化为所有入度为0的课程（不需要任何先修）
        # queue = [i for i in range(numCourses) if indegree[i]==0]
        # undertaken = 0
        # while queue:
        #     curr = queue.pop(0)
        #     undertaken += 1
        #     for curr_post in dict_post[curr]:
        #         indegree[curr_post] -= 1
        #         if indegree[curr_post] == 0:
        #             queue.append(curr_post)
        # return undertaken == numCourses

    
    ################### DFS topoligical sorting #########################
        def dfs(i):
            # 若该node已被其他途径遍历
            if flags[i] == -1: return True
            # 若该node在cycle中（被开始遍历，但在结束前cycle）
            if flags[i] == 1: return False
            # 开始遍历该node的子树（后续课程）
            flags[i] = 1
            for j in adjacency[i]:
                # 对于任何后续课程，如果不能被dfs
                if not dfs(j):
                    return False
            # 该node及其子树已被遍历
            flags[i] = -1
            return True
        # 初始化：0表示该node没有被遍历
        flags = [0 for _ in range(numCourses)]
        # 创建一个相邻结点的树，每棵子树代表对应课程之后可以上的课
        adjacency = [[] for _ in range(numCourses)]
        for curr, prev in prerequisites:
            adjacency[prev].append(curr)
        # 对于每一个课程，做dfs
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

        
        
# @lc code=end

