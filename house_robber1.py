class Solution:
    def houseRobber(self,money):
        n=len(money)
        if n==1:
            return money[0]
        dp=[0]*n
        dp[0],dp[1]=money[0],max(money[0],money[1])
        for i in range(2,n):
            dp[i]=max(dp[i-1],dp[i-2]+money[i])
            
        return dp[n-1]
    
if __name__=='__main__':
    money=list(map(int,input('Enter the money in the houses:').split()))
    obj=Solution()
    print(obj.houseRobber(money))
    