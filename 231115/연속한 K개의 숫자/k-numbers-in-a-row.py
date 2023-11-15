import sys

N, K, B = map(int, input().split())
arr = [0]*(N+1) #arr[0~ N]
prefix_sum = [0]*(N+1)

for _ in range(B):
    val = int(input())
    arr[val] = 1

for i in range(1, N+1):
    prefix_sum[i] = prefix_sum[i-1] + arr[i]

ans = sys.maxsize
for i in range(1, N-K+2): #10 6
    #ans = min(ans, sum(arr[i:i+K]))    #O(n) = (KN)
    ans = min(ans, prefix_sum[i+K-1] - prefix_sum[i-1]) # 속도 25배 가량 단축

print(ans)