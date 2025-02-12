from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = Counter(nums)
        return sorted(list(c.keys()), key=lambda k: c[k])[-1]
