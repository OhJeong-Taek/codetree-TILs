N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]

def in_range(x,y):
    return (0<=x and x<N and 0<=y and y<M)

def can_go(x,y,k):
    return in_range(x,y) and board[x][y] > k and not visited[x][y]

def dfs(x,y,k):
    dxs, dys = [1,0,-1,0], [0,1,0,-1]
    for dx, dy in zip(dxs, dys):
        nx, ny = x+dx, y+dy
        if can_go(nx, ny, k):
            visited[nx][ny] = True
            dfs(nx,ny,k)

def clear_visited():
    for i in range(N):
        for j in range(M):
            visited[i][j] = False

k_max = max(max(x) for x in board)
max_count = 0
ans_k = 0

for k in range(1, k_max):
    count = 0
    for i in range(N):
        for j in range(M):
            if can_go(i,j,k):
                visited[i][j] = True
                count+=1
                dfs(i,j,k)

    if count > max_count:
        max_count = count
        ans_k = k
    clear_visited()

print(max_count, ans_k)