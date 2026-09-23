class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        i = 0
        output = []
            #multiply every value in the array except the value 
            # u at in
            #if we are at that index we need to not include it in
            #the multiplication 
            #[1,2,3,4]
            #u can multiply all the numbers and then divide it by the 
            #index that its at 
        n = len(nums)
        res = [0] * n
        pref = [0] * n
        suff = [0] * n

        pref[0] = suff[n - 1] = 1
        for i in range(1, n):
            pref[i] = nums[i - 1] * pref[i - 1]
        for i in range(n - 2, -1, -1):
            suff[i] = nums[i + 1] * suff[i + 1]
        for i in range(n):
            res[i] = pref[i] * suff[i]
        return res