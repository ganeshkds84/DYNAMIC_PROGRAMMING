class Solution():
    def minimumPath(self,triangle):
        m=len(triangle)
        dp=[[float('inf')]*m for i in range(m)]
        dp[0][0]=triangle[0][0]
        for i in range(1,m):
            dp[i][0]=triangle[i][0]+dp[i-1][0]
        for i in range(1,m):
            for j in range(1,i+1):
                dp[i][j]=triangle[i][j]+min(dp[i-1][j-1],dp[i-1][j])
        final=float('inf')
        for i in range(m):
            res=dp[m-1][i]
            if res<final:
                final=res
        return final
    
if __name__=='__main__':
    m=int(input('Enter number of rows of triangle:'))
    values=[list(map(int,input(f'Enter {i+1} elements:').split())) for i in range(m)]
    obj=Solution()
    print(obj.minimumPath(values))
    