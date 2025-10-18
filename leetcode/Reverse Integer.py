class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        re=0
        ne=0
        if x<0:
            ne=1
            x=-x
        while x!=0:
            n=x%10
            re=re*10+n
            x=x//10
        if ne==1:
            re=-re
        if re < -2**31 or re > 2**31-1:
            return 0
        return re
            
