class Solution:
    def majorityElement(self, nums: List[int]) -> int:  # noqa: F821
        count = {} # Cria um dicionario (hash map) que irá salvar o número e a quantidade de vezes que ele apareceu

        for num in nums: # Para cada número no vetor, vamos adicionar uma aparição dele ao dicionário
            if num in count: # Se o numero já existe no dicionário adiciona uma aparição
                count[num] += 1
            else: # Se não, adiciona o número e sua primeira aparição
                count[num] = 1
        
        return max(count, key=count.get) # Retorna o valor que aparece mais vezes, consequentemente, o número que aparece mais de len(nums)/2 vezes

from collections import Counter  # noqa: E402

def majorityElement(self, nums: List[int]) -> int:  # noqa: F821
    # Counter(nums) returns a dict-like object: {element: frequency, ...}
    count = Counter(nums)
    
    # You can still use max(key=count.get) like before
    return max(count, key=count.get)
    
    # Or use Counter's built‑in method:
    # return count.most_common(1)[0][0]
        