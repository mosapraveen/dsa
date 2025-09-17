class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr_max=curr_min=ans=nums[0]

        for i in range(1,len(nums)):
            a=nums[i]

            temp=curr_max
            curr_max=max(a,a*curr_max,a*curr_min)
            curr_min=min(a,a*temp,a*curr_min)
            ans=max(ans,curr_max)

        return ans
