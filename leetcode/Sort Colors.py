class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(1, len(nums)):
            sort=nums[i]
            j=i-1
            while j>=0 and sort<nums[j]:
                nums[j+1]=nums[j]
                j-=1
                nums[j+1]=sort
            nums[j+1]
