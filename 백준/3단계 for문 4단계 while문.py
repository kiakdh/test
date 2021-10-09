N = int(input())

for i in range(1,10):
    print(f"{N} * {i} = {N*i}")



T = int(input())

for i in range(T):
    A, B = map(int, input().split())
    print(A+B)


import sys

T = int(input())

for i in range(T):
    A, B = map(int, sys.stdin.readline().split())
    print(A+B)



N = int(input())

for i in range(N):
    print(i+1)



N = int(input())
for i in range(N):
    print(N-i)



T = int(input())

for i in range(T):
    A,B = map(int,input().split())
    print(f"Case #{i+1}: {A} + {B} = {A+B}")



n = int(input())

for i in range(n):
    for j in range(i+1):
        print("*",end="")
        if j == i:
            print("")


n = int(input())

for i in range(n):
    s = "*"*(i+1)
    print(f"{s:>{n}}")


while True:
    A, B = map(int, input().split())
    C = A+B
    if C == 0:
        break
    else:
        print(C)
    


while True:
    try:
        A, B = map(int, input().split())
        print(A+B)

    except EOFError:
        break



N = int(input())
numbers = N
cnt = 0


while True:
   data = numbers
   d = data%10+data//10
   numbers = (data%10)*10 + d%10
   cnt += 1
   if numbers == N:
       break
print(cnt)