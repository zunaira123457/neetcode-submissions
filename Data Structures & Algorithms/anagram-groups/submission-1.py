class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for s in strs: 
            key = "".join(sorted(s))
            if key not in group: 
                group[key] = [] #when key doesnt exist -> creating a new dict entry
            group[key].append(s)
        return list(group.values())



        
        