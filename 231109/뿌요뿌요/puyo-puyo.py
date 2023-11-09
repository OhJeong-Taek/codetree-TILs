import sys
sys.setrecursionlimit(10**4)

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]

def in_range(x,y):
    return (0<=x and x<n and 0<=y and y<n)

def can_go(x,y,val):
    return in_range(x,y) and not visited[x][y] and board[x][y] == val

def dfs(x,y,val):
    global count
    dxs, dys = [1,0,-1,0], [0,1,0,-1]
    for dx, dy in zip(dxs, dys):
        nx, ny = x+dx, y+dy
        if can_go(nx,ny,val):
            visited[nx][ny]=True
            count += 1
            dfs(nx,ny,val)

count = 1
max_count = 0
island = 0
for i in range(n):
    for j in range(n):
        count = 1
        if can_go(i,j,board[i][j]):
            visited[i][j] = True
            dfs(i,j,board[i][j])
            if count >= 4:
                island += 1 
            max_count = max(count, max_count)

print(island, max_count)