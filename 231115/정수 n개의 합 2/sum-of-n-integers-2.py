n, k = map(int, input().split())
arr = list(map(int, input().split()))
arr.insert(0,0)

prefix_sum = [0]*(n+1)
prefix_sum[0] = arr[0]

for i in range(1, n+1):
    prefix_sum[i] = prefix_sum[i-1] + arr[i]

answer = 0
for i in range(n+1):
    if i+k > n:
        continue
    answer = max(prefix_sum[i+k] - prefix_sum[i], answer)

print(answer)