# Lesson 8
### QUIZZ-6
In the quizz folder

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

# Task 2:
### v.1
```.py
number = int(input("Input a locker number : "))
if number % 4 == 1:
    color = "red"
elif number % 4 == 2:
    color = "white"
elif number % 4 == 3:
    color = "yellow"
else:
    color = "blue"
print("The color is", color)
```
### v.2
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


print("The color is", color(int(input("Input a locker number : "))))
```
### v.3
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
    number = input("Enter your locker number : ")
    errors = 0
    error_limit = 3
    while not number.isnumeric():
        number = input(number + " is not a number, try again: ")
        errors = errors + 1
        if errors == error_limit:
            print("You are a failure")
            exit("buy a brain")
    return int(number)
color = color(checker())
print("################################################################################")
print(color.upper().center(80, '#'))
print("################################################################################")
```
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
