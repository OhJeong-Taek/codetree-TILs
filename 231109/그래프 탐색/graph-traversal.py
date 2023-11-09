N, M = map(int, input().split())
grid = [[0]*N for _ in range(N)]
visited = [False] * N

for _ in range(M):
    x, y = map(int, input().split())
    grid[x-1][y-1] = 1

def dfs(x):
    visited[x] = True
    for cur in range(N):
        if grid[x][cur] and not visited[cur]:
            dfs(cur)

dfs(1)
print(sum(visited))