#다익스라 최단거리 - 간단
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

def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1,n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]

    for i in range(n-1):
        now  = get_smallest_node()
        visited[now] = True
        for j in graph[now]:
            cost = distance[now]+j[1]
            if cost < distance[j[0]]:
                distance[j[0]]=cost

dijkstra(start)

for i in range(1, n+1):
    if distance[1] == INF:
        print('INFINITY')
    else:
        print(distance[i])
