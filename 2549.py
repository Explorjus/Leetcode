nums1 = [1,4,3,5,6,]
nums2 = [1,2,4,3,5,6]


i = 0
j = 0
wynik = -1

while i < len(nums1) and j < len(nums2):
    if nums1[i] == nums2[j]:
        wynik = nums2[j]
        break
    elif nums1[i] < nums2[j]:
        i += 1
    else:
        j += 1

print(wynik)
