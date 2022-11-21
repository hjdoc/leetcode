class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        merged_array = sorted(nums1+nums2)
        if not len(merged_array) % 2 == 0:
            # division rounds up odd len to find median index
            return merged_array[len(merged_array)/2]
        else:
            # return mean of two middle nums
            key = len(merged_array)/2
            return (merged_array[key] + float(merged_array[key-1]))/2     
        
