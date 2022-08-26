#
# @lc app=leetcode id=895 lang=python3
#
# [895] Maximum Frequency Stack
#

# @lc code=start
class FreqStack:

    def __init__(self):
        self.freqStack = defaultdict(list)
        self.freq = defaultdict(int)
        self.max_freq = 0

    def push(self, val: int) -> None:
        # update freq in self.freq
        curr_freq = self.freq[val] + 1
        self.freq[val] += 1
        
        # update self.max_freq
        if curr_freq > self.max_freq:
            self.max_freq = curr_freq
            self.freqStack[curr_freq] = [] # create placeholder
        
        # add to self.freqStack
        self.freqStack[curr_freq].append(val)

    def pop(self) -> int:
        top_list = self.freqStack[self.max_freq]
        top = top_list.pop()
        self.freq[top] -= 1
        
        # update max freq
        if not top_list:
            self.max_freq -= 1
            
        return top


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
# @lc code=end

