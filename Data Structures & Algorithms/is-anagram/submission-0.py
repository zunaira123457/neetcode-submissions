class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        similar = {}
        second = {}
        
        if len(s) != len(t):
            return False
        
        count_s = Counter(s)
        count_t = Counter(t)
        return count_s == count_t
        
##For this problem, the key phrase is:

#"same characters, each appearing the same number of times, regardless of order"
#That phrase "regardless of order" is a giant neon sign. It tells you: the actual positions don't matter — only the multiset of characters matters. Whenever order doesn't matter and you need to check equality of contents, a hash map/counter is almost always the answer.

#The general decision tree
#Ask yourself these questions in order:

#Does order matter?

#Yes → think arrays, two pointers, sliding window, sorting.
#No → think hash map / set / counting.
#Am I counting how many times something appears?

#Yes → frequency map (Counter).
#Am I checking if two collections contain the same elements?

#Yes → build a frequency map for each and compare, OR sort both and compare.