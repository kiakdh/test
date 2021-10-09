n = int(input())
nlist = list(map(int, input().split()))


M = max(nlist)
m = min(nlist)

print(f"{m} {M}")