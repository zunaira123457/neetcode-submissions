class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            "(" : ")",
            "{" : "}",
            "[": "]"   
        }
        stack = []
        for charac in s:
            if charac== "(" or charac ==  "{" or charac ==  "[":
                stack.append(charac)
            else: 
                if stack and pairs[stack[-1]] == charac:
                    stack.pop(-1)
                else:
                    return False
        return len(stack) == 0
