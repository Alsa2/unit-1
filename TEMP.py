def blackbox(x, y):
    if abs(x-y) == 0:
        return int((x*y)-x)
    else:
        return int((x*y)-abs(x-y))

x = int(input())
y = int(input())
print(blackbox(x, y))