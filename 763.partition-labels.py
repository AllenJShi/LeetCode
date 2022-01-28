#
# @lc app=leetcode id=763 lang=python
#
# [763] Partition Labels
#

# @lc code=start
class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        last = [0] * 26
        # 直接记录每一个s中元素所在的位置，最终储存的为最后一个元素位置
        for i, char in enumerate(s):
            last[ord(char)-ord('a')] = i
        partition = []
        # start开始记录子链的初始位置
        start = end = 0
        # 对于每一个字母遍历
        for i, char in enumerate(s):
            # 更新end，end是当前元素的最后位置或子链中最远元素的end
            # 例子：abcdabbb
            end = max(end, last[ord(char)-ord('a')])
            # 若当前元素的位置在end，表示已遍历到最后一个当前元素
            if i == end:
                # 计算并记录当前元素所在的子链长度
                partition.append(end-start+1)
                # 更新开始start，将是现在子链的下一个位置
                start = end + 1
        return partition
# @lc code=end

