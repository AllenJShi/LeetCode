#
# @lc app=leetcode id=126 lang=python3
#
# [126] Word Ladder II
#

# @lc code=start
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        # create a mask map to accelerate the search
        lookup = collections.defaultdict(list)
        match = False
        n = len(wordList)
        for word in wordList:
            if word==endWord:
                match = True
            for i in range(n):
                mask = word[:i] + '*' + word[i+1:]
                lookup[mask].append(word)
        if not match: return []
        
        wordSet = set(wordList) # set is faster than dict
        # cur_level is the queue in BFS
        cur_level = collections.defaultdict(list)
        cur_level[beginWord] = [[beginWord]]
        while cur_level:
            wordSet -= set(cur_level.keys())
            next_level = collections.defaultdict(list)
            for word in cur_level:
                if word==endWord:
                    return cur_level[endWord]
                for i in range(n):
                    mask = word[:i]+'*'+word[i+1:]
                    for next_word in lookup[mask]:
                        if next_word in wordSet:
                            next_level[next_word] += [ j + [next_word] for j in cur_level[word]]
            cur_level = next_level
        return []
        
# @lc code=end

