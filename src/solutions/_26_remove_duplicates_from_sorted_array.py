from typing import List


class DuplicatesSortedArray:
    @staticmethod
    def remove(nums: List[int]) -> int:
        k = 1
        for i in range(0, len(nums)):
            while k < len(nums) and nums[i] == nums[k]:
                k = k + 1
            if k >= len(nums):
                return i + 1
            nums[i + 1] = nums[k]
        return len(nums)
