class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+", "-", "*", "/"]

        for num in tokens:
            if num in operators:
                b = int(stack.pop())
                a = int(stack.pop())
                if num == "+":
                    result = a + b
                elif num == "-":
                    result = a - b
                elif num == "*":
                    result = a * b
                elif num == "/":
                    result = int(a / b)
                stack.append(result)
            else:
                stack.append(num)
        return int(stack.pop())
