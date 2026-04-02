class Sollution:
    def climbStairs(self,n):
        start=1
        end=1
        for i in range(2,n+1):
            res=start+end
            start=end
            end=res
        return res
        
n=int(input('Enter number of stairs:'))
obj=Sollution()
print(obj.climbStairs(n))