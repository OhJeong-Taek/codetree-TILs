import sys
N, S = map(int, input().split())
arr = list(map(int, input().split()))

minVal = sys.maxsize
sumVal = 0

for elem in arr:
    sumVal += elem;

for i in range(N):
    for j in range(i+1, N):
        diff = abs(S-(sumVal-arr[i]-arr[j]))
        minVal = min(diff, minVal)

print(minVal)