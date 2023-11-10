K, N = map(int, input().split())
answer = []

def print_numbers():
    for i in answer:
        print(i, end=' ')
    print()

def choose_number(cur_num):
    if cur_num == N:
        print_numbers()
        return

    for i in range(1, K+1):
        answer.append(i)
        choose_number(cur_num+1)
        answer.pop()

choose_number(0)