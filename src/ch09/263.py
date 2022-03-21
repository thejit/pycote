#전보
import heapq

INF=int(1e9)

#노드,간선,시작
n,m,start = 3,2,1
graph = [[] for i in range(n+1)]
distance = [INF]*(n+1)

val = [
    (1,2,4),
    (1,3,2),
]
for v in val:
    x,y,z=v
    graph[x].append((y,z))

def dijkstra(start):
    q=[]
    heapq.heappush(q, (0,start))
    distance[start]=0
    while q:
        dist,now=heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost=dist+i[1]
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q, (cost,i[0]))

dijkstra(start)

count=0
max_distance=0
for d in distance:
    if d!=INF:
        count+=1
        max_distance=max(max_distance,d)
print(count-1, max_distance)