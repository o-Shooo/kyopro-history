n, q = map(int, input().split(" "))
a = list(map(int, input().split(" ")))

s = []
for i in range(n):
    if i == 0:
        s.append(a[i])
    else:
        s.append(s[i - 1] + a[i])

result = []
for _ in range(q):
    l, r = map(int, input().split(" "))
    if l == 1:
        result.append(s[r - 1])
    else:
        result.append(s[r - 1] - s[l - 1 - 1])

print(*result, sep="\n")
