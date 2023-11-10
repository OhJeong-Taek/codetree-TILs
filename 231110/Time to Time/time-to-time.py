a,b,c,d = map(int, input().split())

prev_min, aft_min = 60*a+b, 60*c+d
print(aft_min - prev_min)