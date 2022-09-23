# Quizz 7
I liked this quizz
### v.1
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

### v.2

# Importing random
import random
``` .py
#Creating variables
passwords = []
invalid_caracters = [58, 59, 60, 61, 62, 63, 64, 91, 92, 93, 94, 95, 96, 123, 124, 125, 126]
password = ""
length = int(input("Enter the lenght of the password: "))
number_of_passwords = int(input("Enter the number of passwords: "))
symbols = input("Do you want to include special caracters? (True/False): ")

#main lo
while length > 0:
    for i in range(10):
        for i in range(length):
            if symbols == "True":
                temp = random.randint(33, 126)
                while temp in invalid_caracters:
                    temp = random.randint(33, 126)
                password += chr(temp)
            else:
                temp = random.randint(48, 126)
                while temp in invalid_caracters:
                    temp = random.randint(48, 126)
                password += chr(temp)
        passwords.append(password)
        password = ""

    # Print Output
    print("\n".join(passwords))
    length -=1
```

### Flowchart
![](../../Images/Quizz-7-Flowchart.png)

 **Fig. 1** My flow diagram
 
 ### Proof
 ![](../../Images/Quizz7-Proof.png)

 **Fig. 2** Proof
