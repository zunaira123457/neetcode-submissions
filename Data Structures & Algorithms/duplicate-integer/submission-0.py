class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #hashmap -> a data structure that lets you store key-> value 
        #its like a dictionary 
        repeats = {} 
        for num in nums: 
            if num in repeats: 
                return True
            else:
                repeats[num] = 1
        return False