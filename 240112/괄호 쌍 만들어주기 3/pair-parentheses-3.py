arr = list(input())
n = len(arr)

ans = 0
for i in range(n):
    if arr[i] == '(':
        for j in range(i+1, n):
            if arr[j] == ')':
                ans += 1

print(ans)