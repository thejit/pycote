#플로이드 워셜
INF = int(1e9)

#노드 갯수, 간선 갯수
n, m = 4, 7
#시작 노드
start = 1
graph = [[INF] * (n+1) for _ in range(n+1)]
for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b:
            graph[a][b] = 0

val = [
    [1,2,4],
    [1,4,6],
    [2,1,3],
    [2,3,7],
    [3,1,5],
    [3,4,4],
    [4,3,2],
]

for v in val:
    graph[v[0]][v[1]] = v[2]

#점화식 따라 플로이드 워셜
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1,n+1):
            graph[a][b]=min(graph[a][b], graph[a][k]+graph[k][b])

print(graph)
for a in range(1,n+1):
    for b in range(1,n+1):
        if graph[a][b] == INF:
            print('INFINITY', end=' ')
        else:
            print(graph[a][b], end=' ')
    print(' ')
