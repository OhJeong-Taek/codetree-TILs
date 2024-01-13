K, N = tuple(map(int, input().split()))

answer = []
def choose(level):
    if level == N:
        print_answer()
        return
    
    for i in range(1, K+1):
        answer.append(i)
        choose(level+1)
        answer.pop()

    return

def print_answer():
    for x in answer:
        print(x, end=' ')
    print()

choose(0)