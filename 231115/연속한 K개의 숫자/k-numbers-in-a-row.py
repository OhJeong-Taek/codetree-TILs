import sys

N, K, B = map(int, input().split())
arr = [0]*(N+1) #arr[0~ N]

for _ in range(B):
    val = int(input())
    arr[val] = 1

ans = sys.maxsize
for i in range(1, N-K+2): #10 6
    ans = min(ans, sum(arr[i:i+K]))    
#On = (KN)

print(ans)