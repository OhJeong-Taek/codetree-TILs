n = int(input())
count = 0

def beautiful(level):
    global count
    if level == n:
        count += 1
        return
    if level > n:
        return
    
    for i in range(1,5):
        beautiful(level+i)
        

beautiful(0)
print(count)