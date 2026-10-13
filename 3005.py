#kod liczy ile razy wyspepują wszytskie elementy o njawekszzej czestowtliwości
#najpierw szuka jaka jest maksymalna liczba powtorzen jednego elemnetu w nums czyli max_freq
#potem znowu przechodzi po liście i dla kazdego unikalnego elementu którego czestotliwosc jest rowna tej maksymalnej dodaje te czestowliwosc do total


nums = [1, 2, 4, 7, 4, 5, 2,]


max_freq = 0. 
for i in nums:
    freq = 0            #licznik czestotliwosci w danym powtorzeniu
    for j in nums:
        if nums[i] == nums[j]:
            freq += 1
    if freq > max_freq:
        max_freq = freq

total = 0 
used = [] #lista policzonyhc elementow
for i in nums:
    if nums[i] not in used:
        freq = 0
        for j in nums:
            if nums[i] == nums[j]:
                freq += 1
        if freq == max_freq:
            total += freq
        used.append(nums[i])

print(total)