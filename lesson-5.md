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
