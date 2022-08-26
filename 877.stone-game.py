#
# @lc app=leetcode id=877 lang=python3
#
# [877] Stone Game
#

# @lc code=start
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        """ input 3,9,1,2
          |  1  |  2  |  3  |  4  |
         1| 3,0 | 9,3 | 4,9 | 11,4|
         2|     | 9,0 | 9,1 | 10,2|
         3|     |     | 1,0 | 2,1 |
         4|     |     |     | 2,0 |
        from lower rigth of main diagnal toward upper left
        """
        # n = len(piles)
        # dp = [[(0,0)] * n for _ in range(n)]
        # for i in range(n):
        #     dp[i][i] = (piles[i],0)
        
        # # look up the [left,right] interval
        # for left in range (n-1,-1,-1):
        #     for right in range(left+1,n):
        #         pickLeft, pickRight = dp[left+1][right], dp[left][right-1]
        #         if piles[left] + pickLeft[1] > piles[right] + pickRight[1]:
        #             dp[left][right] = (piles[left] + pickLeft[1],pickLeft[0])
        #         else:
        #             dp[left][right] = (piles[right] + pickRight[1],pickRight[0])
        # alice, lee = dp[0][n-1]
        

        # return alice > lee
                
                
        """ input [3,9,1,2]
        store the difference between first and second move
          |  1  |  2  |  3  |  4  |
          -------------------------
         1|  3  | -6  |  -5 |  7  |
         2|     |  9  |  8  |  8  |
         3|     |     |  1  |  1  |
         4|     |     |     |  2  |
        """
        n = len(piles)
        dp = [[0] * n for _ in range(n)]
        for i in range(n): dp[i][i] = piles[i]
        for d in range(1, n): # d:= rigth boundary
            for i in range(n - d): # i:= left boundary
                dp[i][i + d] = max(piles[i] - dp[i + 1][i + d], piles[i + d] - dp[i][i + d - 1])
        from pprint import pprint
        pprint(dp)
        return dp[0][-1] > 0

            
# @lc code=end

