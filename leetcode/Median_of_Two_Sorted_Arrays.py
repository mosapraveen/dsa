class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        i=0
        j=0
        high1=len(nums1)
        high2=len(nums2)
        c=[]
        while i<high1 and j<high2:
            if(nums1[i]<nums2[j]):
                c.append(nums1[i])
                i=i+1
            else:
                c.append(nums2[j])
                j=j+1
        
        while i<high1:
            c.append(nums1[i])
            i+=1

        while j<high2:
            c.append(nums2[j])
            j+=1

        n=len(c)
        if(n%2==0):
            return (c[n//2 - 1] + c[n//2]) / 2.0
        else:
            return c[n//2]
