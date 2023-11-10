from collections import deque
import sys
input = sys.stdin.readline

#functions
def push(x,y):
    global count
    count += 1
    visited[x][y] = True
    q.append((x,y))

def in_range(x,y):
    return 0 <= x < n and 0 <= y < n

def can_go(x,y):
    return in_range(x,y) and not visited[x][y] and board[x][y] == 0

def bfs():
    dxs, dys = [1,0,-1,0], [0,1,0,-1]
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x+dx, y+dy
            if can_go(nx, ny):
                push(nx, ny)


#input
n, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]
q = deque()
count = 0

for _ in range(k):
    r, c = map(int, input().split())
    push(r-1, c-1)


bfs()
print(count)