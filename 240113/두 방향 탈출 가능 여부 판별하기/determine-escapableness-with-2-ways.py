n, m = tuple(map(int, input().split()))
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

def in_range(r, c):
    return 0<=r and r<n and 0<=c and c<m

def can_go(r, c):
    return in_range(r,c) and board[r][c] and not visited[r][c]

def dfs(r, c):
    drs, dcs = [1, 0], [0, 1]
    for dr, dc in zip(drs, dcs):
        nr, nc = r+dr, c+dc
        if can_go(nr, nc):
            visited[nr][nc] = 1
            dfs(nr, nc)

dfs(0, 0)
print(visited[n-1][m-1])