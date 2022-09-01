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
## Two digits

Given a two-digit number, print its digits separately.

``` .py
a = int(input())
print(a // 10, a % 10)
```
## Swap digits

Given a two-digit number, swap its digits as shown in the tests below.

``` .py
a = int(input())
print(str(a % 10) + str(a // 10))
```
## Last two digits

Given an integer number, print its last two digits. 

``` .py
a = int(input())
print(a%100)
```
## Tens digit

Given an integer. Print its tens digit. 

``` .py
n = int(input())
print(n // 10 % 10)
```
## Sum of digits

Given a three-digit number. Find the sum of its digits. 

``` .py
a = int(input())
print(int((a // 100) + (a % 100 - a % 10 )/ 10 + (a % 10)))
```
## Reverse three digits

Given a three-digit integer number, print its digits in a reversed order.

``` .py
a = int(input())
x1 = str(a % 10)
x2 = str(int((a % 100 - a % 10 )/ 10))
x3 = str(a // 100)
print(x1+x2+x3)
```
## Merge two numbers

Given two two-digit numbers, merge their digits as shown in the tests below. 

``` .py
a = int(input())
b = int(input())
print(str(a // 10)+str(b // 10)+str( a % 10)+str(b % 10))
```
## Cyclic rotation 

Given a four-digit integer number, perform its cyclic rotation by two digits, as shown in the tests below. 

``` .py
a = int(input())
print(str(a % 100)+str(a // 100))
```
## Fractional part 

Given a positive real number, print its fractional part.  

``` .py
a = float(input())
b = a % 1
print(b)
```
## First digit after decimal point 

Given a positive real number, print its first digit to the right of the decimal point.  

``` .py
a = float(input())
b = a % 1
b = b * 10
num_str = str(b)
first_digit = num_str[0]
print(first_digit)
```
## Car route

A car can cover distance of N kilometers per day. How many days will it take to cover a route of length M kilometers? The program gets two numbers: N and M. 

``` .py
M = int(input())
N = int(input())
if (N % M) == 0:
    print(N / M)
else:
    print(int((N / M) + 1))
```
## Day of week

Let's count the days of the week as follows: 0 - Sunday, 1 - Monday, 2 - Tuesday, ..., 6 - Saturday. Given an integer K in the range 1 to 365, find the number of the day of the week for the K-th day of the year provided that this year's January 1 is Thursday. 

``` .py
a = int(input())
print((a + 3) % 7)
```
## Digital clock

Given the integer N - the number of minutes that is passed since midnight - how many hours and minutes are displayed on the 24h digital clock? 

``` .py
s = int(input())
h = s // 60
m = s % 60
print(h,m)
```
## Total cost

A cupcake costs A dollars and B cents. Determine, how many dollars and cents should one pay for N cupcakes. A program gets three numbers: A, B, N. It should print two numbers: total cost in dollars and cents. 

``` .py
A = int(input())
B = int(input())
N = int(input())
T = ((A*100 + B)*N)
print((T // 100), ((T % 100)))
```
## Century 

Given a year as a positive integer, print its century. Mind that the 20th century began on 1901 and ended on 2000. 

``` .py
year = int(input())
print((year - 1) // 100 + 1)
```
## Snail 

A snail goes up A feet during the day and falls B feet at night. How long does it take him to go up H feet? 

``` .py
H = int(input())
A = int(input())
B = int(input())
x = 0
cre = (A-B)
while cre*x < H:
    x = x + 1
    print(x*cre)
print(x)
```
## Clock face - 1

H hours, M minutes and S seconds are passed since the midnight (0 ≤ H < 12, 0 ≤ M < 60, 0 ≤ S < 60). Determine the angle (in degrees) of the hour hand on the clock face right now. 

``` .py
H = int(input())
M = int(input())
S = int(input())
A = H / 12 * 360
A = A + (360 / 12 / 60 * M)
A = A + (360 / 12 / 60 / 60 * S)
print(A)
```
## Clock face - 2 

Hour hand turned by α degrees since the midnight. Determine the angle by which minute hand turned since the start of the current hour. Input and output in this problems are floating-point numbers. 

``` .py
a = float(input())
a = (a % (360 / 12))
print(a / 60 * 360 * 2)s
```
# Lesson 3

## Is positive 

Given an integer, print "YES" if it's positive and print "NO" otherwise. 

``` .py
a = int(input())
if a > -1:
    print("YES")
else:
    print("NO")
```

