from typing import List


class TwoSums:
    @staticmethod
    def twoSum(nums: List[int], target: int) -> List[int]:
        already_taken = dict()
        for idx, n in enumerate(nums):
            if n in already_taken:
                return [already_taken[n], idx]
            already_taken[target - n] = idx
        return list()
