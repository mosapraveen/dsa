class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        i=0
        while i<len(s) and s[i]==" ":
            i+=1
        
        sign=1
        if(i<len(s) and (s[i]=='-' or s[i]=='+')):
            if(s[i]=='+'):
                sign=1
            else:
                sign=-1
            i+=1
        
        num=0
        while(i<len(s) and s[i].isdigit()):
            num=num*10+int(s[i])
            if num*sign > 2**31-1:
                return 2**31-1
            if num*sign < -2**31:
                return -2**31
            i+=1
        
        return num*sign
