#
# @lc app=leetcode id=520 lang=python
#
# [520] Detect Capital
#

# @lc code=start

class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
    ############## SIMULATION OF CHECKING EACH LETTER ##################
        """
        if len(word) == 1: return True
        # start with the 2nd letter, because the first is correct no matter
        if word[1].isupper():
            if word[0].islower(): return False
            i = 2
            while i < len(word) and word[i].isupper():
                i += 1
            if i < len(word): return False
            return True
        else:
            i = 2
            while i < len(word) and word[i].islower():
                i += 1
            if i < len(word): return False
            return True
        """
    ############## USE TOTAL COUNT OF CAPITALS #############
        count = 0
        for i in word:
            if i >='A' and i<='Z':
                count += 1
        if count==1 and word[0].isupper():
            return True
        elif count==0:
            return True
        elif count == len(word):
            return True
        else:
            return False
        
# @lc code=end

