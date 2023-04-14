from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        result: float = float
        sortedList = sorted(nums1 + nums2)
        length = len(sortedList)
        if length % 2 == 0:
            start = (length/2) - 1
            end = length/2
            return float((sortedList[int(start)] + sortedList[int(end)]) / 2)
        return float(sortedList[int(length/2)])