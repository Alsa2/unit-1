# Quizz 6
Given a string
``` .py
# Quizz 4
s = input()
#s = s.lower()
sum = 0
for i in s:
    if i.isupper():
        sum += ord(i) - 64
    elif i.islower():
        sum += ord(i) - 96
print(sum)
```
