class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = nums1+nums2
        nums3.sort()

        low = 0
        high = len(nums3)

        if len(nums3) % 2 != 0:
            mid = (high)//2
            return nums3[mid] 
        elif len(nums3) % 2 ==0:
            mid = (high)//2
            return (nums3[mid-1]+nums3[mid])/2



        