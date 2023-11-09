n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
max_area = -1

for i in range(n):
    for j in range(m):
        if grid[i][j] > 0:
            for end_i in range(i,n):
                for end_j in range(j,m):
                    is_rectangle = True
                    for k in range(i, end_i+1):
                        for l in range(j, end_j+1):
                            if grid[k][l] <= 0:
                                is_rectangle = False
                                break
                        if not is_rectangle:
                            break
                    if is_rectangle:
                        max_area = max(max_area, (end_i-i+1)*(end_j-j+1))
                    else:
                        break

print(max_area)