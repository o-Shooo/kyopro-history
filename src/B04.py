N = input()

Answer = 0
for i, n in enumerate(reversed(N)):
    if n == "1":
        Answer += 2**i
print(Answer)
