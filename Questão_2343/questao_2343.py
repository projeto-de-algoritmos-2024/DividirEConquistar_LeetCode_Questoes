class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        resultado = [] 
        for k, trim in queries:
            numeros_recortados = [(num[-trim:], i) for i, num in enumerate(nums)]  
            numeros_recortados.sort()  
            resultado.append(numeros_recortados[k-1][1])  
        return resultado
