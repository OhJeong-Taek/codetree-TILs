import sys

n = int(input())
arr = list(map(int, input().split()))

minVal = sys.maxsize

for i in range(n):
    sumVal = 0
    for j in range(n):
        sumVal+=arr[j]*abs(j-i)
    
    minVal = min(sumVal, minVal)

print(minVal)