# Quizz 9
### SL Program
Same as hl but enter 13 as shift
### Hl Program
```.py
#Create a function that receives as input a string and returns the string ciphered with shift 13.

#Example input
#hello word -> uryyb jbeyq
#Secret -> iushuj
#a -> n
shift = int(input('Enter shift: '))
def cipher(string):
    string = string.lower()
    new_string = ''
    for letter in string:
        if letter.isalpha():
            if ord(letter) + shift > 122:
                new_string += chr(ord(letter)+shift-26)
            else:
                new_string += chr(ord(letter)+shift)
        else:
            new_string += letter
    return new_string

print(cipher(input("Enter string: ")))
```
