from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        # print(dict(count))
        res = dict(sorted(count.items(), key=lambda item: item[1]))
        result = list(res)[-k:]
        return result