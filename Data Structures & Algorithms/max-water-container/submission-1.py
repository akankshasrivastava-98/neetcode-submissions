class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxCapacity = 0
        n = len(heights)
        # for i in range(n-1):
        #     for j in range(i+1,n):
        #         curCapacity = (j-i)*min(heights[i],heights[j])
        #         maxCapacity = max(maxCapacity,curCapacity)
        # return maxCapacity
        i = 0
        j = n-1
        curCapacity = 0
        while i<j:
            curCapacity = (j-i)*min(heights[i],heights[j])
            maxCapacity = max(maxCapacity,curCapacity)
            if heights[i] <= heights[j]:
                i+=1
            else:
                j-=1
        return maxCapacity



        