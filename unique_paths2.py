class Solution:
    def uniquePaths(self,matrix):
        m=len(matrix)
        n=len(matrix[0])
        if matrix[0][0]==1:
            return 0
        dp=[[0]*n for i in range(m)]
        dp[0][0]=1
        #firstRow
        for i in range(1,n):
            if matrix[0][i]==0:
                dp[0][i]=dp[0][i-1]
        #firstColumn
        for j in range(1,m):
            if matrix[j][0]==0:
                dp[j][0]=dp[j-1][0]
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j]==1:
                    dp[i][j]=0
                else:
                    dp[i][j]=dp[i-1][j]+dp[i][j-1]
        
        return dp[m-1][n-1]
    
if __name__=='__main__':
    rows=int(input('Enter number of rows:'))
    cols=int(input('Enter number of columns:'))
    matrix=[list(map(int,input(f'Enter {i} row numbers:').split())) for i in range(rows)]
    obj=Solution()
    print(obj.uniquePaths(matrix))
    
    
    