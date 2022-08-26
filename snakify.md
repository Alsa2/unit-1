# Chapter 1

## Sum of three numbers

Write a program that takes three numbers and prints their sum. Every number is given on a separate line.

``` .py
a = int(input())
b = int(input())
c = int(input())
print(a + b + c)
```

## Hi John

Write a program that greets the person by printing the word "Hi" and the name of the person. See the examples below.

``` .py
a = str(input())
print("Hi", a)
```
## Square 

Write a program that takes a number and print its square. 

``` .py
a = int(input())
print(a*a)
```
## Area of right-angled triangle 

Write a program that reads the length of the base and the height of a right-angled triangle and prints the area. Every number is given on a separate line. 

``` .py
a = int(input())
b = int(input())
print(a*b/2)
```

## Hello, Harry!

Write a program that greets the user by printing the word "Hello", a comma, the name of the user and an exclamation mark after it. See the examples below. 

``` .py
print('Hello, ' + input() + '!')
```
## Apple sharing 

N students take K apples and distribute them among each other evenly. The remaining (the undivisible) part remains in the basket. How many apples will each single student get? How many apples will remain in the basket?

``` .py
n = int(input())
K = int(input())
print(K // n)
print(K % n)
```
## Previous and next

Write a program that reads an integer number and prints its previous and next numbers. See the examples below for the exact format your answers should take. There shouldn't be a space before the period. 

``` .js
a = parseInt(input());
b = (a-1);
c = (a+1)
print("The next number for the number " + a +" is "+ c + ".");
print("The previous number for the number " + a +" is "+ b + ".");
```
## Two timestamps

A timestamp is three numbers: a number of hours, minutes and seconds. Given two timestamps, calculate how many seconds is between them. The moment of the first timestamp occurred before the moment of the second timestamp. 

``` .py
hours_1 = int(input())
minutes_1 = int(input())
seconds_1 = int(input())
hours_2 = int(input())
minutes_2 = int(input())
seconds_2 = int(input())
print(hours_2 * 3600 + minutes_2 * 60 + seconds_2
    - hours_1 * 3600 - minutes_1 * 60 - seconds_1)
```
## School desks 

A school decided to replace the desks in three classrooms. Each desk sits two students. Given the number of students in each class, print the smallest possible number of desks that can be purchased. 

``` .py
a = int(input())
b = int(input())
c = int(input())
tot = 0
an = a % 2
if an == 0:
    totala =+ a/2

else:
    totala = a // 2 +1

bn = b % 2
if bn == 0:
    totalb = b/2

else:
    totalb = b // 2 +1

cn = c % 2
if cn == 0:
    totalc = c/2

else:
    totalc = c // 2 +1

print(int(totala + totalb + totalc))
```

# Chapter 2

## Last Digit

Given an integer number, print its last digit.

``` .py
a = int(input())
print(a%10)
```
## Tens digit

Given an integer. Print its tens digit. 

``` .py
n = int(input())
print(n // 10 % 10)
```

