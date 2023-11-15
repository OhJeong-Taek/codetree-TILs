n, k = map(int, input().split())
arr = list(map(int, input().split()))
arr = [0] + arr
prefix_sum = [0]*(n+1)
for i in range(1, n+1):
    prefix_sum[i] = prefix_sum[i-1] + arr[i]

ans = 0
for l in range(1, n+1):
    for s in range(1, n+2-l): 
        if prefix_sum[s+l-1]-prefix_sum[s-1] == k:
            ans += 1

print(ans)