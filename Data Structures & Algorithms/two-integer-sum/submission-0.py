class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, n in enumerate(nums):
            diff = target - n 
            if diff in seen: 
                return [seen[diff], i]
            seen[n] = i
        


# What you did wrong (and why)
# 1 return [nums[i], nums[j]] Returned values instead of indices; j doesn't exist return [seen[diff], i] 2 return [nums[i], ...] nums[i] is the current value, not the matching index use seen[diff] for the earlier index 3 seen[n] = 1 Stored a dummy 1 instead of the index seen[n] = i
# The deeper lesson: seen must map value → index, because the answer needs indices. You kept reaching for values. That's the single most common mistake on this problem.

# The approach (memorize this order)
# Make an empty dict: seen = {} (value → index)
# Loop with for i, n in enumerate(nums):
# Compute diff = target - n
# Check first: if diff in seen: → return [seen[diff], i]
# Store last: seen[n] = i
# Order matters: you check before you store, so you never match a number with itself (which would give i == j).

# Why check-before-store
# If you stored n before checking, then on nums = [5, 5], target = 10 at i = 0 you'd store {5: 0}, and at i = 1 diff = 5 would match — but it'd also let [5,5], target=10 match itself if you weren't careful. Checking first guarantees the pair is two distinct indices.

# Remember
# Dict = value → index. Not value → 1. Not index → value.
# Return [seen[diff], i] — earlier index always comes first, which handles the "smaller index first" rule automatically.
# One pass, one dict. You don't need nested loops.
# enumerate gives you both the index i and value n — use it, don't index manually.
# Complexity to write down
# Time: O(n) — one pass; dict lookup is O(1) average
# Space: O(n) — worst case you store every element
# Compare: brute-force double loop is O(n²) time, O(1) space. The hash map trades memory for speed.

# The one-line mental model
# "For each number, ask: have I already seen the number that completes me? If yes, return both indices. If no, remember this number for later."
            
            
        