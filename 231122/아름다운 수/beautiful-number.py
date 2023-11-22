n = int(input())
answer = 0

def Choose(curr_num):
    global answer
    if curr_num > n:
        return

    if curr_num == n:
        answer += 1
        return
    
    for i in range(1, 5):
        Choose(curr_num+i)
        
Choose(0)
print(answer)