a, b, c = map(int, input().split())

prev = 11*60*24 + 11*60 + 11
aft = a*60*24 + b*60 + c

print(aft-prev if aft>=prev else -1)