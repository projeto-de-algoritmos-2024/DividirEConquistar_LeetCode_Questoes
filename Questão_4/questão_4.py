class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i, j = 0, 0
        arrayResultante = [] # array resultante do merge dos dois arrays

        def merge_sort(arr):
            if len(arr) <= 1:
                return arr

            # divide o array em dois
            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])

            # mescla metades quando ordenadas ou tamanho 2
            return merge(left, right)

        # faz o merge das metades de forma linear
        def merge(left, right):
            merged = []
            i = j = 0

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1

            # Adiciona os elementos restantes de cada lado
            merged.extend(left[i:])
            merged.extend(right[j:])

            return merged

        num1Sorted = merge_sort(nums1)
        num2Sorted = merge_sort(nums2)
        # mescla os dois arrays em um array resultante utilizando a mesma logica
        arrayResultante = merge(num1Sorted, num2Sorted)

        # mediana do array mesclado
        total_length = len(arrayResultante)
        if total_length % 2 == 1:
            return arrayResultante[total_length // 2] #comprimento ímpar
        else:
            mid1, mid2 = total_length // 2 - 1, total_length // 2
            return (arrayResultante[mid1] + arrayResultante[mid2]) / 2 #comprimento par
