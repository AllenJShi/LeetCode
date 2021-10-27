#
# @lc app=leetcode id=62 lang=python
#
# [62] Unique Paths
#

# @lc code=start
class Solution(object):
    def uniquePaths(self, m, n):
        """f(i,j) be the unique path to (i,j)
        f(i,j) = f(i-1,j) + f(i,j-1)
        f(0,0) = 1
        f(i,0) = 1
        f(0,j) = 0
        find(m-1,n-1)
        """
        f = [[1] * n] + [[1] + [0] * (n-1) for _ in range(m-1)]
        # print(f)                
        for i in range(1,m):
            for j in range(1,n):
                f[i][j] = f[i-1][j] + f[i][j-1]
        print_(f)
        return f[m-1][n-1]
    
def print_(mat):
    for i in mat:
        print(i)
# @lc code=end

