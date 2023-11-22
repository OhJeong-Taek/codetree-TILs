K, N = map(int, input().split())
answer = []

def print_answer():
    for elem in answer:
        print(elem, end=' ')
    print()

def Choose(curr_num):
    if curr_num == N:
        print_answer()
        return

    for i in range(1, K+1):
        answer.append(i)
        Choose(curr_num + 1)
        answer.pop()


Choose(0)