#
# @lc app=leetcode id=833 lang=python3
#
# [833] Find And Replace in String
#

# @lc code=start
class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        prev = 0
        replacements = sorted(zip(indices,sources,targets),key=lambda x:x[0])
        res = []
        for index, source, target in replacements:
            if s[index:index+len(source)] != source:
                continue 
            res.append(s[prev:index]) # copy the unchanged part
            res.append(target) # replace
            prev = index + len(source) # update prev
        res.append(s[prev:]) # append the remaining str
        return ''.join(res)
# @lc code=end

