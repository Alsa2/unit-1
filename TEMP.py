def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prWhite(skk): print("\033[97m {}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
def prBlue(skk): print("\033[94m {}\033[00m" .format(skk))

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
if color == "red":
    prRed("################################################################################")
    prRed(color.upper().center(80, '#'))
    prRed("################################################################################")
if color == "white":
    prWhite("################################################################################")
    prWhite(color.upper().center(80, '#'))
    prWhite("################################################################################")
if color == "yellow":
    prYellow("################################################################################")
    prYellow(color.upper().center(80, '#'))
    prYellow("################################################################################")
if color == "blue":
    prBlue("################################################################################")
    prBlue(color.upper().center(80, '#'))
    prBlue("################################################################################")