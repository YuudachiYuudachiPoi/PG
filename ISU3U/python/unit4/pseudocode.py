x = 1
y = 1
sum = 0

while True:
    while True:
        sum = sum + y
        if y == x:
            break
        y = y + 1
    print(sum)
    if x == 10:
        break
    x = x + 1

