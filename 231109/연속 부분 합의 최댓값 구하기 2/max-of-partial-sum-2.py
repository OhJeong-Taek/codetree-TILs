n = int(input())
grid = list(map(int, input().split()))
candidates = [0]*n

maxVal = 0
for idx, elem in enumerate(grid):
    if maxVal < 0:
        maxVal = elem
    else:
        maxVal += elem
    candidates[idx] = maxVal

print(max(candidates))