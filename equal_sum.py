class Solution:
    def equalSum(self,nums):
        target=sum(nums)
        if target%2!=0:
            return False
        t=target//2
        m=len(nums)
        dp=[[False]*(t+1)for i in range(m+1)]
        for i in range(m+1):
            dp[i][0]=True
        for i in range(1,m+1):
            for j in range(1,t+1):
                if nums[i-1]>j:
                    dp[i][j]=dp[i-1][j]
                else:
                    if dp[i-1][j]==True or dp[i-1][j-nums[i-1]]==True:
                        dp[i][j]=True
        return dp[m][t]
    
if __name__=='__main__':
    nums=list(map(int,input('Enter numbers:').split()))
    obj=Solution()
    print(obj.equalSum(nums))