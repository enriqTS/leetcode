class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = prices[0] # Valor em que eu vou comprar a ação, inicialmente é o primeiro valor do vetor
        max_profit = 0 # Valor do lucro máximo que eu posso ter, inicialmente é 0, pois não comprei nenhuma ação ainda
        for i in range(len(prices)): 
            if prices[i] < buy_price: # Se o preço de compra for menor que o preco atual do vetor, eu atualizo o valor de compra para o preço atual
                buy_price = prices[i]
            profit = prices[i] - buy_price # Verifica o lucro que teria se vendesse "hoje"
            if profit > max_profit: # Verifica se é o maior lucro que já tive, se sim, atualiza o valor do lucro máximo
                max_profit = profit
        
        return max_profit # Retorna o lucro máximo