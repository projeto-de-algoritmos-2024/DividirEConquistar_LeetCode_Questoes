class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i, j = 0, 0
        arrayResultante = [] # array resultante do merge dos dois arrays

        # mescla os dois arrays de forma linear
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                arrayResultante.append(nums1[i])
                i += 1
            else:
                arrayResultante.append(nums2[j])
                j += 1

        # elementos restantes de nos arrays se um chega ao final
        while i < len(nums1):
            arrayResultante.append(nums1[i])
            i += 1
        while j < len(nums2):
            arrayResultante.append(nums2[j])
            j += 1

        # mediana do array mesclado
        total_length = len(arrayResultante)
        if total_length % 2 == 1:
            return arrayResultante[total_length // 2] #comprimento ímpar
        else:
            mid1, mid2 = total_length // 2 - 1, total_length // 2
            return (arrayResultante[mid1] + arrayResultante[mid2]) / 2 #comprimento par
