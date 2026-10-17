class Solution:
    def minSwaps(self, nums):
        pary = []

        # dla każdej liczby liczymy sumę cyfr i zapisujemy parę (suma, liczba)
        for liczba in nums:
            suma = 0
            for cyfra in str(liczba):
                suma += int(cyfra)
            pary.append((suma, liczba))

        # sort() sam porównuje najpierw sumę, a przy remisie samą liczbę
        pary.sort()

        # docelowa kolejność liczb
        target = []
        for para in pary:
            target.append(para[1])

        arr = nums[:]
        zamiany = 0

        # ustawiamy każdą liczbę na jej docelowe miejsce
        for i in range(len(arr)):
            if arr[i] != target[i]:
                j = arr.index(target[i])
                arr[i], arr[j] = arr[j], arr[i]
                zamiany += 1

        return zamiany

nums = [18, 43, 34, 16]

rozwiazanie = Solution()
wynik = rozwiazanie.minSwaps(nums)

print(wynik)