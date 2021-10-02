
N = int(input("정점의 수를 입력해주세요: "))
E = int(input("간선의 수를 입력해주세요: "))
R = []

D = []
F = []
Dv = []
for i in range(N):
    F.append(i)
    Dv.append([i,999999])

for i in range(E):
    i2 = i+1
    A1 = int(input("간선%d의 출발 노드를 입력해주세요: "%i2))
    A2 = int(input("간선%d의 도착 노드를 입력해주세요: "%i2))
    A3 = int(input("간선%d의 가중치를 입력해주세요: "%i2))
    R.append([A1,A2,A3])



stp = int(input("시작 노드를 입력해주세요: "))-1
Dv[stp][1] = 0


'''방문'''
'''거리계산'''

mylist=[list(map(int, input().split())) for _ in range(n)]
newlist=[(i,j) for i in range(n) for j in range(m) if mylist[i][j]==stp]


'''
https://minjoos.tistory.com/2
https://minjoos.tistory.com/3
https://justkode.kr/algorithm/python-dijkstra
'''