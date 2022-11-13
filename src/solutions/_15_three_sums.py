from typing import List


class ThreeSums:
    @staticmethod
    def threeSum(nums: List[int]) -> List[List[int]]:
        result = set()
        for i in range(0, len(nums)):
            existing_numbers = set()
            for j in range(i + 1, len(nums)):
                if -nums[i] -nums[j] in existing_numbers:
                    result.add(tuple(sorted((nums[i], nums[j], -nums[i] - nums[j]))))
                else:
                    existing_numbers.add(nums[j])

        return [list(x) for x in result]
