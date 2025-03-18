A, B = map(int, input().split())

Answer = False
for i in range(A, B + 1):
    if 100 % i == 0:
        Answer = True

if Answer:
    print("Yes")
else:
    print("No")
