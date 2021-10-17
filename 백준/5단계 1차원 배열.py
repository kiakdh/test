n = int(input())
nlist = list(map(int, input().split()))


M = max(nlist)
m = min(nlist)

print(f"{m} {M}")



nlist = []

for i in range(9):
    n = int(input())
    nlist.append(n)

M = max(nlist)

print(M)
print(nlist.index(M)+1)



nlist = [0,0,0,0,0,0,0,0,0,0]
cnt = 0


A = int(input())
B = int(input())
C = int(input())
T = A*B*C
Ts = str(T)

tlist = list(map(int,str(Ts)))

for i in range(len(tlist)):
    n = tlist[i] 
    nlist[n] += 1

for k in range(len(nlist)):
    print(nlist[k])



nlist = []

for i in range(10):
    k = int(input())
    nlist.append(k%42)

n = set(nlist)
nlist2 = list(n)

print(len(nlist2))



import sys

n = int(input())
score = list(map(int, sys.stdin.readline().split()))
M = max(score)
sum = 0

for i in range(len(score)):
    sum += score[i]/M*100

print(sum/n)