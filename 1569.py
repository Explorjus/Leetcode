nums = [3,4,5,1,2]

rest = nums[1:]
mid = len(rest) // 2

print(mid)

left = rest[:mid]
right = rest[mid:]

print(left)
print(right)

for i in range(len(left)):

    