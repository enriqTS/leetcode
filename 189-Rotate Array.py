class Solution:
    def rotate(self, nums: List[int], k: int) -> None:  # noqa: F821
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums) # Tamanho do vetor
        k %= n # Divide k pelo tamanho e pega o resto, porque de acordo com matemática, se você tem um vetor de n=7 e um k=10, isso equivale a uma rotação completa,
               # que volta o vetor para o original e então uma rotação de 3, que é o resto de k % n, ou 10 % 7

        r_k = nums[n-k::] # Pega os valores de nums iniciando em n-k (As últimas posições, que serão posicionadas no início)
        r_n = nums[:n-k:] #Pega os valores de nums terminando em n-k (As primeiras posições, que serão posicionadas no final)

        nums[:] = r_k + r_n # Concatena os dois vetores obtidos e os coloca em nums, como pedido pelo exercicio

    def rotate(self, nums: List[int], k: int) -> None:  # noqa: F811, F821
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        nums[:] = nums[-k:] + nums[:-k]   # Sugestão da IA, no lugar de vetores auxiliares, simplesmente concatene diretamente
        # nums[-k:] -> Pega os ultimos k valores do array
        # nums[:-k] -> Pega os valores até n-k
        # São equivalentes a nums[n-k:] + nums[:n-k]