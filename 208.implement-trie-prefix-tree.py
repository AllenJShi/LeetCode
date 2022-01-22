#
# @lc app=leetcode id=208 lang=python
#
# [208] Implement Trie (Prefix Tree)
#

# @lc code=start
class Trie(object):

    def __init__(self):
        self.db = []

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        if word not in self.db:
            self.db.append(word)
        

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return (word in self.db)
        

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        ### 用python buildin 函数 str.startswith()
        # for word in self.db:
        #     if len(word) < len(prefix): continue
        #     if word.startswith(prefix):
        #         return True
        # return False
        
        
        ### 自己做搜索
        def isPrefix(word, prefix):
            for i in range(len(prefix)):
                if word[i] != prefix[i]:
                    return False
            return True
        for word in self.db:
            if len(word) < len(prefix): continue
            if isPrefix(word,prefix):
                return True
        return False

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

