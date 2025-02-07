class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target > nums[-1]:
            return len(nums)
        if target <= nums[0]:
            return 0
        for index, value in enumerate(nums):
            if index == 0:
                continue
            if value >= target >= nums[index-1]:
                return index
