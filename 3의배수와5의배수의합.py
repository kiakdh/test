N = int(input("정수를 입력해주세요:"))
cnt3 = 0
cnt5 = 0
cnt15 = 0
N3 = 0
N5 = 0
N15 = 0

while True:
    cnt3 += 1
    N3 +=  cnt3*3
    if cnt3*3>N:
        N3 -= cnt3*3
        break

while True:
    cnt5 += 1 
    N5 += cnt5*5
    if cnt5*5>N:
        N5 -= cnt5*5
        break

while True:
    cnt15 += 1
    N15 += cnt15*15
    if cnt15*15 > N:
        N15 -= cnt15*15
        break
    
    print(N3+N5-N15)