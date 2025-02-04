class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        current_length = len(nums)
        i = 0
        while i < current_length:
            while nums[i] == val:
                if i == current_length - 1:
                    current_length -= 1
                    break
                for k in range(i, current_length-1):
                    nums[k] = nums[k+1]
                current_length -= 1
            i += 1
        return current_length
