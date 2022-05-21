#
# @lc app=leetcode id=380 lang=python3
#
# [380] Insert Delete GetRandom O(1)
#

# @lc code=start
class RandomizedSet:

    def __init__(self):
        self.randomset = set()
        
    def insert(self, val: int) -> bool:
        if val not in self.randomset:
            self.randomset.add(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.randomset:
            self.randomset.remove(val)
            return True
        return False
        
    def getRandom(self) -> int:
        import random
        return random.sample(self.randomset,k=1)[0]

"""
class RandomizedSet:

    def __init__(self):
        self.d = {}
        self.l = []

    def insert(self, val: int) -> bool:
        if val not in self.d:
            new_idx = len(self.l)
            self.d[val] = new_idx
            self.l.append(val)
            return True
        return False
        
    def remove(self, val: int) -> bool:
        if val in self.d:
            cur_val_idx = self.d[val]
            last_idx = len(self.l)-1
            last_val = self.l[-1]
            
            self.l[cur_val_idx], self.l[last_idx] = self.l[last_idx], self.l[cur_val_idx]
            self.d[last_val] = cur_val_idx
            del self.d[val]
            self.l.pop()
            return True
        return False
        

    def getRandom(self) -> int:
        return random.choice(self.l)
        
"""

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end

