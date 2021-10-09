nlist = []

for i in range(9):
    n = int(input())
    nlist.append(n)

M = max(nlist)

print(M)
print(nlist.index(M))

