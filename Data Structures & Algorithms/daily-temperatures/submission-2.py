class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []  # stores indices of temperatures
        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                prev_idx = stack.pop()
                result[prev_idx] = i - prev_idx
            stack.append(i)
        return result