#미래도시
INF = int(1e9)
#노드갯수, 간선갯수
n,m=5,7
#초기화
graph = [[INF] * (n+1) for _ in range(n+1)]
#자기자신은 0
for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b:
            graph[a][b]=0

val = [
    (1,2),
    (1,3),
    (1,4),
    (2,4),
    (3,4),
    (3,5),
    (4,5),
]

for v in val:
    a,b = v
    graph[a][b]=1
    graph[b][a]=1

#거쳐갈 노드, 최종 목적지
x,k =4,5

for i in range(1, n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b]=min(graph[a][b], graph[a][i]+graph[i][b])

distance = graph[1][k]+graph[k][x]

if distance >= INF:
    print('-1')
else:
    print(distance)
