#다익스라 최단거리 - 개선
import heapq

INF = int(1e9)

#노드 갯수, 간선 갯수
n, m = 6, 11
#시작 노드
start = 1
graph = [[] for i in range(n+1)]
visited = [False] * (n+1)
distance = [INF] * (n+1)

val = [
    [1,2,2],
    [1,3,5],
    [1,4,1],
    [2,3,3],
    [2,4,2],
    [3,2,3],
    [3,6,5],
    [4,3,3],
    [4,5,1],
    [5,3,1],
    [5,6,2],
]

for v in val:
    graph[v[0]].append((v[1],v[2]))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            print(i)
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in range(1, n+1):
    if distance[1] == INF:
        print('INFINITY')
    else:
        print(distance[i])
