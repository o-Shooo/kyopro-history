N = int(input())
A = list(map(int, input().split()))

Answer = False
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            if A[i] + A[j] + A[k] == 1000:
                Answer = True
                break

if Answer:
    print("Yes")
else:
    print("No")
