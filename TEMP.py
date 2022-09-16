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

print(validate_input("Enter a number: "))
