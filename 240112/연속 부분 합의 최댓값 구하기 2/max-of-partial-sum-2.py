import sys
n = int(input())
arr = list(map(int, input().split()))

ans = -sys.maxsize
cur_sum = 0
for elem in arr:
    cur_sum += elem
    ans = max(cur_sum, ans)
    if cur_sum < 0:
        cur_sum = 0
        

print(ans)