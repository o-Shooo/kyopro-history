N, Q = map(int, input().split())
A = list(map(int, input().split()))

W = [0] * (N + 1)
for i in range(N):
    W[i + 1] = W[i] + A[i]

for i in range(Q):
    L, R = map(int, input().split())
    print(W[R] - W[L - 1])
