#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#

# @lc code=start
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    #     queue= deque([(beginWord,1)])
    #     visited = set()
        
    #     while queue:
    #         curr, moves = queue.popleft()
    #         if curr == endWord:
    #             return moves
    #         neighbors = []
            
    #         # here make it O(len(wordList))
    #         # however, we can use for c in "a-z". see the solution
    #         for word in wordList:
    #             if self.diff_by_one(word,curr):
    #                 neighbors.append(word)
                    
    #         for nei in neighbors:
    #             if nei and nei not in visited:
    #                 queue.append((nei,moves+1))
    #                 visited.add(nei)
    #     return 0
    
    # def diff_by_one(self,word,curr):
    #     n_diff = 0
    #     for i in range(len(word)):
    #         if word[i] != curr[i]:
    #             n_diff += 1
    #     return n_diff <= 1
    
        wordList = set(wordList)
        queue = collections.deque([[beginWord, 1]])
        while queue:
            word, length = queue.popleft()
            if word == endWord:
                return length
            for i in range(len(word)):
                # this is actually O(1)
                for c in range(97,123):
                    next_word = word[:i] + chr(c) + word[i+1:]
                    if next_word in wordList:
                        wordList.remove(next_word)
                        queue.append([next_word, length + 1])
        return 0
# @lc code=end

