class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter_n = Counter(nums)
        return sorted(counter_n, key=counter_n.get, reverse=True)[:k]


                
        