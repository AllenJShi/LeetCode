#
# @lc app=leetcode id=752 lang=python3
#
# [752] Open the Lock
#

# @lc code=start
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends: return -1
        def helper(s_num):
            return str((int(s_num)+1)%10), str((int(s_num)-1)%10)
        # use queue to store (key, move)
        queue = deque([("0000",0)])
        visited = set(deadends+["0000"])
        while queue:
            pwd,move = queue.popleft()
            if pwd==target:
                return move
            neighbors = []
            for i in range(4):
                up, down = [pwd[:i] + x + pwd[i+1:] for x in helper(pwd[i])]
                neighbors.extend([up,down])
            for nxt_pwd in neighbors:
                if nxt_pwd not in visited:
                    # \ and nxt_pwd not in deadends: # add deadends to visited
                        queue.append((nxt_pwd,move+1))
                        visited.add(nxt_pwd)             
        return -1
# @lc code=end

