from collections import deque
q = deque()

n, m = tuple(map(int, input().split()))
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]

def push(x,y):
    visited[x][y] = 1
    q.append((x,y))

def bfs():
    dxs, dys = [0,1,0,-1], [1,0,-1,0]
    while q:
        x,y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x+dx, y+dy
            if can_go(nx, ny):
                push(nx, ny)

def in_range(x, y): 
    return 0<=x<n and 0<=y<n

def can_go(x,y):
    return in_range(x,y) and not visited[x][y] and not board[x][y]

for _ in range(m):
    x, y = map(int, input().split())
    x-=1 
    y-=1
    if can_go(x,y):
        push(x,y)
        bfs()
    
print(sum(visited[i][j] for i in range(n) for j in range(n)))