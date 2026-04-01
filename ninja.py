class Solution:
    def ninjaTraining(self,matrix):
        rows=len(matrix)
        cols=len(matrix[0])
        dp=[[0]*cols for _ in range(rows)]
        for i in range(1):
            for j in range(cols):
                dp[i][j]=matrix[i][j]
        for i in range(1,rows):
            for j in range(cols):
                if j==0:
                    dp[i][j]=matrix[i][j]+max(dp[i-1][1],dp[i-1][2])
                elif j==1:
                    dp[i][j]=matrix[i][j]+max(dp[i-1][0],dp[i-1][2])
                else:
                    dp[i][j]=matrix[i][j]+max(dp[i-1][0],dp[i-1][1])
                    
        final=0
        for j in range(cols):
            res=dp[rows-1][j]
            if res>final:
                final=res
        return final
    
matrix= [[10, 40, 70], [20, 50, 80], [30, 60, 90],[10,20,30]]
obj=Solution()
print(obj.ninjaTraining(matrix))