## Is odd

Given an integer, print "YES" if it's odd and print "NO" otherwise. 

``` .py
a = int(input())
if a % 2 == 0:
    print("NO")
else:
    print("YES")
```

## Is even 

Given an integer, print "YES" if it's even and print "NO" otherwise. 

``` .py
a = int(input())
if a % 2 == 0:
    print("YES")
else:
    print("NO")
```
## Ends on seven

Given an integer, print "YES" if it's last digit is 7 and print "NO" otherwise.

``` .py
a = str(input())
len = len(a)
a = (a[len-1])
if int(a) == 7:
    print("YES")
else:
    print("NO")
```
## Minimum of two numbers

Given two integers, print the smaller value. 

``` .py
a = int(input())
b = int(input())
if a > b:
    print(b)
else:
    print(a)
```
## Are both odd

Given two integers, print "YES" if they're both odd and print "NO" otherwise.

``` .py
a = int(input())
b = int(input())
if not a % 2 == 0 and not b % 2 == 0:
    print("YES")
else:
    print("NO")
```
## At least one odd 

Given two integers, print "YES" if at least one of them is odd and print "NO" otherwise. 

``` .py
a = int(input())
b = int(input())
if not a % 2 == 0 or not b % 2 == 0:
    print("YES")
else:
    print("NO")
```
## Exactly one odd 

Given two integers, print "YES" if exactly one of them is odd and print "NO" otherwise. 

``` .py
a = int(input())
b = int(input())
if (not a % 2 == 0 and b % 2 == 0) or ( a % 2 == 0 and not b % 2 == 0):
    print("YES")
else:
    print("NO")
```
## Sign function

For the given integer X print 1 if it's positive, -1 if it's negative, or 0 if it's equal to zero. 

``` .py
a = int(input())
if a == 0:
    print(0)
if a > 0:
    print(1)
if a < 0:
    print(-1)
```
## Numbers in ascending order

Given three different integers, print YES if they're given in ascending order, print NO otherwise. 

``` .py
a = int(input())
b = int(input())
c = int(input())
if a < b < c:
    print("YES")
else:
    print("NO")
```
## Is three digit 

Given an integer, print "YES" if it's a three-digit number and print "NO" otherwise. 

``` .py
a = str(input())
a = len(a)
if int(a) == 3:
    print("YES")
else:
    print("NO")
```
## Minimum of three numbers 

 Given three integers, print the smallest value. 

``` .py
a = int(input())
b = int(input())
c = int(input())
if a > b:
    if c > b:
        print(b)
if b > a:
    if c > a:
        print(a)
if a > c:
    if b > c:
        print(c)
```
## Equal numbers

 Given three integers, determine how many of them are equal to each other. The program must print one of these numbers: 3 (if all are the same), 2 (if two of them are equal to each other and the third is different) or 0 (if all numbers are different). 

``` .py
a = int(input())
b = int(input())
c = int(input())
if a == b == c:
    print(3)
elif a == b or b == c or c == a and not a == b == c:
    print(2)
else:
    print(0)
```
## Rook move 

Chess rook moves horizontally or vertically. Given two different cells of the chessboard, determine whether a rook can go from the first cell to the second in one move.

The program receives the input of four numbers from 1 to 8, each specifying the column and row number, first two - for the first cell, and then the last two - for the second cell. The program should output YES if a rook can go from the first cell to the second in one move, or NO otherwise. 

``` .py
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if x1 == x2 or y1 == y2:
    print("YES")
else:
    print("NO")
```
## Chess board - black square 

Given a square of a chessboard. Print BLACK if it's black and print WHITE otherwise. 

``` .py
a = int(input())
b = int(input())
if (a+b) % 2 == 0:
    print("BLACK")
else:
    print("WHITE")
```
## Chess board - same color 

Given two cells of a chessboard. If they are painted in one color, print the word YES, and if in a different color - NO. 

``` .py
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if (x1 + y1 + x2 + y2) % 2 == 0:
    print('YES')
else:
    print('NO')
```
## Distance to closest point 

 Given the coordinates of the three points A, B, and C on a line. Print a distance from the point A to closest point to it. 

``` .py
A = int(input())
B = int(input())
C = int(input())
if abs(A - B) < abs(A - C):
    print(abs(A - B))
else:
    print(abs(A - C))
```
## TEMPLAT_TITLE

TEMPLATE_STATEMENT

``` .py
TEMPLATE_SCRIPT
```