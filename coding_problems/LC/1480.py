from typing import List


def runningSum(self, nums: List[int]) -> List[int]:
    result = nums
    for i in range(0, len(nums)):
        if (i == 0):
            continue
        else:
            result[i] = result[i] + nums[i-1]

    return result