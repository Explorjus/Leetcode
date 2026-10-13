list1 = [1,4,6,4,7]
list2 = [2,1,5,6,4,3,]


merged = list1 + list2
        
for j in merged:
    for i in merged:
        if merged[j] < merged[i]:
            merged[i], merged[j] = merged[j], merged[i]
            
            
print(merged)