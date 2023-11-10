import sys
from collections import deque
q = deque()

n, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]
r, c = map(int, input().split())
max_val = 0
min_r = min_c = sys.maxsize

def push(x, y, update_max_val = True):
    global max_val, min_r, min_c
    visited[x][y] = True
    q.append((x, y))

    if update_max_val:
        if board[x][y] > max_val:
            max_val = board[x][y]
            min_r, min_c = x, y
        elif board[x][y] == max_val:
            if min_r > x or (min_r == x and min_c > y):
                min_r, min_c = x, y
        
def visited_clear():
    for i in range(n):
        for j in range(n):
            visited[i][j] = False

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y, val):
    return in_range(x,y) and not visited[x][y] and board[x][y] < val

def bfs():
    dxs, dys = [1,0,-1,0], [0,1,0,-1]
    while q:
        x,y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x+dx, y+dy
            if can_go(nx, ny, board[x][y]):
                push(nx, ny)

def initialize():
    global max_val, min_r, min_c
    visited_clear()
    max_val = 0
    min_r = min_c = sys.maxsize

for _ in range(k):
    push(r-1, c-1, False)
    bfs()
    r, c = min_r, min_c
    initialize()

print(r+1, c+1)