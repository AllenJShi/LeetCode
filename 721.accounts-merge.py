#
# @lc app=leetcode id=721 lang=python3
#
# [721] Accounts Merge
#

# @lc code=start
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        hashmap = defaultdict(list) # adjacent list
        visited = [False] * len(accounts)
        res = []
        for idx, account in enumerate(accounts):
            for email in account[1:]:
                hashmap[email].append(idx)
        def dfs(i, emails):
            if visited[i]:
                return
            visited[i] = True
            for email in accounts[i][1:]:
                emails.add(email)
                for neighbor in hashmap[email]:
                    dfs(neighbor,emails)
        for i, account in enumerate(accounts):
            if visited[i]:
                continue
            name, emails = account[0], set()
            dfs(i,emails)
            res.append([name]+sorted(emails))
        return res
            
# @lc code=end

