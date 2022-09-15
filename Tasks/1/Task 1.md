# Task 1
```.py
def color(number):
    if number % 4 == 1:
        return "red"
    elif number % 4 == 2:
        return "white"
    elif number % 4 == 3:
        return "yellow"
    else:
        return "blue"
x = 1
while x < 2401:
    print(x, "is",color(x))
    x += 1
```
