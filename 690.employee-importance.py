#
# @lc app=leetcode id=690 lang=python3
#
# [690] Employee Importance
#

# @lc code=start
"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        ################# bfs solution #################
        visited = set()
        res = 0
        hashmap = {employee.id:{"importance":employee.importance,"subordinates":employee.subordinates} for employee in employees}
        # for employee in employees:
        #     if employee.id == id:
        #         queue = deque([employee.id])
        #         res += employee.importance
        #         while queue:
        #             employee_id = queue.popleft()
        #             for subordinate_id in hashmap[employee_id]["subordinates"]:
        #                 if subordinate_id not in visited:
        #                     queue.append(subordinate_id)
        #                     visited.add(subordinate_id)
        #                     res += hashmap[subordinate_id]["importance"]
        # return res
    
    
        ################# dfs solution #################
        def dfs(employee_id):
            nonlocal res,visited
            res += hashmap[employee_id]["importance"]
            # visited.add(employee_id)
            if not hashmap[employee_id]["subordinates"]: return
            for subordinate_id in hashmap[employee_id]["subordinates"]:
                # if subordinate_id not in visited:
                dfs(subordinate_id)
            
        dfs(id)  
        return res
                

# @lc code=end

