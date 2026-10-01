class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #first define all the operands: operands = "+ -" etc
        operators = ["+", "-", "*", "/"]
        stack = []

        for num in tokens:
            if num not in operators:
                stack.append(int(num))
            if num in operators:
                if num == "+":
                    b = stack.pop()
                    a = stack.pop()
                    output = a + b
                    stack.append(output)

                elif num == "-":
                    b = stack.pop()
                    a = stack.pop()
                    output = a - b
                    stack.append(output)
                
                elif num == "*":
                    b = stack.pop()
                    a = stack.pop()
                    output = a * b
                    stack.append(output)

                elif num == "/":
                    b = stack.pop()
                    a = stack.pop()
                    output = int(a / b)
                    stack.append(output)
        return stack.pop()
                