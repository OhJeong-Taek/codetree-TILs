n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
seq = [0 for _ in range(n)]

def is_happy_sequence():
    consequtive, max_ccnt = 1, 1
    for i in range(1,n):
        if seq[i-1] == seq[i]:
            consequtive += 1
        else:
            consequtive = 1
        max_ccnt = max(max_ccnt, consequtive)
    return max_ccnt >= m

answer = 0
#row
for i in range(n):
    seq = grid[i][:]
    if is_happy_sequence():
        answer += 1

#column
for i in range(n):
    for j in range(n):
        seq[i] = grid[j][i]
    if is_happy_sequence():
        answer += 1
print(answer)