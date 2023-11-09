n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]

def in_range(x,y):
    return (0<=x and x<n and 0<=y and y<n)

def can_go(x,y):
    return in_range(x,y) and not visited[x][y] and board[x][y]

def dfs(x,y):
    global count
    dxs, dys = [0,1,0,-1], [1,0,-1,0]
    for dx, dy in zip(dxs, dys):
        nx, ny = x+dx, y+dy
        if can_go(nx,ny):
            visited[nx][ny] = True
            count += 1
            dfs(nx,ny)

answer = 0
count = 1
count_list = []
for i in range(n):
    for j in range(n):
        if board[i][j] and not visited[i][j]:
            visited[i][j] = True
            dfs(i,j)
            answer += 1
            count_list.append(count)
            count = 1

print(answer)
for elem in sorted(count_list):
    print(elem)