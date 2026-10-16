def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2 #wyznacza indeks srodka listy
    left = merge_sort(arr[:mid]) #lewa strona od poczatku do mid
    right = merge_sort(arr[mid:]) #prawa strona od mid do konca


    seen = []
    distinc = []
    result = [] #tablica z wynikiem
    i = j = 0
    while i < len(left) and j < len(right): 
        if left[i] <= right[j]:
            result.append(left[i]); i += 1
            if left[i-1] not in seen:
                seen.append(left[i-1])
                
        else:
            result.append(right[j]); j += 1
            if right[j-1] not in seen:
                seen.append(right[j-1])
                
    result.extend(left[i:])
    result.extend(right[j:])
    print(seen)
    return result

print(merge_sort([12, 11, 13, 5, 6, 7]))  # [5, 6, 7, 11, 12, 13]
