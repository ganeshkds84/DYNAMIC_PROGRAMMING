class Solution:
    def minimumPath(self,grid):
        m=len(grid)
        n=len(grid[0])
        dp=[[0]*n for i in range(m)]
        if n==0:
            res=0
            for i in range(m):
                res+=grid[i][0]
        for i in range(n):
            dp[0][i]=grid[0][i]
        for i in range(1,m):
            for j in range(n):
                if j==0:
                    dp[i][j]=grid[i][j]+min(dp[i-1][j],dp[i-1][j+1])
                elif j==n-1:
                    dp[i][j]=grid[i][j]+min(dp[i-1][j],dp[i-1][j-1])
                else:
                    dp[i][j]=grid[i][j]+min(dp[i-1][j-1],dp[i-1][j],dp[i-1][j+1])
        final=float('inf')
        for i in range(n):
            res=dp[m-1][i]
            if res<final:
                final=res
            
        return final
    
if __name__=='__main__':
    m=int(input('Enter number of rows:'))
    n=int(input('Enter number of columns:'))
    grid=[list(map(int,input(f'Enter row {i} elements:').split())) for i in range(m)]
    obj=Solution()
    print(obj.minimumPath(grid))
    