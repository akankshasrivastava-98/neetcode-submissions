class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        # diffDict = {}
        # for i in range(n):
        #     diff = target - nums[i]
        #     if diff in diffDict:
        #         return [diffDict[diff],i]
        #     else:
        #         diffDict[nums[i]] = i
        # return []
        arr = [(nums[i], i) for i in range(len(nums))]

        arr.sort()

        i = 0
        j = n - 1

        while i < j:
            curr_sum = arr[i][0] + arr[j][0]

            if curr_sum == target:
                res = [arr[i][1], arr[j][1]]
                res.sort()
                return res

            elif curr_sum < target:
                i += 1

            else:
                j -= 1

        return []




        