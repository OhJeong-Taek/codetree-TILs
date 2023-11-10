from collections import deque

q = deque()
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]

def push(x, y):
    visited[x][y] = True
    q.append((x, y))

def in_range(x,y):
    return 0 <=x <n and 0 <= y < m

def can_go(x,y):
    return in_range(x,y) and not visited[x][y] and board[x][y] == 1

def bfs():
    while q:
        x, y = q.popleft()
        dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]
        for dx, dy in zip(dxs, dys):
            nx, ny = x+dx, y+dy
            if can_go(nx, ny):
                push(nx, ny)

push(0,0)
bfs()

print(1 if visited[n-1][m-1] else 0)