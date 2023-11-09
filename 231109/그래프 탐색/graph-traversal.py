N, M = map(int, input().split())
grid = [[0]* (N+1) for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(M):
    x, y = map(int, input().split())
    grid[x][y] = 1
    grid[y][x] = 1

def dfs(x):
    if M == 0:
        return
    for cur in range(1, N+1):
        if grid[x][cur] and not visited[cur]:
            visited[cur] = True
            dfs(cur)

dfs(1)
print(max(sum(visited)-1, 0))