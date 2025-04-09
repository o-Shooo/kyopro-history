N = int(input())
A = list(map(int, input().split()))
Q = int(input())

Atari = [0] * (N + 1)
Hazure = [0] * (N + 1)
for i in range(N):
    if A[i] == 1:
        Atari[i + 1] = Atari[i] + 1
        Hazure[i + 1] = Hazure[i]
    else:
        Hazure[i + 1] = Hazure[i] + 1
        Atari[i + 1] = Atari[i]

for i in range(Q):
    L, R = map(int, input().split())
    if Atari[R] - Atari[L - 1] > Hazure[R] - Hazure[L - 1]:
        print("win")
    elif Atari[R] - Atari[L - 1] == Hazure[R] - Hazure[L - 1]:
        print("draw")
    else:
        print("lose")
