N = int(input("정수를 입력해주세요:"))

for i in range(0,N//3,1):
    i += i
A *= 3

for i in range(0,N//5,1):
    B += i
B *= 5

print(A+B)