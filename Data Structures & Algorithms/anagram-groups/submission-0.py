class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #order doesnt matter so a count/hasmap 
        groups = {}
        for s in strs:
            key = "".join(sorted(s))
            if key not in groups:
                groups[key]= []
            groups[key].append(s)
        return list(groups.values()) 

#really struggled with this one, still need to understand it doesnt make sense to me.
