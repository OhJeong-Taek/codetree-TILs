from itertools import product

K, N = map(int, input().split())
for elem in product(range(1,K+1), repeat=N):
    for i in elem:
        print(i, end=" ")
    print()