class Solution:
    # Minha solucao inicial 
    def removeElement1(self, nums: List[int], val: int) -> int:
        k = 0 # Quantidade de itens diferente de val

        for i in range(len(nums)): # For loop que substitui os itens invalidos por -1 e incrementa k se for valido
            if nums[i] == val:
                nums[i] = -1
            else:
                k += 1

        n = [0] * len(nums) # Vetor auxiliar do mesmo tamanho de nums, preenchido por 0
        i = 0 # iterador
        j = 0 # iterador

        while i < len(nums) and j < k: # Loop que checa todos os itens de nums e salva os válidos em n
            if nums[i] != -1:
                n[j] = nums[i]
                j += 1
            i += 1
        
        nums[:] = n # Salva os valores de n em nums

        return k # Retorna a quantidade de itens válidos, como solicitado pelo exercicio
    
    # Solucao mais otimizada
    def removeElement2(self, nums: List[int], val: int) -> int:
        i = 0 # ponteiro para todos os itens do vetor nums
        k = 0 # ponteiro para os itens validos do vetor nums

        while i < len(nums): # Loop que checa se um item é valido, se for, coloca ele na posicao valida disponivel 
            if nums[i] != val: # Checa se não é o valor proibido
                nums[k] = nums[i] # Se não for, coloca na primeira posicao valida disponivel
                k += 1 # Incrementa o ponteiro indicando posicao válida (sempre no inicio do vetor)
            i += 1 # Incrementa o ponteiro do valor que está sendo comparado

        return k # Retorna a quantidade de itens válidos, como solicitado pelo exercicio