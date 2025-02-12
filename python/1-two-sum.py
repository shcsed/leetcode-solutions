class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index1, m in enumerate(nums):
            for index2, n in enumerate(nums):
                if index2 <= index1:
                    continue
                if m + n == target:
                    return [index1, index2]
