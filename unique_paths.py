class Solution:
    def uniquePaths(self,m,n):
        if m==1 or n==1:
            return 1
        dp=[[1]*n for i in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j]=dp[i-1][j]+dp[i][j-1]
        return dp[m-1][n-1]

if __name__=='__main__':
    matrix=[]
    m=int(input('Enter number of rows:'))
    n=int(input('Enter number of columns:'))
    
    for i in range(m):
        row=list(map(int,input().split()))
        matrix.append(row)
    
    obj=Solution()
    print(obj.uniquePaths(len(matrix),len(matrix[0])))