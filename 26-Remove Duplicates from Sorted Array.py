class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0 # Ponteiro/iterador que marca a posicao em que vamos colocar o item não duplicado
        j = 1 # Ponteiro/iterador que marca o valor que estamos comparando com o valor presente em i

        while i < len(nums) and j < len(nums): # Enquanto estiver dentro do vetor
            if nums[i] == nums[j]: # Se o valor de nums[i] for igual a nums[j], é duplicado, vamos para o próximo
                j += 1
            else: # Se encontramos um valor nums[i] != nums[j], não é duplicado, incrementamos i e colocamos ele na posicão correta dele
                i += 1
                nums[i] = nums[j]
        
        return i+1 # Retornamos a quantidade de itens não duplicados do vetor, como i marca a posicao dos não duplicados, basta somar 1
