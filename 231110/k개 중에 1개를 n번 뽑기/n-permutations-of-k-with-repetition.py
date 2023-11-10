from itertools import product

K, N = map(int, input().split())
for i in product(range(1,K+1), repeat=N):
    x, y = i
    print(x, y)