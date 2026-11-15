class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countDict = {}
        for n in nums:
            if n in countDict:
                countDict[n]+=1
            else:
                countDict[n] = 1
        ans = []
        i = 1
        res = OrderedDict(sorted(countDict.items(), key=lambda item: item[1], reverse=True))
        for x,v in res.items():
            if i>k:
                break
            ans.append(x)
            i+=1
        return ans




        