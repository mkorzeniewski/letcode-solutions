import sys
from typing import List


class ThreeSumsClosest:
    @staticmethod
    def threeSum(nums: List[int], target: int) -> int:
        nums.sort()
        if len(nums) == 3:
            return sum(nums[:3])

        if sum(nums[:3]) > target:
            return sum(nums[:3])

        if sum(nums[-3:]) < target:
            return sum(nums[-3:])

        res = sum(nums[:3])

        for i in range(0, nums):
            low, high = i+1, len(nums)-1
            while low < high:
                s = nums[i] + nums[low] + nums[high]
                if abs(s - target) < abs(res - target):
                    res = s

                if s < target:
                    low = low + 1
                elif s > target:
                    high = high - 1
                else:
                    return s
        return res



