class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            ")": "(",
            "}": "{",
            "]": "[",
        }
        stack = []

        for charac in s: 
            if charac == "(" or charac == "{" or charac == "[":
                stack.append(charac)
            else:
                if stack and stack[-1] == pairs[charac]:
                    stack.pop(-1)
                else:
                    return False
        return len(stack) == 0