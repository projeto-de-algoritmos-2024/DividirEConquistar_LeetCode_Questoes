class Solution:
    def createSortedArray(self, instrucoes: List[int]) -> int:
        mod = 10**9 + 7
        max_val = max(instrucoes)
        BIT = [0] * (max_val + 1) 
        
        def consulta(indice): 
            soma = 0 
            while indice > 0:
                soma += BIT[indice]
                indice -= indice & -indice
            return soma
        
        def atualiza(indice, valor):
            while indice <= max_val:
                BIT[indice] += valor
                indice += indice & -indice
                
        custo = 0 
        for i, instrucao in enumerate(instrucoes):
            custo_esquerda = consulta(instrucao - 1)  
            custo_direita = i - consulta(instrucao) 
            custo += min(custo_esquerda, custo_direita)
            atualiza(instrucao, 1)
        
        return custo % mod