#
# @lc app=leetcode id=1094 lang=python3
#
# [1094] Car Pooling
#

# @lc code=start
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # idea: loading passengers == - dispatching passengers
        pairs = [(loc, numPeople) for numPeople,loc,_ in trips] + [(loc, -numPeople) for numPeople,_,loc in trips]
        for _, numsPeople in sorted(pairs):
            capacity -= numsPeople
            if capacity < 0:
                return False
        return True
# @lc code=end

