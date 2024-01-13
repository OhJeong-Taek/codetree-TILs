n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

def in_range(r, c):
    return 0<=r and r<n and 0<=c and c<n

def can_go(r, c, v):
    return in_range(r, c) and board[r][c] == v and not visited[r][c]

count = 0
def dfs(r, c, v):
    global count
    visited[r][c] = 1
    count += 1
    drs, dcs = [0, 1, 0, -1], [1, 0, -1, 0]
    for dr, dc in zip(drs, dcs):
        nr, nc = r + dr, c+dc
        if can_go(nr, nc, v):
            dfs(nr, nc, v)

max_val = 0
island_cnt = 0
for r in range(n):
    for c in range(n):
        if can_go(r, c, board[r][c]):
            dfs(r, c, board[r][c])
            if count >= 4:
                island_cnt += 1
            max_val = max(max_val, count)
            count = 0

print(island_cnt, max_val, end=' ')