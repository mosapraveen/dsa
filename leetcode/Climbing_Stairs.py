class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        a,b=1,2
        if(n<=2):
            return n
        for i in range(3,n+1):
            a,b=b,a+b
        return b
        
