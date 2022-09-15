# Task 3
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


def checker():
    color = input("Enter your locker color : ")
    errors = 0
    error_limit = 3
    while color.lower() != "red" and color.lower() != "white" and color.lower() != "yellow" and color.lower() != "blue":
        color = input(color + " is not a accepted color, try again : ")
        errors = errors + 1
        if errors == error_limit:
            print("You are a failure")
            exit("buy a brain")
    return color.lower()

def color(number):
    if number == "red":
        return 1
    elif number == "white":
        return 2
    elif number == "yellow":
        return 3
    else:
        return 4


color = color(checker())
print(color)
for i in range(1, 2400):
    if i % 4 == color:
        print(i)
```
