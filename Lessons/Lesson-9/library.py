#Funtions
def validate_input(promt:str):
    """This function asks the user for an input and validates the input is an integer"""
    red = "\033[1;31m"
    end_code = "\033[0m"
    while True:
        try:
            #ask in a normal color
            user_input = int(input(end_code + promt))
            return user_input
        except ValueError:
            print(f"{red}Please enter a valid number")


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

def ascii_art(letercolor,):
    """This function prints letters in ascii art"""
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
    if letercolor not in color_dict:
        print("Please enter a valid color")
        return
    #ascii art
    print(color_dict [letercolor])
    print("  _   _   _   _   _   _ ")
    print(" / \ / \ / \ / \ / \ / \ ")
    print("( C | O | M | S | C | I )")
    print(" \_/ \_/ \_/ \_/ \_/ \_/ ")
    print(end_code)
