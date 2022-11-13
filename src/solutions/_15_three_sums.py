from typing import List


class ThreeSums:
    @staticmethod
    def threeSum(nums: List[int]) -> List[List[int]]:
        sums_of_pairs = {}
        result = set()
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] not in sums_of_pairs:
                    sums_of_pairs[nums[i] + nums[j]] = set()
                sums_of_pairs[nums[i] + nums[j]].add((i, j)) if nums[i] < nums[j] else sums_of_pairs[nums[i] + nums[j]].add((j, i))

        for n in range(0, len(nums)):
            if -nums[n] in sums_of_pairs:
                for i, j in sums_of_pairs[-nums[n]]:
                    if n not in (i, j):
                        if nums[n] < nums[i]:
                            result.add((nums[n], nums[i], nums[j]))
                        elif nums[n] < nums[j]:
                            result.add((nums[i], nums[n], nums[j]))
                        else:
                            result.add((nums[i], nums[j], nums[n]))

        return [list(x) for x in result]
