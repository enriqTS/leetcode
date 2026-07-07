class Solution:

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        i = m - 1 # nums1
        j = n - 1 # nums2
        k = m + n - 1

        if m == 0:
            for f in range(m+n):
                nums1[f] = nums2[f]
        else:                    
            while i >= 0 and j >= 0: 
                if nums1[i] >= nums2[j]:
                    nums1[k] = nums1[i]
                    i -= 1
                elif nums1[i] < nums2[j]:
                    nums1[k] = nums2[j]
                    j -= 1
                k -= 1
            if i < 0 and j >= 0:
                while j >= 0:
                    nums1[k] = nums2[j]
                    j -= 1
                    k -= 1