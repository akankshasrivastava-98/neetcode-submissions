class Solution:
    def getEatinghours(self,piles,k):
        hours = 0
        for pile in piles:
            if pile>k:
                if pile%k !=0:
                    hours += pile//k + 1
                else:
                    hours += pile//k
            else:
                hours +=  1
        return hours

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minHour = float('inf')
        low = 1
        high = max(piles)
        while low<=high:
            mid = (low+high)//2
            requiredHour = self.getEatinghours(piles,mid)
            if requiredHour <=h:
                minHour = min(minHour,mid)
                high = mid-1
            else:
                low = mid+1
        return minHour


        