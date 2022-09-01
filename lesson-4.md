# Lesson 4
### Snakify Homework
I am continuing to do my exercice, once i will finish the chapter I will upload them.

### QUIZZ-2
SL:
``` .py
# QUIZZ-2
A = int(input("Enter a number: "))
B = int(input("Enter another number: "))
if A == 20 or B == 20 or A + B == 20:
    print("TRUE")
else:
    print("FALSE")
```
HL:
``` .py
# QUIZZ-2
A = []
tempA = False
temA = 0
print("Enter the string and when you change number enter C")
while temA != "C":
    temA = input("Enter a number: ")
    if temA != "C":
        A.append(int(temA))
B = []
tempB = False
temB = 0
print("Enter the string and when you change number enter C")
while temB != "C":
    temB = input("Enter a number: ")
    if temB != "C":
        B.append(temB)
lenA = len(A)
lenB = len(B)
var = False
for i in range(lenA):
    for j in range(lenB):
        if int(A[i]) == 20 or int(B[j]) == 20 or int(A[i]) + (B[j]) == 20:
            var = True
            break
    if var == True:
        break
print(var)
```
