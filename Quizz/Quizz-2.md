# QUIZZ-2
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
#Crating a exit condition
tempA = False
#Creating a  temporal variable for checking if there is the leter C in the list
temA = 0
print("Enter the string and when you change number enter C")
while temA != "C":
    temA = input("Enter a number: ")
    if temA != "C":
        A.append(int(temA))
B = []
#Crating a exit condition
tempB = False
#Creating a  temporal variable for checking if there is the leter C in the list
temB = 0
print("Enter the string and when you change number enter C")
while temB != "C":
    temB = input("Enter a number: ")
    if temB != "C":
        B.append(temB)
#lenA means the length of A
lenA = len(A)
#lenB means the length of B
lenB = len(B)
#Creating a variable for the final output
finalstatement = False
for i in range(lenA):
    for j in range(lenB):
        if int(A[i]) == 20 or int(B[j]) == 20 or int(A[i]) + (B[j]) == 20:
            finalstatement = True
            break
    if finalstatement == True:
        break
print(finalstatement)
```