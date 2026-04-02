class Solution:
    def frogJump(self,heights):
        n=len(heights)
        dp=[0]*n
        dp[0],dp[1]=0,abs(heights[1]-heights[0])
        for i in range(2,n):
            dp[i]=min(dp[i-2]+abs(heights[i]-heights[i-2]),dp[i-1]+abs(heights[i]-heights[i-1]))
        return dp[n-1]
    
heights=list(map(int,input('Enter the heights:').split()))
obj=Solution()
print(obj.frogJump(heights))