n, k = map(int, input().split())
arr = []
for i in range(n):
    arr.append(int(input()))

ans = 0
for i in range(n-1, -1, -1):
    ans += k // arr[i]
    k = k % arr[i]

print(ans)