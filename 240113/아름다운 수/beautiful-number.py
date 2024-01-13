N = int(input())
answer = 0
def choose(level):
    global answer
    if level > N:
        return
    if level == N:
        answer += 1
    
    for i in range(1,5):
        choose(level+i)
    return    

choose(0)
print(answer)