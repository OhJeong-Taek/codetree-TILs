N, Q = map(int, input().split())
POS_LEN = 1000000
arr = [0] * (POS_LEN + 1)
prefix_sum = [0] * (POS_LEN + 1)

for val in list(map(int, input().split())):
    arr[val] = 1


for i in range(1, POS_LEN + 1):
    prefix_sum[i] = prefix_sum[i-1] + arr[i]

for _ in range(Q):
    s, e = map(int, input().split())
    print(prefix_sum[e] - prefix_sum[s-1 if s>=1 else 0])