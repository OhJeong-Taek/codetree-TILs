n, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
prefix_sum = [[0]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        prefix_sum[i][j] = prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1] + board[i-1][j-1]

ans = 0
for i in range(n-k+1): #n-k+1 , 3
    for j in range(n-k+1):
        ans = max(ans, prefix_sum[i+k][j+k] - prefix_sum[i+k][j] - prefix_sum[i][j+k] + prefix_sum[i][j])

print(ans)