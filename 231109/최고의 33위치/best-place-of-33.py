N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]

board_size = len(board)
answer = 0
for i in range(board_size):
    for j in range(board_size):
        val = 0
        if i+3 <= board_size and j+3 <= board_size:
            for k in range(i, i+3):
                for l in range(j, j+3):
                    val += board[k][l]
        answer = max(val, answer)
print(answer)