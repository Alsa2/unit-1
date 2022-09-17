# Task 3
[HL] Task 3: Create a program that receives a color from the user, validates the input,  and outputs the numbers of the lockers of the color provided. Use at least 10 different functions for Manipulating Strings (Learning Log Item 19)


```.py
def box(message, color):
    """This function prints a message in a box"""
    #colors
    red = "\033[1;31m"
    green = "\033[1;32m"
    yellow = "\033[1;33m"
    blue = "\033[1;34m"
    purple = "\033[1;35m"
    cyan = "\033[1;36m"
    white = "\033[1;37m"
    end_code = "\033[0m"
    #color dictionary
    color_dict = {"red": red, "green": green, "yellow": yellow, "blue": blue, "purple": purple, "cyan": cyan, "white": white}
    #color check
    if color not in color_dict:
        print("Please enter a valid color")
        return
    #check if message is too long
    if len(message) > 70:
        print("Message is too long")
        return
    #box
    print(color_dict [color])
    print("╔══════════════════════════════════════════════════════════════════════════════╗")
    print("║                                                                              ║")
    print("║" + message.upper().center(78, ' ') + "║")
    print("║                                                                              ║")
    print("╚══════════════════════════════════════════════════════════════════════════════╝")
    print(end_code)

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
        box(str(i), color(1))
```
