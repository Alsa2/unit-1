# Lesson 5
### QUIZZ-3
HL:
``` .py
# Quizz 3
InputProtein = str(input("Enter your proteins : "))
lenghtInput = len(InputProtein)
OutputProtein = ""
for i in range(lenghtInput):
    if InputProtein[i] == "A":
        OutputProtein += "T"
    elif InputProtein[i] == "T":
        OutputProtein += "A"
    elif InputProtein[i] == "G":
        OutputProtein += "C"
    elif InputProtein[i] == "C":
        OutputProtein += "G"
print(OutputProtein)
```

### Exercice 1
```.py
height1 = int(input())
height2 = int(input())
height3 = int(input())
if height1 > height2:
    #swapping the heights
    tmp = height1
    height1 = height2
    height2 = tmp
if height1 > height3:
    #swapping the heights
    tmp = height1
    height1 = height3
    height3 = tmp
if height2 > height3:
    #swapping the heights
    tmp = height3
    height3 = height2
    height2 = tmp
print(height3)
print(b)
print(height1)
```
### Exercice 2
```.py
#only accept numbers in the variable income
income = input("Enter your income: ")
while not income.isdigit():
    income = input("Enter your income (only digits): ")
income = int(income)
#if income is positive set the tax to 5%
if income > 0:
    tax = income * 0.05
#if income > 10000 set the tax to 10%
elif income > 10000:
    tax = income * 0.1
#if income > 50000 set the tax to 10%
elif income > 50000:
    tax = income * 0.15
#if income > 100000 set the tax to 25%
elif income > 100000:
    tax = income * 0.25
print("The IRS wants", tax, "dollars from you")
```
### Exercice 3
```.py

#defining a function that converts alphabetical numbers to numerical numbers
def convert_to_number(alphabetical_number):
    alphabetical_numbers = {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4,
        "e": 5,
        "f": 6,
        "g": 7,
        "h": 8,
        "i": 9,
        "j": 10,
        "k": 11,
        "l": 12,
        "m": 13,
        "n": 14,
        "o": 15,
        "p": 16,
        "q": 17,
        "r": 18,
        "s": 19,
        "t": 20,
        "u": 21,
        "v": 22,
        "w": 23,
        "x": 24,
        "y": 25,
        "z": 26
    }
    #return the value of the key in the dictionary
    return alphabetical_numbers[alphabetical_number]
input_string_1 = input("Enter the first string: ")
input_string_2 = input("Enter the second string: ")
input_string_3 = input("Enter the third string: ")
#define a variable that will hold the numerical value of the string
numerical_value_1 = []
numerical_value_2 = []
numerical_value_3 = []
#loop through the string and convert each letter to a numerical value
for letter in input_string_1:
    numerical_value_1.append(convert_to_number(letter))
for letter in input_string_2:
    numerical_value_2.append(convert_to_number(letter))
for letter in input_string_3:
    numerical_value_3.append(convert_to_number(letter))
# see what string is longer for the [i] in the loop
length_1 = len(numerical_value_1)
length_2 = len(numerical_value_2)
length_3 = len(numerical_value_3)
#see what is the greatest length
if length_1 > length_2 and length_1 > length_3:
    biggest_length = length_1
elif length_2 > length_1 and length_2 > length_3:
    biggest_length = length_2
else:
    biggest_length = length_3
#loop through the string and see who is the biggest
for i in range(biggest_length):
    if numerical_value_1[i] > numerical_value_2[i] and numerical_value_1[i] > numerical_value_3[i]:
        last = input_string_1
    elif numerical_value_2[i] > numerical_value_1[i] and numerical_value_2[i] > numerical_value_3[i]:
        last = input_string_2
    elif numerical_value_3[i] > numerical_value_1[i] and numerical_value_3[i] > numerical_value_2[i]:
        last = input_string_3
#loop through the string and see who is the smallest
for i in range(biggest_length):
    if numerical_value_1[i] < numerical_value_2[i] and numerical_value_1[i] < numerical_value_3[i]:
        first = input_string_1
    elif numerical_value_2[i] < numerical_value_1[i] and numerical_value_2[i] < numerical_value_3[i]:
        first = input_string_2
    elif numerical_value_3[i] < numerical_value_1[i] and numerical_value_3[i] < numerical_value_2[i]:
        first = input_string_3
#loop through the string and see who is in the middle (yes i know i could skip that and just process the last and first but i wanted to do it this way)
for i in range(biggest_length):
    if numerical_value_1[i] > numerical_value_2[i] and numerical_value_1[i] < numerical_value_3[i]:
        middle = input_string_1
    elif numerical_value_2[i] > numerical_value_1[i] and numerical_value_2[i] < numerical_value_3[i]:
        middle = input_string_2
    elif numerical_value_3[i] > numerical_value_1[i] and numerical_value_3[i] < numerical_value_2[i]:
        middle = input_string_3
#print the result
print(first, middle, last)

```
# Exercice 4
```.py
#the program will ask the user to enter the number of scores
while True:
    try:
        num = int(input("Enter the number of scores: "))
        break
    except ValueError:
        print("That's not a number!")
scores = []

#the program will ask the user to enter the scores
for i in range(num):
    while True:
        try:
            score = int(input("Enter a score: "))
            break
        except ValueError:
            print("That's not a number!")
    scores.append(score)
scores.sort()

#the program will calculate the median
if num % 2 == 0:
    median = (scores[num//2] + scores[num//2 - 1]) / 2
else:
    median = scores[num//2]

#the program will print the median
print("The median is", median)
```

