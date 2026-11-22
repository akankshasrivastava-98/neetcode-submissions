class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        i = 0
        j = n-1
        totalWater = 0
        leftMax = 0
        rightMax = 0
        while i<j:     
            leftMax = max(leftMax,height[i])
            rightMax = max(rightMax,height[j])
            if height[i] > height[j]:
                curWater = min(leftMax,rightMax)-height[j]
                j-=1
            else:
                curWater = min(leftMax,rightMax)-height[i]
                i+=1
            if curWater > 0:
                totalWater += curWater
        return totalWater
            

        