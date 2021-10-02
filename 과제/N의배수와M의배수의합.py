def mul(A,B):
    cnt = 0
    K=0
    A = int(A)
    B = int(B)
    while True:
        cnt += 1
        K += cnt*B
        if cnt*B>A:
            K -= cnt*B
            break
    return(K)




K = int(input("정수를 입력해주세요: "))
N = int(input("원하는 배수1을 입력해주세요: "))
M = int(input("원하는 배수2를 입력해주세요: "))

X = int(mul(K,N))
Y = int(mul(K,M))
Z = int(mul(K,N*M))
print(X+Y-Z)


