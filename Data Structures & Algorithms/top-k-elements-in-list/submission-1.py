class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #do a count and then add all the numbers to the count and then comapre it to the k and displau all the values equal to or more than the k.
        count_n = Counter(nums)
        return [num for num,_ in count_n.most_common(k)]
        
#count_n.most_common(k) → returns the k most frequent items as (value, count) pairs, already sorted by count descending. For our example with k=2: [(3, 3), (2, 2)].
#for num, _ in ... → unpacks each pair; num gets the number, _ gets the count (ignored).
#[num for ...] → builds a list of just the numbers → [3, 2].


        