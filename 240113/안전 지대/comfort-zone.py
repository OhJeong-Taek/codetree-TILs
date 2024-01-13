N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

max_val = 0
for i in range(N):
    for j in range(M):
        max_val = max(max_val, board[i][j])

def in_range(r, c):
    return 0<=r and r<N and 0<=c and c<M 

def can_go(r, c, k):
    return in_range(r, c) and not visited[r][c] and board[r][c] > k

def dfs(r, c, k):
    drs, dcs = [0,1,0,-1], [1,0,-1,0]
    visited[r][c] = 1
    for dr, dc in zip(drs, dcs):
        nr, nc = r+dr, c+dc
        if can_go(nr, nc, k):
            dfs(nr, nc, k)

def clear_visited():
    for i in range(N):
        for j in range(M):
            visited[i][j] = 0

max_comfort_zone = 0
max_k = 0
for k in range(1, max_val):
    comfort_zone = 0
    for r in range(N):
        for c in range(M):
            if can_go(r, c, k):
                comfort_zone += 1
                dfs(r,c,k)
    if comfort_zone > max_comfort_zone:
        max_k = k 
        max_comfort_zone = comfort_zone
    
    clear_visited()

print(max_k, max_comfort_zone, end=' ')