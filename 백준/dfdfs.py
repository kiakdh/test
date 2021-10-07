n = int(input())
result = n
cnt = 0

while True:
    first = result%10
    last = result%10+result//10
    result = first*10+last%10
    cnt += 1
    if result == n:
        break




print(cnt)
