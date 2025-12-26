arr = list(map(int, input().split()))

max_count = 0
count = 0

for i in arr:
    if i == 1:
        count += 1
        if count > max_count:
            max_count = count
    else:
        count = 0

print( max_count)