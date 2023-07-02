from typing import List


class DuplicatesSortedArray2:
    @staticmethod
    def remove(nums: List[int]) -> int:
        s, f = 1, 2
        while f < len(nums):
            if nums[f] == nums[s] and nums[f] == nums[s-1]:
                f = f+1
            else:
                s = s + 1
                nums[s] = nums[f]
                f = f + 1
        return s + 1