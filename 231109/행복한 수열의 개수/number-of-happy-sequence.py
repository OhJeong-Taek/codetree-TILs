n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]


answer = 0
#row
for i in range(n):
    consequtive = 0
    bef = board[i][0]
    for j in range(n):
        cur = board[i][j]
        if bef == cur:
            consequtive += 1
        else:
            consequtive = 1
        bef = cur
    if consequtive >= m:
        answer += 1

#column
for i in range(n):
    consequtive = 0
    bef = board[0][i]
    for j in range(n):
        cur = board[j][i]
        if bef == cur:
            consequtive += 1
        else:
            consequtive = 1
        bef = cur
    if consequtive >= m:
        answer += 1
print(answer)