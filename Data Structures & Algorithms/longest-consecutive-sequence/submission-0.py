class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #go thru the nums array and check to see if one value is 
        num_set = set(nums)
        longest = 0 

        for num in nums: 
            if num - 1 in num_set:
                continue
            current_length = 1
            
            while num + 1 in num_set:
                current_length += 1
                num += 1
            
   
                
            if current_length > longest:
                longest = current_length
        return longest

    #Set = a collection that lets me quickly ask “does this number exist?”      
        
        