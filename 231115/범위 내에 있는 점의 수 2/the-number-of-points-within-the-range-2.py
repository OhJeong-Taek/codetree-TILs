N, Q = map(int, input().split())
POS_LEN = 1000000 + 1
arr = [0] * (POS_LEN)
prefix_sum = [0] * (POS_LEN)

for val in list(map(int, input().split())):
    arr[val] = 1


for i in range(1,POS_LEN):
    prefix_sum[i] = prefix_sum[i-1] + arr[i]

for _ in range(Q):
    s, e = map(int, input().split())
    print(prefix_sum[e] - prefix_sum[s-1])