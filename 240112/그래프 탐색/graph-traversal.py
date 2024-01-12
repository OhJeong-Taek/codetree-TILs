N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]

for i in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

ans = 0

def DFS(v):
    global ans
    for cur_v in graph[v]:
        if not visited[cur_v]:
            visited[cur_v] = True
            ans += 1
            DFS(cur_v)
    
visited[1] = True
DFS(1)
print(ans)