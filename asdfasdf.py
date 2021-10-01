def ASD(A,B):
    cnt = 0
    K=0
    while True:
        cnt += 1
        K += cnt*B
        if cnt*B>A:
            K -= cnt*B
            break
    return(K)




K = input("정수를 입력해주세요: ")
N = input("원하는 배수1을 입력해주세요: ")
M = input("원하는 배수2를 입력해주세요: ")

X = ASD(K,N)
print(X)


