#
# @lc app=leetcode id=884 lang=python3
#
# [884] Uncommon Words from Two Sentences
#

# @lc code=start
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        cnt = Counter(s1.split())
        cnt += Counter(s2.split())
        
        return [w for w in cnt if cnt[w]==1]
# @lc code=end

