class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter_s = Counter(s)
        counter_t = Counter(t)

        if len(s) != len(t):
            return False
        
        return counter_s == counter_t
        