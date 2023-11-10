m1, d1, m2, d2 = map(int, input().split())
day_str = input()

days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days_str = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

day_index = days_str.index(day_str)

days1, days2 = sum(days[:m1-1])+d1, sum(days[:m2-1])+d2
diff = days2-days1


print(diff//7 + (1 if diff%7 >= day_index else 0))