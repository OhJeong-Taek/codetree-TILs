n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# - shape
answer = 0
for i in range(n):
    for j in range(m-2):
        answer = max(answer, grid[i][j] + grid[i][j+1] + grid[i][j+2])

# l shape
for j in range(m):
    for i in range(n-2):
        answer = max(answer, grid[i][j] + grid[i+1][j] + grid[i+2][j])

for i in range(n-1):
    for j in range(m-1):
        maxGrid = grid[i][j] + grid[i+1][j] + grid[i][j+1] + grid[i+1][j+1] - min(grid[i][j],grid[i+1][j],grid[i][j+1],grid[i+1][j+1])
        answer = max(answer, maxGrid)

print(answer)