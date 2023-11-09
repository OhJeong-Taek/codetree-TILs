import sys
input = sys.stdin.readline

n, m = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

coins.reverse()

count = 0

for coin in coins:
    count += m//coin
    m %= coin

print(count)