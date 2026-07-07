class Solution:

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        i = m - 1 # Ponteiro para os valores de nums1
        j = n - 1 # Ponteiro para os valores de nums2
        k = m + n - 1 # Ponteiro para o final de nums1, que está preenchido com 0s

        # Trata dos casos especiais onde o vetor nums1 vem vazio, basta copiar nums2
        if m == 0:
            for f in range(m+n):
                nums1[f] = nums2[f]
        # Trata todos os outros casos
        else:        
            # Enquanto nums1 e nums2 tem elementos ainda, copia para nums1, comecando pelo final, pois já está sortido            
            while i >= 0 and j >= 0: 
                # Se o item final de nums1 for maior que o de nums2, coloca ele no final de nums1 (preenchido com 0s) 
                # e decrementa o ponteiro de nums1
                if nums1[i] >= nums2[j]:
                    nums1[k] = nums1[i]
                    i -= 1
                # Se o item final de nums2 for maior que o de nums1, coloca ele no final de nums1 (preenchido com 0s) 
                # e decrementa o ponteiro de nums2
                elif nums1[i] < nums2[j]:
                    nums1[k] = nums2[j]
                    j -= 1
                # Decrementa o ponteiro que aponta para o final de nums1, ou seja, segue para o proximo valor
                k -= 1
            # Caso esgotemos os valores de nums1 porém ainda existem em nums2, basta copiar os valores para nums1, pois já estão em ordem
            if i < 0 and j >= 0:
                while j >= 0:
                    nums1[k] = nums2[j]
                    j -= 1
                    k -= 1



""" Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].

Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1. """

