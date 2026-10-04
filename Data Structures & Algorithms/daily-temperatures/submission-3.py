class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Pre-fill result with 0s. Default 0 = "no warmer day found ahead."
        # This saves us from having to explicitly set 0 later for leftover days.
        result = [0] * len(temperatures)
        
        # Monotonic (decreasing) stack storing INDICES of days we haven't resolved yet.
        # We store indices (not values) so we can compute (current_day - past_day) = gap.
        # Invariant: temps at these indices are in DECREASING order from bottom to top.
        stack = []
        
        # Walk through every day once, left to right.
        for i, t in enumerate(temperatures):
            # While today's temp is warmer than the temp at the top of the stack,
            # we've just found the "next warmer day" for that waiting day.
            # We may resolve MULTIPLE waiting days at once (hence the while, not if).
            while stack and temperatures[stack[-1]] < t:
                # Pop the waiting day's index — its answer is ready now.
                prev_idx = stack.pop()
                # The number of days waited = current_index - prev_index.
                result[prev_idx] = i - prev_idx
                # Loop continues: maybe the new top also has a cooler temp than today.
            
            # After resolving everyone who was waiting for a warmer day,
            # today becomes the newest "waiting" day for a future warmer day.
            stack.append(i)
        
        # Any indices still in the stack never found a warmer day → they keep their 0.
        return result


#The pattern to memorize
#This is the Monotonic Stack pattern. Recognize it when you see phrases like:

#"next greater element"
#"days until warmer"
#"how far until something bigger/smaller"
