class Solution:
    def countSum(self,nums,k):
        m=len(nums)
        dp=[[0]*(k+1) for i in range(m+1)]
        for i in range(m+1):
            dp[i][0]=1
        for i in range(1,m+1):
            for j in range(1,k+1):
                if nums[i-1]>j:
                    dp[i][j]=dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j]+dp[i-1][j-nums[i-1]]
        return dp[m][k]
    
    
if __name__=='__main__':
    values=list(map(int,input('Enter the numbers:').split()))
    k=int(input('Enter the k value:'))
    obj=Solution()
    print(obj.countSum(values,k))
    