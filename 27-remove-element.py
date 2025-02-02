class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        rcur = len(nums) - 1
        total_len = len(nums) - 1
        cnt = 0
        for index, n in enumerate(nums):
            if index >= rcur:
                break
            cnt += 1
            if n == val:
                while rcur >= 0 and nums[rcur] == val:
                    rcur -= 1
                if rcur >= index:
                    temp = nums[rcur]
                    nums[rcur] = nums[index]
                    nums[index] = temp
                    rcur -= 1
        return len(nums) - cnt
