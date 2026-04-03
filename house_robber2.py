class Solution:
    def robHouse(self,money):
        n=len(money)
        if n==1:
            return money[0]
        case1=self.robRange(money,0,n-2)
        case2=self.robRange(money,1,n-1)
        return max(case1,case2)
        
    def robRange(self,money,start,end):
        n=end-start+1
        if n==1:
            return money[start]
        dp=[0]*n
        dp[0],dp[1]=money[start],max(money[start],money[start+1])
        for i in range(2,n):
            dp[i]=max(dp[i-1],dp[i-2]+money[start+i])
        return dp[n-1]
    
if __name__=='__main__':
    money=list(map(int,input('Enter money in the houses:').split()))
    obj=Solution()
    print(obj.robHouse(money))
    