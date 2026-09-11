class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsDict = {}

        for i, value in enumerate(nums):
            difference = target - value
            if difference in numsDict:
                return[numsDict[difference], i]
            numsDict[value] = i