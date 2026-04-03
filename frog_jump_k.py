class Solution:
    def frogJump(self,heights,k):
        n=len(heights)
        dp=[0]*n
        for i in range(1,n):
            val=float('inf')
            for j in range(i,i-k,-1):
                if j>=0:
                    res=dp[j-1]+abs(heights[i]-heights[j-1])
                    if res<val:
                        val=res
                else:
                    break
            dp[i]=val
        return dp[n-1]
    
heights=list(map(int,input('Enter the heights:').split()))
k=int(input('Enter the distances:'))
obj=Solution()
print(obj.frogJump(heights,k))
