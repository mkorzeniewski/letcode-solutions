import sys
from typing import List


class ThreeSumsClosest:
    @staticmethod
    def threeSum(nums: List[int], target: int) -> int:
        closest_difference = (sys.maxsize, 0)
        for i in range(0, len(nums)-2):
            two_sums = [nums[i] + nums[i+1] - target]
            for j in range(i + 2, len(nums)):
                for k in range(0, len(two_sums)):
                    sum3 = nums[j] + two_sums[k]
                    if sum3 == 0:
                        return sum3 + target
                    abs_sum3 = - sum3 if (sum3 < 0) else sum3
                    if closest_difference[0] > abs_sum3:
                        closest_difference = (abs_sum3, sum3 + target)
                two_sums.append(nums[i] + nums[j] - target)

        return closest_difference[1]
