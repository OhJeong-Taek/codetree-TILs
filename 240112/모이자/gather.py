import sys
n = int(input())
arr = list(map(int, input().split()))

ans = sys.maxsize
for i in range(n):
    dist = 0
    for j in range(n):
        dist += abs(i-j)*arr[j]
    ans = min(ans, dist)

print(ans)