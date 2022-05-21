#
# @lc app=leetcode id=140 lang=python3
#
# [140] Word Break II
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        hashmap = collections.defaultdict(list)
        def dfs(end):
            res = []
            if end == 0: return [""]
            if end in hashmap:
                # if the end index is stored
                # return the corresponding result
                return hashmap[end]
            for start in range(0,end):
                sub = s[start:end]
                if sub in wordDict:
                    tmp = dfs(start)
                    # print(tmp)
                    for t in tmp:
                        a  = sub if len(t)==0 else (t+" "+sub)
                        res.append(a)
            hashmap[end] = res
            return res
        return dfs(len(s))
# @lc code=end

