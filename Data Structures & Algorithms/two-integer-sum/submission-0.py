class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        diffDict = {}
        for i in range(n):
            diff = target - nums[i]
            if diff in diffDict:
                return [diffDict[diff],i]
            else:
                diffDict[nums[i]] = i
        return []
        