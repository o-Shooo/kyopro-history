n, k = input().split(" ")

count = 0
for i in range(1, int(n) + 1):
    for j in range(1, int(n) + 1):
        if (int(k) - i - j) <= int(n) and (int(k) - i - j) >= 1:
            count += 1
print(count)
