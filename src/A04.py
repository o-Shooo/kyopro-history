N = int(input())

Answer = ""
for i in [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]:
    wari = 2**i
    print((N // wari) % 2, end="")
