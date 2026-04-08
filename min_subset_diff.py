class Solution:
    def minSubset(self,nums):
        m=len(nums)
        total=sum(nums)
        target=total//2
        dp=[[False]*(target+1) for i in range(m+1)]
        for i in range(m+1):
            dp[i][0]=True
        for i in range(1,m+1):
            for j in range(1,target+1):
                if nums[i-1]>j:
                    dp[i][j]=dp[i-1][j]
                else:
                    if dp[i-1][j]==True or dp[i-1][j-nums[i-1]]==True:
                        dp[i][j]=True
        for i in range(target,-1,-1):
            if dp[m][i]==True:
                required=i
                break
            
        return total-2*required
    
if __name__=='__main__':
    nums=list(map(int,input('Enter the numbers:').split()))
    obj=Solution()
    print(obj.minSubset(nums))