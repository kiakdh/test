def purchase(n,k):
    return()



testcase = int(input("테스트케이스의 개수를 입력해주세요: "))



for i in range(1, testcase+1):
    N = input("공터의 크기를 입력해주세요: ")
    K = input("구매할 땅의 크기를 입력해주세요: ")
    answer = []
    result = purchase(N,K)
    answer.append(i)


for i in range(len(answer)):
    print(answer[i], end=" ")