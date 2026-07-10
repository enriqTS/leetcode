class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:  # noqa: F821
        i = 0 # ponteiro de escrita, aponta para onde o valor será escrito
        j = 0 # ponteiro de leitura, aponta os valores que estão sendo analisados

        while j < len(nums): # Verifica se o ponteiro de leitura não chegou no final
            if j == 0 or nums[j] != nums[j-1]: # Se estamos no primeiro item ou se o valor mudou
                nums[i] = nums[j] # copia para a posição de escrita
                count = 1 # Volta o count para 1 (valor novo) ou inicia o count, caso j == 0
                j += 1 # incrementa o ponteiro de leitura
                i += 1 # incrementa o ponteiro de escrita 
            elif nums[j] == nums[j-1] and count < 2: # Caso os valores sejam iguais e o count menor que 2, ainda podemos mexer o ponteiro de escita
                nums[i] = nums[j]
                i += 1
                j += 1
                count += 1 
            else: # Caso os valores seham iguais o count >= 2, o ponteiro de escrita já está no lugar certo, precisamos apenas achar um valor diferente
                j += 1

        return i # Ponteiro de escrita é a quantidade de itens no final