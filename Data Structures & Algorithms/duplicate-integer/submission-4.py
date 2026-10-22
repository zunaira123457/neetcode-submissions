class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter_nums = Counter(nums)

        for n in nums: 
            if counter_nums[n] > 1: 
                return True
        return False