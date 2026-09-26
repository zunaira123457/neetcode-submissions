class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        repeating = set()

        for n in nums:
            if n in repeating:
                return True
            else:
                repeating.add(n)
        return False