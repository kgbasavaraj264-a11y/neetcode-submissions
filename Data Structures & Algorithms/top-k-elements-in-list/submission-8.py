from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h=Counter(nums)
        result=[num for num,count in h.most_common(k)]
        return result