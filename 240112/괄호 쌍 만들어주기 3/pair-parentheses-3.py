string = input()
n = len(string)
ans = 0

for i in range(n):
    for j in range(i+1, n):
        if string[i] == '(' and string[j] == ')':
            ans += 1

print(ans)