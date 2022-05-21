#
# @lc app=leetcode id=384 lang=python
#
# [384] Shuffle an Array
#

# @lc code=start
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = list(nums)
        self.shuffled = nums

    def reset(self) -> List[int]:
        return self.nums

    def shuffle(self) -> List[int]:
        for i in range(len(self.shuffled)):
            swap_idx = random.randrange(i,len(self.shuffled))
            self.shuffled[i], self.shuffled[swap_idx] = self.shuffled[swap_idx], self.shuffled[i]
        return self.shuffled 



# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
# @lc code=end

