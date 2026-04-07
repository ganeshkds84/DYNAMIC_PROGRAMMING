class Solution:
    def subsetSum(self,arr,t):
        m=len(arr)
        dp=[[False]*(t+1) for i in range(m+1)]
        for i in range(m+1):
            dp[i][0]=True
        for i in range(1,m+1):
            for j in range(1,t+1):
                if arr[i-1]>j:
                    dp[i][j]=dp[i-1][j]
                else:
                    if dp[i-1][j]==True or dp[i-1][j-arr[i-1]]==True:
                        dp[i][j]=True
        
        return dp[m][t]
    
if __name__=='__main__':
    arr=list(map(int,input('Enter the elements:').split()))
    target=int(input('Enter target value:'))
    obj=Solution()
    print(obj.subsetSum(arr,target))