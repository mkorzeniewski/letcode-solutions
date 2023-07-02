import sys
from typing import List


class ThreeSumsClosest:
    @staticmethod
    def threeSum(nums: List[int], target: int) -> int:
        closest_difference = (sys.maxsize, 0)
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j+1, len(nums)):
                    sum3 = nums[i] + nums[j] + nums[k]
                    diff = sum3 - target
                    if diff == 0:
                        return sum3
                    diff = - diff if (diff < 0) else diff
                    if closest_difference[0] > diff:
                        closest_difference = (diff, sum3)
        return closest_difference[1]

