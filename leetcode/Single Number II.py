class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        praveen={}
        for i in nums:
            praveen[i]=praveen.get(i,0)+1

        for i in praveen:
            if(praveen[i]==1):
                return i
