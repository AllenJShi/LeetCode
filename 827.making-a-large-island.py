#
# @lc app=leetcode id=827 lang=python3
#
# [827] Making A Large Island
#

# @lc code=start
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        tag = 2 # because 0-ocean, 1-land
        area_dict = {}
        directions = ((1,0),(-1,0),(0,1),(0,-1))
        for r in range(ROWS):
            for c in range(COLS):
                # if island, do bfs here
                if grid[r][c] == 1:
                    grid[r][c] = tag
                    queue = deque([(r,c)])
                    area = 0
                    while queue:
                        i,j = queue.popleft()
                        area += 1
                        for direction in directions:
                            ii,jj = tuple(map(sum,zip((i,j),direction)))
                            if 0<=ii<ROWS and 0<=jj<COLS and grid[ii][jj] == 1:
                                grid[ii][jj] = tag
                                queue.append((ii,jj))
                    area_dict[tag] = area
                    tag += 1
        if not area_dict: return 1
        max_area = max(area_dict.values())
        for ri in range(ROWS):
            for ci in range(COLS):
                if grid[ri][ci] == 0:
                    area = 1
                    islands = set()
                    for direction in directions:
                        rii, cii = tuple(map(sum,zip((ri,ci),direction)))
                        if 0<=rii<ROWS and 0<=cii<COLS and grid[rii][cii]!=0:
                            islands.add(grid[rii][cii])
                    for island in islands:
                        area += area_dict[island]
                    max_area = max(max_area,area)
        return max_area
                                                            
# @lc code=end

