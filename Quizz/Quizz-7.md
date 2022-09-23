# Quizz 7
I liked this quizz
``` .py
import random
lenght = int(input("Enter the lenght of the password: "))
numberofpasswords = int(input("Enter the number of passwords: "))
special = input("Do you want to include special caracters? (True/False): ")
if special == "True":
    password = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+"
else:
    password = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
for i in range(numberofpasswords):
    print()
    for i in range(lenght):
        print(random.choice(password), end = "")
```
