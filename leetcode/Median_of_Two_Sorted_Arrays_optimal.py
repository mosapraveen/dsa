#optimal approach

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        merged = nums1 + nums2
        a= sorted(merged)
        n = len(a)
        
        if n % 2 == 0:
            mid1 = n // 2
            mid2 = mid1 - 1
            return (a[mid1] + a[mid2]) / 2.0
        else:
            return a[n//2]
