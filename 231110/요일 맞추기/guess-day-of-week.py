m1, d1, m2, d2 = map(int, input().split())

days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day_str = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

day1, day2 = sum(days[:m1-1])+d1, sum(days[:m2-1])+d2

print(day_str[(day2-day1)%7])