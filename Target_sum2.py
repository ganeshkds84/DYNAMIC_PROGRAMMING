class Solution:
    def findTargetSumWays(self,nums,target):
        MOD=10**9+7
        total=sum(nums)
        if abs(target)>total:
            return 0
        if (total+target)%2!=0:
            return 0
        p=(total+target)//2
        dp=[0]*(p+1)
        dp[0]=1
        for num in nums:
            for j in range(p,num-1,-1):
                dp[j]=(dp[j]+dp[j-num])%MOD
        return dp[p]    
    
if __name__=='__main__':
    nums=list(map(int,input('Enter the numbers:').split()))
    target=int(input('Enter the target value:'))
    Ashu=Solution()
    print(Ashu.findTargetSumWays(nums,target))