#import charging_log.cvs
import csv
import time
import os


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
def get_sec(time_str):
    """Get seconds from time."""
    h, m, s = time_str.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)

# Define the path to the data file
data_file = "/Volumes/GoogleDrive/My Drive/UWC Isak Japan/Computer Science/unit-1/Lessons/Lesson-10/charging_log.cvs"

#import csv file
csv = csv.reader(open(data_file, "r"), delimiter=",")
#skip header
next(csv)

menu = """
1. Display all records
2. Av average time per kWh
3. Total kWh used
4. Total charge time
5. Exit
"""
print(menu)
choice = input("Enter your choice: ")
while True:
    if not choice.isdigit():
        print("Invalid choice")
        while not choice.isdigit():
            choice = input("Enter your choice: ")
    if choice == "1":
        print("Display all records")
        for row in csv:
            print(row)
    elif choice == "2":
        print("Average time per kWh")
        average = 0
        for row in csv:
            average += int(row[1])
    elif choice == "3":
        total = 0
        for row in csv:
            charge = row[1]
            charge_cleaned = charge.replace("kWh", "")
            total += float(charge_cleaned)
            msg = "Total kWh used: " + str(total)
            box(msg, "green")
        print("Total consumption is :",total)
    elif choice == "4":
        print("Total charge time")
        sum = 0
        for row in csv:
            sum += int(get_sec(row[2]))
        msg = ("You charged for " + time.strftime('%H:%M:%S', time.gmtime(sum)))
        box(msg, "red")
    elif choice == "5":
        exit("Goodbye")
    else:
        print("Not in menu")
    print(menu)
    choice = input("Enter your choice: ")







