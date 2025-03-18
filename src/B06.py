n = int(input())
a = list(map(int, input().split(" ")))
q = int(input())

x = []
for i in range(n):
    if i == 0:
        if a[i] == 1:
            x.append({"hit": 1, "miss": 0})
        else:
            x.append({"hit": 0, "miss": 1})
    else:
        if a[i] == 1:
            x.append({"hit": x[i - 1]["hit"] + 1, "miss": x[i - 1]["miss"]})
        else:
            x.append({"hit": x[i - 1]["hit"], "miss": x[i - 1]["miss"] + 1})

ans = []
for _ in range(q):
    l, r = map(int, input().split(" "))
    if l == 1:
        if x[r - 1]["hit"] > x[r - 1]["miss"]:
            ans.append("win")
        elif x[r - 1]["hit"] < x[r - 1]["miss"]:
            ans.append("lose")
        else:
            ans.append("draw")
    else:
        if (x[r - 1]["hit"] - x[l - 2]["hit"]) > (x[r - 1]["miss"] - x[l - 2]["miss"]):
            ans.append("win")
        elif (x[r - 1]["hit"] - x[l - 2]["hit"]) < (
            x[r - 1]["miss"] - x[l - 2]["miss"]
        ):
            ans.append("lose")
        else:
            ans.append("draw")

print(*ans, sep="\n")
