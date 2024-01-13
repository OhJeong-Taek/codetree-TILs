n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]

def in_range(r, c):
    return 0<=r and r<n and 0<=c and c<n

def can_go(r, c):
    return in_range(r,c) and board[r][c] and not visited[r][c]

def dfs(r, c):
    global count
    if visited[r][c] or not board[r][c]:
        return

    visited[r][c] = 1
    count += 1

    drs, dcs = [1,0,-1,0], [0,1,0,-1]
    for dr, dc in zip(drs, dcs):
        nr, nc = r+dr, c+dc
        if can_go(nr, nc):
            dfs(nr, nc)

arr = []
for i in range(n):
    for j in range(n):
        count = 0
        dfs(i, j)
        if count > 0:
            arr.append(count)

arr.sort()
print(len(arr))
for x in arr:
    print(x)