import sys

N, K, B = map(int, input().split())
arr = [0]*(N+1)

for _ in range(B):
    val = int(input())
    arr[val] = 1

ans = sys.maxsize
for i in range(N-K+2): #10 6
    ans = min(ans, sum(arr[i:i+K]))    
#On = (KN)

print(ans)