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
## Digits in ascending order 

Given a three-digit integer, print YES if its digits go in ascending order, print NO otherwise. 

``` .py
x = str(input())
a = x[0]
b = x[1]
c = x[2]
if a < b < c:
    print("YES")
else:
    print("NO")
```
## Four-digit palindrome 

 A palindrome is a number which reads the same when read forward as it it does when read backward. Given a four-digit integer, print "YES" if it's a palindrome and print "NO" otherwise. 

``` .py
x = str(input())
a = x[0]
b = x[1]
c = x[2]
d = x[3]
if a + b == d + c:
    print("YES")
else:
    print("NO")
```
## King move 

Chess king moves horizontally, vertically or diagonally to any adjacent cell. Given two different cells of the chessboard, determine whether a king can go from the first cell to the second in one move.

The program receives the input of four numbers from 1 to 8, each specifying the column and row number, first two - for the first cell, and then the last two - for the second cell. The program should output YES if a king can go from the first cell to the second in one move, or NO otherwise.


``` .py
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
s1 = abs(x1 - x2)
s2 = abs(y1 - y2)
if s1 <= 1 and s2 <= 1:
    print('YES')
else:
    print('NO')
```
## Bishop moves

In chess, the bishop moves diagonally, any number of squares. Given two different squares of the chessboard, determine whether a bishop can go from the first to the second in one move.

The program receives as input four numbers from 1 to 8, specifying the column and row numbers of the starting square and the column and row numbers of the ending square. The program should output YES if a Bishop can go from the first square to the second in one move, or NO otherwise. 

``` .py
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if abs(x1 - x2) == abs(y1 - y2):
    print('YES')
else:
    print('NO')
```
## Queen move 

Chess queen moves horizontally, vertically or diagonally to any number of cells. Given two different cells of the chessboard, determine whether a queen can go from the first cell to the second in one move.

The program receives the input of four numbers from 1 to 8, each specifying the column and row number, first two - for the first cell, and then the last two - for the second cell. The program should output YES if a queen can go from the first cell to the second in one move, or NO otherwise. 

``` .py
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if abs(x1 - x2) == abs(y1 - y2) or x1 == x2 or y1 == y2:
    print('YES')
else:
    print('NO')
```
## Index of outlier 

 Given three integers: two are equal to each other and the third one is different. Print the index number of this different one - 1, 2 or 3. 

``` .py
a = int(input())
b = int(input())
c = int(input())
if a != b and a != c:
    print("1")
elif b != c and b != a:
    print("2")
else:
    print("3")
```
## Knight move 

Chess knight moves like the letter L. It can move two cells horizontally and one cell vertically, or two cells vertically and one cells horizontally. Given two different cells of the chessboard, determine whether a knight can go from the first cell to the second in one move.

The program receives the input of four numbers from 1 to 8, each specifying the column and row number, first two - for the first cell, and then the last two - for the second cell. The program should output YES if a knight can go from the first cell to the second in one move, or NO otherwise. 

``` .py
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if abs(x1 - x2) == 1 and abs(y1 - y2) == 2 or abs(x1 - x2) == 2 and abs(y1 - y2) == 1:
    print('YES')
else:
    print('NO')
```
## Chocolate bar 

Chocolate bar has the form of a rectangle divided into n×m portions. Chocolate bar can be split into two rectangular parts by breaking it along a selected straight line on its pattern. Determine whether it is possible to split it so that one of the parts will have exactly k squares.

The program reads three integers: n, m, and k. It should print YES or NO. 

``` .py
n = int(input())
m = int(input())
k = int(input())
if ((k % n == 0) or (k % m == 0)) and k < n * m:
    print('YES')
else:
    print('NO')
```
## Leap year 

Given the year number. You need to check if this year is a leap year. If it is, print LEAP, otherwise print COMMON.

The rules in Gregorian calendar are as follows:

-a year is a leap year if its number is exactly divisible by 4 and is not exactly divisible by 100
-a year is always a leap year if its number is exactly divisible by 400 

``` .py
a = int(input())
if (a % 4 == 0) and not (a % 100 == 0) or (a % 400 == 0):
    print("LEAP")
else:
    print("COMMON")
```
## Days in month 

 Given a month - an integer from 1 (January) to 12 (December), print the number of days in it in the year 2017 (or any other non-leap year). 

``` .py
a = int(input())
if a == 1 or a == 3 or a == 5 or a == 7 or a == 8 or a == 10 or a == 12:
    print("31")
elif a == 2:
    print("28")
else:
    print("30")
```
## Next day 

 Given the month (an integer from 1 to 12) and the day in it (an integer from 1 to 31) in the year 2017 (or in any other common year), print the month and the day of the next day to it. The first test corresponds to March 30 and March 31. The second test corresponds to March 31 and April 1. 

``` .py
a = int(input())
b = int(input())
if a == 1 or a == 3 or a == 5 or a == 7 or a == 8 or a == 10 or a == 12:
    day = 31
elif a == 2:
    day = 28
else:
    day = 30
if day == 31:
    if a == 12 and b == 31:
        print("1")
        print("1")
    elif b == 31:
        print(a + 1)
        print(1)
    else:
        print(a)
        print(b + 1)
if day == 30:
    if b == 30:
        print(a + 1)
        print(1)
    else:
        print(a)
        print(b + 1)
if day == 28:
    if b == 28:
        print(a + 1)
        print(1)
    else:
        print(a)
        print(b + 1)
```
## Linear equation 

 Write a program that solves a linear equation ax = b in integers. Given two integers a and b (a may be zero), print a single integer root if it exists and print "no solution" or "many solutions" otherwise. 

``` .py
a = int(input())
b = int(input())
if a == 0 and b == 0:
    print('many solutions')
elif a == 0 and b != 0 or b % a != 0:
    print('no solution')
else:
    print(b // a)
```
## Vertices of rectangle 

Given integer coordinates of three vertices of a rectangle whose sides are parallel to the coordinate axes, find the coordinates of the fourth vertex of the rectangle. In the first test the three given vertices are (1, 4), (1, 6), (7, 4). The fourth vertex is thus (7, 6). 

``` .py
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x3 = int(input())
y3 = int(input())
if x1 == x2:
    x4 = x3
elif x1 == x3:
    x4 = x2
else:
  x4 = x1
if y1 == y2:
    y4 = y3
elif y1 == y3:
    y4 = y2
else:
    y4 = y1
print(x4)
print(y4)
```
## Sort three numbers 

Given three integers, print them in ascending order. 


``` .py
a = int(input())
b = int(input())
c = int(input())

if a > b:
    a, b = b, a
if a > c:
    a, c = c, a
if b > c:
    b, c = c, b

print(a)
print(b)
print(c)
```
## White pawn move 

A white chess pawn moves up vertically one square at a time. An exception is a pawn on a row #2: it can move either one or two squares up. In addition, a white chess pawn captures diagonally up one square to the left or right. A white chess pawn can never occur on a row #1.

The program receives the input of four numbers from 1 to 8, each specifying the column and row number, first two - for the first square, and then the last two - for the second square. The program should print YES if a white pawn can possibly move from the first square to the second square in one move in some game - either by move or by capture. The program should print NO otherwise. The first four tests correspond to the green arrows on the picture below. 

``` .py
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if abs(x1 - x2) < 2 and y1 > 1 and y1 < y2:
    if y2 - y1 < 2:
        print("YES")
    elif y1 == 2 and y2 - y1 < 3 and x1 == x2:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
```
# Chapter 4
## Count to N 

 Given an integer N, print all the numbers from 1 to N. 

``` .py
n = int(input())
x = 1
while n >= x:
    print(x)
    x = x + 1
```
## Series - 1 

 Given two integers A and B (A ≤ B). Print all numbers from A to B inclusively. 

``` .py
x = int(input())
n = int(input())
while n >= x:
    print(x)
    x = x + 1

```
## First N odd, ascending 

 Given an integer N, print all the odd numbers from 1 to N in ascending order. 

``` .py
n = int(input())
x = 1
while n >= x:
    if x % 2 == 1:
        print(x)
    x = x + 1
```
## Series - 2 

 Given two integers A and B. Print all numbers from A to B inclusively, in ascending order, if A < B, or in descending order, if A ≥ B. 

``` .py
n1 = int(input())
n2 = int(input())
if n1 < n2:
    while n2 >= n1:
        print(n1)
        n1 = n1 + 1
else:
    while n1 >= n2:
        print(n1)
        n1 = n1 -1

```
## First N even, descending 

 Given an integer N, print all the even numbers from 0 to N in descending order. 

``` .py
n = int(input())
for i in range(n, -1, -1):
    if i % 2 == 0:
        print(i)
```
## Sum of ten numbers 

 10 numbers are given in the input. Read them and print their sum. Use as few variables as you can. 

``` .py
while True:
    try:
        print(sum([int(input()) for i in range(10)]))
        break
    except:
        print('Please enter a valid number')

```
## Sum of N numbers 

N numbers are given in the input. Read them and print their sum.

The first line of input contains the integer N, which is the number of integers to follow. Each of the next N lines contains one integer. Print the sum of these N integers. 

``` .py
n = int(input())
sum = 0
for i in range(n):
            sum += int(input())
print(sum)

```
## Product of N numbers 

N numbers are given in the input. Read them and print their product.

The first line of input contains a positive integer N: the number of integers to follow. Each of the next N lines contains one integer. Print the product of these N integers. 

``` .py
n = int(input())
product = 1
for i in range(n):
    product *= int(input())
print(product)
```
## Sum of cubes 

For the given integer N calculate the following sum:
1**3+2**3+…+N**3

``` .py
n = int(input())
sum = 0
for i in range(1, n+1):
    sum += i**3
print(sum)
```
## Factorial 

In mathematics, the factorial of an integer n, denoted by n! is the following product:
n!=1×2×…×n

``` .py
n = int(input())
factorial = 1
for i in range(1,n + 1):
    factorial = factorial*i
print(factorial)
```
## The number of zeros 

Given N numbers: the first number in the input is N, after that N integers are given. Count the number of zeros among the given integers and print it.

You need to count the number of numbers that are equal to zero, not the number of zero digits. 

``` .py
n = int(input())
count = 0
for i in range(n):
    if int(input()) == 0:
        count += 1
print(count)
```
## Adding factorials 

Given an integer n, print the sum 1!+2!+3!+...+n!.

This problem has a solution with only one loop, so try to discover it. And don't use the math library :) 

``` .py
n = int(input())
sum = 0
for i in range(1, n+1):
    factorial = 1
    for j in range(1, i+1):
        factorial *= j
    sum += factorial
print(sum)
```
## Squares in range 

Given two integers A and B, print squares of all integer numbers between them, as shown below. There shouldn't be any spaces around * and =. The sep argument of the function print() may help you with that. 

``` .py
A = int(input())
B = int(input())
for i in range(A, B+1):
    print(i, '*', i, '=', i**2, sep='')
```
## Ladder 

For given integer n ≤ 9 print a ladder of n steps. The k-th step consists of the integers from 1 to k without spaces between them.

To do that, you can use the sep and end arguments for the function print(). 

``` .py
n = int(input())
for i in range(1, n+1):
    print(*range(1, i+1), sep='', end="""
""")
```
## Is prime 

A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. Given an integer N > 1, print PRIME if it's prime and print COMPOSITE otherwise. 

``` .py
A = int(input())
if A > 1:
    for i in range(2, A):
        if (A % i) == 0:
            print("COMPOSITE")
            break
    else:
        print("PRIME")
```
## Print primes in range 

A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. Given two integers A and B, print all prime numbers between them, inclusively. 

``` .py
A = int(input())
B = int(input())
for i in range(A, B+1):
    if i > 1:
        for j in range(2, i):
            if (i % j) == 0:
                break
        else:
            print(i)
```
## Number of primes in range 

 A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. Given two integers A and B, print the number of primes between them, inclusively. 

``` .py
A = int(input())
B = int(input())
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
count = 0
for i in range(A, B+1):
    if isPrime(i):
        count += 1
print(count)
```
## Lost card 

There was a set of cards with numbers from 1 to N. One of the card is now lost. Determine the number on that lost card given the numbers for the remaining cards.

Given a number N, followed by N − 1 integers - representing the numbers on the remaining cards (distinct integers in the range from 1 to N). Find and print the number on the lost card. 

``` .py
n = int(input())
sum = 0
for i in range(n-1):
    sum += int(input())
print(int(n*(n+1)/2 - sum))
```
#Chapter 5

## Slices 

You are given a string.

In the first line, print the third character of this string.

In the second line, print the second to last character of this string.

In the third line, print the first five characters of this string.

In the fourth line, print all but the last two characters of this string.

In the fifth line, print all the characters of this string with even indices (remember indexing starts at 0, so the characters are displayed starting with the first).

In the sixth line, print all the characters of this string with odd indices (i.e. starting with the second character in the string).

In the seventh line, print all the characters of the string in reverse order.

In the eighth line, print every second character of the string in reverse order, starting from the last one.

In the ninth line, print the length of the given string. 

``` .py
s = input()
print(s[2])
print(s[-2])
print(s[:5])
print(s[:-2])
print(s[::2])
print(s[1::2])
print(s[::-1])
print(s[::-2])
print(len(s))
```
## The number of words 

 Given a string consisting of words separated by spaces. Determine how many words it has. To solve the problem, use the method count. 

``` .py
a= input()
print(a.count(' ')+1)
```
## The two halves 

Given a string. Cut it into two "equal" parts (If the length of the string is odd, place the center character in the first string, so that the first string contains one more characther than the second). Now print a new string on a single row with the first and second halfs interchanged (second half first and the first half second)

Don't use the statement if in this task. 

``` .py
s = input()
print(s[(len(s) + 1) // 2:] + s[:(len(s) + 1) // 2])
```
## To swap the two words 

Given a string consisting of exactly two words separated by a space. Print a new string with the first and second word positions swapped (the second word is printed first).

This task should not use loops and if. 

``` .py
s = input()
print(s[s.find(' ')+1:] + ' ' + s[:s.find(' ')])
```
## The first and last occurrence 

Given a string that may or may not contain a letter of interest. Print the index location of the first and last appearance of f. If the letter f occurs only once, then output its index. If the letter f does not occur, then do not print anything.

Don't use loops in this task. 

``` .py
s = input()
if s.count('f') == 1:
    print(s.find('f'))
elif s.count('f') > 1:
    print(s.find('f'), s.rfind('f'))
```
## The second occurrence 

 Given a string that may or may not contain the letter of interest. Print the index location of the second occurrence of the letter f. If the string contains the letter f only once, then print -1, and if the string does not contain the letter f, then print -2. 

``` .py
s = input()
if s.count('f') == 1:
    print(-1)
elif s.count('f') == 0:
    print(-2)
else:
    print(s.find('f', s.find('f') + 1))
```
## Remove the fragment 

 Given a string in which the letter h occurs at least twice. Remove from that string the first and the last occurrence of the letter h, as well as all the characters between them. 

``` .py
s = str(input())
print(s[:(s.find('h'))]+s[(s.rfind('h')+1):])
```
## Reverse the fragment 

 Given a string in which the letter h occurs at least two times, reverse the sequence of characters enclosed between the first and last appearances. 

``` .py
s = input()
i = s.find('h')
j = s.rfind('h')
print(s[:i] + s[i:j+1][::-1] + s[j+1:])
```
## Replace the substring 

 Given a string. Replace in this string all the numbers 1 by the word one. 

``` .py
s = input()
print(s.replace('1', 'one'))
```
## Delete a character 

 Given a string. Remove from this string all the characters @. 

``` .py
s = input()
print(s.replace('@', ''))
```
## Replace within the fragment 

 Given a string. Replace every occurrence of the letter h by the letter H, except for the first and the last ones. 

``` .py
s = input()
a = s[:s.find('h') + 1] 
b = s[s.find('h') + 1:s.rfind('h')]
c = s[s.rfind('h'):]
s = a + b.replace('h', 'H') + c
print(s)
```
## Delete every third character 

 Given a string. Delete from it all the characters whose indices are divisible by 3. 

``` .py
s = input()
t = ''
for i in range(len(s)):
    if i % 3 != 0:
        t = t + s[i]
print(t)
```
# Chapter 6
## List of squares 

 For a given integer N, print all the squares of integer numbers where the square is less than or equal to N, in ascending order. 

``` .py
N = int(input())
i = 1
while i ** 2 <= N:
    print(i ** 2)
    i += 1
```
## Least divisor 

 Given an integer not less than 2. Print its smallest integer divisor greater than 1. 

``` .py
N = int(input())
i = 2
while i <= N:
    if N % i == 0:
        print(i)
        break
    i += 1
```
## The power of two 

For a given integer N, find the greatest integer x where 2x is less than or equal to N. Print the exponent value and the result of the expression 2x.

Don't use the operation **.

``` .py
n = int(input())
two = 2
x = 1
while two <= n:
    two *= 2
    x += 1
print(x - 1, two // 2)
```
## Morning jog 

As a future athlete you just started your practice for an upcoming event. Given that on the first day you run x miles, and by the event you must be able to run y miles.

Calculate the number of days required for you to finally reach the required distance for the event, if you increases your distance each day by 10% from the previous day.

Print one integer representing the number of days to reach the required distance. 

``` .py
x = int(input())
y = int(input())
d = 1
while x < y:
    x = x * 1.1
    d = d + 1
print(d)
```
## The length of the sequence 

 Given a sequence of non-negative integers, where each number is written in a separate line. Determine the length of the sequence, where the sequence ends when the integer is equal to 0. Print the length of the sequence (not counting the integer 0). The numbers following the number 0 should be omitted. 

``` .py
x = int(input())
count = 0
while x != 0:
    x = int(input())
    count += 1
print(count)
```
## The sum of the sequence 

 Determine the sum of all elements in the sequence, ending with the number 0. 

``` .py
x = int(input())
sum = 0
while x != 0:
    sum += x
    x = int(input())
print(sum)
```
## The average of the sequence 

 Determine the average of all elements of the sequence ending with the number 0. 

``` .py
x = int(input())
sum = 0
count = 0
while x != 0:
    sum = sum + x
    count = count + 1
    x = int(input())
print(sum / count)
```
## The maximum of the sequence 

 A sequence consists of integer numbers and ends with the number 0. Determine the largest element of the sequence. 

``` .py
s = int(input())
max = s
while s != 0:
    s = int(input())
    if s > max:
        max = s
print(max)
```
## The index of the maximum of a sequence 

 A sequence consists of integer numbers and ends with the number 0. Determine the index of the largest element of the sequence. If the highest element is not unique, print the index of the first of them. 

``` .py
s = int(input())
i = 0
max = 0
while s != 0:
    i += 1
    if s > max:
        max = s
        index = i
    s = int(input())
print(index)
```
## The number of even elements of the sequence

 Determine the number of even elements in the sequence ending with the number 0. 

``` .py
s = int(input())
count = 0
while s != 0:
    if s % 2 == 0:
        count += 1
    s = int(input())
print(count)
```
![](Images/Snakify/6.10.jpg)

## The number of elements that are greater than the previous one 

 A sequence consists of integer numbers and ends with the number 0. Determine how many elements of this sequence are greater than their neighbours above. 

``` .py
s = int(input())
count = 0
while s != 0:
    s1 = int(input())
    if s1 > s:
        count += 1
    s = s1
print(count)
```
![](Images/Snakify/6.11.jpg)

## The second maximum 

 The sequence consists of distinct positive integer numbers and ends with the number 0. Determine the value of the second largest element in this sequence. It is guaranteed that the sequence has at least two elements. 

``` .py
s = []
temp = 1
while temp != 0:
    temp = int(input())
    s.append(temp)
s.sort()
print(s[-2])
```
![](Images/Snakify/6.12.jpg)

## The number of elements equal to the maximum 

 A sequence consists of integer numbers and ends with the number 0. Determine how many elements of this sequence are equal to its largest element. 

``` .py
s = []
temp = 1
while temp != 0:
    temp = int(input())
    s.append(temp)
print(s.count(max(s)))
```
![](Images/Snakify/6.13.jpg)

## Fibonacci numbers 

The Fibonacci sequence is defined as follows:
ϕ0=0, ϕ1=1, ϕn=ϕn−1+ϕn−2.
Given a non-negative integer n, print the nth Fibonacci number ϕn.

This problem can also be solved with a for loop. 

``` .py
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
n = int(input())
print(fib(n))
```
![](Images/Snakify/6.14.jpg)

## The index of a Fibonacci number 

The Fibonacci sequence is defined as follows:
ϕ0=0, ϕ1=1, ϕn=ϕn−1+ϕn−2.
Given an integer a, determine its index among the Fibonacci numbers, that is, print the number n such that ϕn=a. If a is not a Fibonacci number, print -1. 

``` .py
n = int(input())
a = 0
b = 1
c = 0
count = 1
while c < n:
    c = a + b
    a = b
    b = c
    count += 1
if c == n:
    print(count)
else:
    print(-1)

```
![](Images/Snakify/6.15.jpg)

## The maximum number of consecutive equal elements 

 Given a sequence of integer numbers ending with the number 0. Determine the length of the widest fragment where all the elements are equal to each other. 

``` .py
n = int(input())
max = 1
count = 1
while n != 0:
    n1 = int(input())
    if n == n1:
        count += 1
        if max < count:
            max = count
    else:
        count = 1
    n = n1
print(max)

```
![](Images/Snakify/6.16.jpg)

# Chapter 7

## Even indices 

 Given a list of numbers, find and print all the list elements with an even index number. (i.e. A[0], A[2], A[4], ...). 

``` .py
s = str(input())
s = s.split()
for i in range(0, len(s), 2):
    print(s[i], end=' ')
```
![](Images/Snakify/7.1.jpg)

## Even elements 

 Given a list of numbers, find and print all elements that are an even number. In this case use a for-loop that iterates over the list, and not over its indices! That is, don't use range() 

``` .py
numbers = str(input())
numbers = numbers.split()
for number in numbers:
    if int(number) % 2 == 0:
        print((number), end=" ")
```
![](Images/Snakify/7.2.jpg)

## Greater than previous 

 Given a list of numbers, find and print all the elements that are greater than the previous element. 

``` .py
s = str(input())
s = s.split()
for i in range(1, len(s)):
    if int(s[i]) > int(s[i-1]):
        print(s[i], end=' ')

```
![](Images/Snakify/7.3.jpg)

## Neighbors of the same sign 

 Given a list of numbers, find and print the first adjacent elements which have the same sign. If there is no such pair, leave the output blank. 

``` .py
s = str(input())
s = s.split()
for i in range(len(s)):
    s[i] = int(s[i])
for i in range(len(s) - 1):
    if s[i] * s[i + 1] > 0:
        print(s[i], s[i + 1])
        break
```
![](Images/Snakify/7.4.jpg)

## Greater than neighbours 

Given a list of numbers, determine and print the quantity of elements that are greater than both of their neighbors.

The first and the last items of the list shouldn't be considered because they don't have two neighbors. 

``` .py
s = str(input())
s = s.split()
s = [int(i) for i in s]
count = 0
for i in range(1, len(s) - 1):
    if s[i] > s[i - 1] and s[i] > s[i + 1]:
        count += 1
print(count)
```
![](Images/Snakify/7.5.jpg)

## The largest element 

 Given a list of numbers. Determine the element in the list with the largest value. Print the value of the largest element and then the index number. If the highest element is not unique, print the index of the first instance. 

``` .py
s = str(input())
list = s.split()
max = 0
for i in range(len(list)):
    if int(list[i]) > int(list[max]):
        max = i
print(list[max], max)
```
![](Images/Snakify/7.6.jpg)

## The number of distinct elements 

 Given a list of numbers with all of its elements sorted in ascending order, determine and print the quantity of distinct elements in it. 

``` .py
s = str(input())
s = s.split()
s = [int(i) for i in s]
s = set(s)
print(len(s))
```
![](Images/Snakify/7.7.jpg)

## Swap neighbours 

 Given a list of numbers, swap adjacent items in pairs (A[0] with A[1], A[2] with A[3], etc.). Print the resulting list. If a list has an odd number of elements, leave the last element in place. 

``` .py
s = str(input())
s = s.split()
if len(s) % 2 == 0:
    for i in range(0, len(s), 2):
        s[i], s[i+1] = s[i+1], s[i]
else:
    for i in range(0, len(s)-1, 2):
        s[i], s[i+1] = s[i+1], s[i]
print(' '.join(s))

```
![](Images/Snakify/7.8.jpg)

## Swap min and max 

 Given a list of unique numbers, swap the minimal and maximal elements of this list. Print the resulting list. 

``` .py
s = str(input())
s = s.split()
s = [int(i) for i in s]
min = s[0]
max = s[0]
for i in s:
    if i < min:
        min = i
    if i > max:
        max = i
for i in range(len(s)):
    if s[i] == min:
        s[i] = max
    elif s[i] == max:
        s[i] = min
print(*s)

```
![](Images/Snakify/7.9.jpg)

## The number of pairs of equal 

 Given a list of numbers, count how many element pairs have the same value (are equal). Any two elements that are equal to each other should be counted exactly once. 

``` .py
l = str(input())
l = l.split()
l = [int(i) for i in l]
count = 0
for i in range(len(l)):
    for j in range(len(l)):
        if i != j and l[i] == l[j]:
            count += 1
print(count // 2)
```
![](Images/Snakify/7.10.jpg)

## Unique elements 

 Given a list of numbers, find and print the elements that appear in the list only once. The elements must be printed in the order in which they occur in the original list. 

``` .py
l = str(input())
l = l.split()
for i in l:
    if l.count(i) == 1:
        print(i, end = ' ')
```
![](Images/Snakify/7.11.jpg)

## Queens 

 In chess it is known that it is possible to place 8 queens on an 8×8 chess board such that none of them can attack another. Given a placement of 8 queens on the board, determine if there is a pair of queens that can attach each other on the next move. Print the word NO if no queen can attack another, otherwise print YES. The input consists of eight coordinate pairs, one pair per line, with each pair giving the position of a queen on a standard chess board with rows and columns numbered starting at 1. 

``` .py
q1 = str(input())
q2 = str(input())
q3 = str(input())
q4 = str(input())
q5 = str(input())
q6 = str(input())
q7 = str(input())
q8 = str(input())
q1 = q1.split()
q2 = q2.split()
q3 = q3.split()
q4 = q4.split()
q5 = q5.split()
q6 = q6.split()
q7 = q7.split()
q8 = q8.split()
q1[0] = int(q1[0])
q1[1] = int(q1[1])
q2[0] = int(q2[0])
q2[1] = int(q2[1])
q3[0] = int(q3[0])
q3[1] = int(q3[1])
q4[0] = int(q4[0])
q4[1] = int(q4[1])
q5[0] = int(q5[0])
q5[1] = int(q5[1])
q6[0] = int(q6[0])
q6[1] = int(q6[1])
q7[0] = int(q7[0])
q7[1] = int(q7[1])
q8[0] = int(q8[0])
q8[1] = int(q8[1])
if q1[0] == q2[0] or q1[1] == q2[1] or q1[0] + q1[1] == q2[0] + q2[1] or q1[0] - q1[1] == q2[0] - q2[1]:
    print("YES")
elif q1[0] == q3[0] or q1[1] == q3[1] or q1[0] + q1[1] == q3[0] + q3[1] or q1[0] - q1[1] == q3[0] - q3[1]:
    print("YES")
elif q1[0] == q4[0] or q1[1] == q4[1] or q1[0] + q1[1] == q4[0] + q4[1] or q1[0] - q1[1] == q4[0] - q4[1]:
    print("YES")
elif q1[0] == q5[0] or q1[1] == q5[1] or q1[0] + q1[1] == q5[0] + q5[1] or q1[0] - q1[1] == q5[0] - q5[1]:
    print("YES")
elif q1[0] == q6[0] or q1[1] == q6[1] or q1[0] + q1[1] == q6[0] + q6[1] or q1[0] - q1[1] == q6[0] - q6[1]:
    print("YES")
elif q1[0] == q7[0] or q1[1] == q7[1] or q1[0] + q1[1] == q7[0] + q7[1] or q1[0] - q1[1] == q7[0] - q7[1]:
    print("YES")
elif q1[0] == q8[0] or q1[1] == q8[1] or q1[0] + q1[1] == q8[0] + q8[1] or q1[0] - q1[1] == q8[0] - q8[1]:
    print("YES")
elif q2[0] == q3[0] or q2[1] == q3[1] or q2[0] + q2[1] == q3[0] + q3[1] or q2[0] - q2[1] == q3[0] - q3[1]:
    print("YES")
elif q2[0] == q4[0] or q2[1] == q4[1] or q2[0] + q2[1] == q4[0] + q4[1] or q2[0] - q2[1] == q4[0] - q4[1]:
    print("YES")
elif q2[0] == q5[0] or q2[1] == q5[1] or q2[0] + q2[1] == q5[0] + q5[1] or q2[0] - q2[1] == q5[0] - q5[1]:
    print("YES")
elif q2[0] == q6[0] or q2[1] == q6[1] or q2[0] + q2[1] == q6[0] + q6[1] or q2[0] - q2[1] == q6[0] - q6[1]:
    print("YES")
elif q2[0] == q7[0] or q2[1] == q7[1] or q2[0] + q2[1] == q7[0] + q7[1] or q2[0] - q2[1] == q7[0] - q7[1]:
    print("YES")
elif q2[0] == q8[0] or q2[1] == q8[1] or q2[0] + q2[1] == q8[0] + q8[1] or q2[0] - q2[1] == q8[0] - q8[1]:
    print("YES")
elif q3[0] == q4[0] or q3[1] == q4[1] or q3[0] + q3[1] == q4[0] + q4[1] or q3[0] - q3[1] == q4[0] - q4[1]:
    print("YES")
elif q3[0] == q5[0] or q3[1] == q5[1] or q3[0] + q3[1] == q5[0] + q5[1] or q3[0] - q3[1] == q5[0] - q5[1]:
    print("YES")
elif q3[0] == q6[0] or q3[1] == q6[1] or q3[0] + q3[1] == q6[0] + q6[1] or q3[0] - q3[1] == q6[0] - q6[1]:
    print("YES")
elif q3[0] == q7[0] or q3[1] == q7[1] or q3[0] + q3[1] == q7[0] + q7[1] or q3[0] - q3[1] == q7[0] - q7[1]:
    print("YES")
elif q3[0] == q8[0] or q3[1] == q8[1] or q3[0] + q3[1] == q8[0] + q8[1] or q3[0] - q3[1] == q8[0] - q8[1]:
    print("YES")
elif q4[0] == q5[0] or q4[1] == q5[1] or q4[0] + q4[1] == q5[0] + q5[1] or q4[0] - q4[1] == q5[0] - q5[1]:
    print("YES")
elif q4[0] == q6[0] or q4[1] == q6[1] or q4[0] + q4[1] == q6[0] + q6[1] or q4[0] - q4[1] == q6[0] - q6[1]:
    print("YES")
elif q4[0] == q7[0] or q4[1] == q7[1] or q4[0] + q4[1] == q7[0] + q7[1] or q4[0] - q4[1] == q7[0] - q7[1]:
    print("YES")
elif q4[0] == q8[0] or q4[1] == q8[1] or q4[0] + q4[1] == q8[0] + q8[1] or q4[0] - q4[1] == q8[0] - q8[1]:
    print("YES")
elif q5[0] == q6[0] or q5[1] == q6[1] or q5[0] + q5[1] == q6[0] + q6[1] or q5[0] - q5[1] == q6[0] - q6[1]:
    print("YES")
elif q5[0] == q7[0] or q5[1] == q7[1] or q5[0] + q5[1] == q7[0] + q7[1] or q5[0] - q5[1] == q7[0] - q7[1]:
    print("YES")
elif q5[0] == q8[0] or q5[1] == q8[1] or q5[0] + q5[1] == q8[0] + q8[1] or q5[0] - q5[1] == q8[0] - q8[1]:
    print("YES")
elif q6[0] == q7[0] or q6[1] == q7[1] or q6[0] + q6[1] == q7[0] + q7[1] or q6[0] - q6[1] == q7[0] - q7[1]:
    print("YES")
elif q6[0] == q8[0] or q6[1] == q8[1] or q6[0] + q6[1] == q8[0] + q8[1] or q6[0] - q6[1] == q8[0] - q8[1]:
    print("YES")
elif q7[0] == q8[0] or q7[1] == q8[1] or q7[0] + q7[1] == q8[0] + q8[1] or q7[0] - q7[1] == q8[0] - q8[1]:
    print("YES")
else:
    print("NO")
```
![](Images/Snakify/7.12.jpg)

## The bowling alley 

 In bowling, the player starts wtih 10 pins at the far end of a lane. The object is to knock all the pins down. For this exercise, the number of pins and balls will vary. Given the number of pins N and then the number of balls K to be rolled, followed by K pairs of numbers (one for each ball rolled), determine which pins remain standing after all the balls have been rolled. The balls are numbered from 1 to N (inclusive) for this situation. The subsequent number pairs, one for each K represent the start to stop (inclusive) positions of the pins that were knocked down with each role. Print a sequence of N characters, where "I" represents a pin left standing and "." represents a pin knocked down. 

``` .py
N, K = [int(s) for s in input().split()]
alley = ['I'] * N
for i in range(K):
    left, right = [int(s) for s in input().split()]
    for j in range(left - 1, right):
        alley[j] = '.'
print(''.join(alley))
```
![](Images/Snakify/7.13.jpg)

# Chapter 8

## The length of the segment 

Given four real numbers representing cartesian coordinates: (x1,y1),(x2,y2). Write a function distance(x1, y1, x2, y2) to compute the distance between the points (x1,y1) and (x2,y2). Read four real numbers and print the resulting distance calculated by the function.

The formula for distance between two points can be found at Wolfram. 

``` .py
def distance(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))
print(distance(x1, y1, x2, y2))
```
![](Images/Snakify/8.1.jpg)

## Negative exponent 

Given a positive real number a and integer n.

Compute a**n. Write a function power(a, n) to calculate the results using the function and print the result of the expression.

Don't use the same function from the standard library. 

``` .py
def power(a, n):
    result = 1
    for i in range(abs(n)):
        result *= a
    if n >= 0:
        return result
    else:
        return 1 / result

print(power(float(input()), int(input())))
```
![](Images/Snakify/8.2.jpg)

## Uppercase 

Write a function capitalize(lower_case_word) that takes the lower case word and returns the word with the first letter capitalized. Eg., print(capitalize('word')) should print the word Word.

Then, given a line of lowercase ASCII words (text separated by a single space), print it with the first letter of each word capitalized using the your own function capitalize().

In Python there is a function ord(character), which returns character code in the ASCII chart, and the function chr(code), which returns the character itself from the ASCII code. For example, ord('a') == 97, chr(97) == 'a'. 

``` .py
def capitalize(a):
    st = a.split(" ")
    result = []
    for i in range(len(st)):
        b = st[i]
        c = b[0].upper() + b[1:len(st[i])]
        result.append(c)
    return(" ".join(result))
print(capitalize(input()))
```
![](Images/Snakify/8.3.jpg)

## Exponentiation 

Given a positive real number a and a non-negative integer n. Calculate an without using loops, ** operator or the built in function math.pow(). Instead, use recursion and the relation an=a⋅an−1. Print the result.

Form the function power(a, n). 

``` .py
def power(a, n):
    if n == 0:
        return 1
    else:
        return a * power(a, n - 1)
a = float(input())
n = int(input())
print(power(a, n))
```
![](Images/Snakify/8.4.jpg)

## Reverse the sequence 

Given a sequence of integers that end with a 0. Print the sequence in reverse order.

Don't use lists or other data structures. Use the force of recursion instead. 

``` .py
def reverse():
    x = int(input())
    if x != 0:
        reverse()
    print(x)

reverse()
```
![](Images/Snakify/8.5.jpg)

## Fibonacci numbers 

Given a non-negative integer n, print the nth Fibonacci number. Do this by writing a function fib(n) which takes the non-negative integer n and returns the nth Fibonacci number.

Don't use loops, use the flair of recursion instead. However, you should think about why the recursive method is much slower than using loops. 

``` .py
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


print(fib(int(input())))

```
![](Images/Snakify/8.6.jpg)

# Chapter 9

## Maximum 

Given two integers representing the rows and columns (m×n), and subsequent m rows of n elements, find the index position of the maximum element and print two numbers representing the index (i×j) or the row number and the column number. If there exist multiple such elements in different rows, print the one with smaller row number. If there multiple such elements occur on the same row, output the smallest column number. 

``` .py
n, m = [int(j) for j in input().split()]
a = [[int(j) for j in input().split()] for i in range(n)]
max_row = 0
max_col = 0
max = a[max_row][max_col]
for i in range(n):
    for j in range(m):
        if max < a[i][j]:
            max = a[i][j]
            max_row = i
            max_col = j
print(max_row, max_col)
```
![](Images/Snakify/9.1.jpg)

## Snowflake 

Given an odd number integer n, produce a two-dimensional array of size (n×n). Fill each element with a single character string of "." . Then fill the middle row, the middle column and the diagnals with the single character string of "*" (an image of a snow flake). Print the array elements in (n×n) rows and columns and separate the characters with a single space. 

``` .py
n = int(input())
a = [['.'] * n for i in range(n)]
for i in range(n):
    a[n // 2][i] = '*'
    a[i][n // 2] = '*'
    a[i][i] = '*'
    a[n-i-1][i] = '*'
for row in a:
    print(' '.join(row))

```
![](Images/Snakify/9.2.jpg)

## Chess board 

Given two numbers n and m. Create a two-dimensional array of size (n×m) and populate it with the characters "." and "*" in a checkerboard pattern. The top left corner should have the character "." . 

``` .py
def board(n, m):
    if (n + m) % 2 == 0:
        return '.'
    else:
        return '*'

n, m = [int(j) for j in input().split()]
a = [[board(i, j) for j in range(m)] for i in range(n)]
for row in a:
    print(' '.join(row))
```
![](Images/Snakify/9.3.jpg)

## The diagonal parallel to the main 

Given an integer n, produce a two-dimensional array of size (n×n) and complete it according to the following rules, and print with a single space between characters:

    On the main diagonal write 0 .
    On the diagonals adjacent to the main, write 1 .
    On the next adjacent diagonals write 2 and so forth. 

Print the elements of the resulting array. 

``` .py
n = int(input())
a = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        a[i][j] = abs(i - j)
for i in range(n):
    print(*a[i])
```
![](Images/Snakify/9.4.jpg)

## Side diagonal 

Given an integer n, create a two-dimensional array of size (n×n) and populate it as follows, with spaces between each character:

    The positions on the minor diagonal (from the upper right to the lower left corner) receive 1 .
    The positions above this diagonal recieve 0 .
    The positions below the diagonal receive 2 . 

Print the elements of the resulting array. 

``` .py
n = int(input())
matrix = [[0 for i in range(n)] for j in range(n)]
for i in range(n):
    for j in range(n):
        if i + j == n - 1:
            matrix[i][j] = 1
        elif i + j > n - 1:
            matrix[i][j] = 2
for i in range(n):
    print(*matrix[i])
```
![](Images/Snakify/9.5.jpg)

## Swap the columns 

Given two positive integers m and n, m lines of n elements, giving an m×n matrix A, followed by two non-negative integers i and j less than n, swap columns i and j of A and print the result.

Write a function swap_columns(a, i, j) and call it to exchange the columns. 

``` .py
def swap_columns(a, i, j):
    for row in a:
        row[i], row[j] = row[j], row[i]
    return a
m, n = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(m)]
i, j = map(int, input().split())
a = swap_columns(a, i, j)
for row in a:
    print(*row)
```
![](Images/Snakify/9.6.jpg)

## Scale a matrix 

Given two positive integers m and n, m lines of n elements, giving an m×n matrix A, followed by one integer c, multiply every entry of the matrix by c and print the result. 

``` .py
m, n = map(int, input().split())
A = [[int(x) for x in input().split()] for _ in range(m)]
c = int(input())
for row in A:
    print(*[x*c for x in row])
```
![](Images/Snakify/9.7.jpg)

## Multiply two matrices 

Given three positive integers m, n and r, m lines of n elements, giving an m×n matrix A, and n lines of r elements, giving an n×r matrix B, form the product matrix AB, which is the m×r matrix whose (i,k) entry is the sum
A[i][1]∗B[1][k]+⋯+A[i][n]∗B[n][k]
and print the result. 

``` .py
temp = input()
m, n, r = temp.split()
m = int(m)
n = int(n)
r = int(r)
A = []
B = []
for i in range(m):
    temp = input()
    temp = temp.split()
    A.append(temp)
for i in range(n):
    temp = input()
    temp = temp.split()
    B.append(temp)
for i in range(m):
    for j in range(r):
        sum = 0
        for k in range(n):
            sum = sum + int(A[i][k]) * int(B[k][j])
        print(sum, end = " ")
    print()
```
![](Images/Snakify/9.8.jpg)

# Chapter 10

## The number of distinct numbers 

Given a list of integers. Determine how many distinct numbers there are.

This task can be solved in one line of code.

``` .py
print(len(set([int(i) for i in input().split()])))
```
![](Images/Snakify/10.1.jpg)

## The number of equal numbers 

Given two lists of numbers. Count how many unique numbers occur in both of them.

This task can be solved in one line of code.

``` .py
print(len(set(input().split()) & set(input().split())))
```
![](Images/Snakify/10.2.jpg)

## The intersection of sets 

Given two lists of numbers. Find all the numbers that occur in both the first and the second list and print them in ascending order.

Even this task can be solved in one line of code.

``` .py
print(*sorted(set(input().split()) & set(input().split())))
```
![](Images/Snakify/10.3.jpg)

## Has the number been encountered before 

 Given a sequence of numbers, determine if the next number has already been encountered. For each number, print the word YES (in a separate line) if this number has already been encountered, and print NO, if it has not already been encountered.

``` .py
n = input().split()
s = set()
for i in n:
    if i in s:
        print("YES")
    else:
        print("NO")
        s.add(i)
```
![](Images/Snakify/10.4.jpg)

## Cubes 

Alice and Bob like to play with colored cubes. Each child has its own set of cubes and each cube has a distinct color, but they want to know how many unique colors exist if they combine their block sets. To determine this, the kids enumerated each distinct color with a random number from 0 to 108. At this point their enthusiasm dried up, and you are invited to help them finish the task.

Given two integers that indicate the number of blocks in Alice's and then Bob's sets N
and M. The following N lines contain the numerical color value for each cube in Alice's set. Then the last M

rows contain the numberical color value for each cube in Bob's set.

Find three sets: the numerical colors of cubes in both sets, the numerical colors of cubes only in Alice's set, and the numerical colors of cubes only in Bob's set. For each set, print the number of elements in the set, followed by the numerical color elements, sorted in ascending order. 

``` .py
n, m = [int(j) for j in input().split()]
A = set()
B = set()
for i in range(n):
    A.add(int(input()))
for i in range(m):
    B.add(int(input()))
C = A & B
D = A - B
Е = B - A
print(len(C))
print(*sorted(C), key=int)
print(len(D))
print(*sorted(D), key=int)
print(len(Е))
print(*sorted(Е), key=int)
```
![](Images/Snakify/10.4.jpg)

## The number of distinct words in some text 

Given a number n, followed by n lines of text, print the number of distinct words that appear in the text.

For this, we define a word to be a sequence of non-whitespace characters, seperated by one or more whitespace or newline characters. Punctuation marks are part of a word, in this definition.

``` .py
n = int(input())
words = []
for i in range(n):
    words += input().split()
print(len(set(words)))
```
![](Images/Snakify/10.5.jpg)

## Guess the number 

Augustus and Beatrice play the following game. Augustus thinks of a secret integer number from 1 to n. Beatrice tries to guess the number by providing a set of integers. Augustus answers YES if his secret number exists in the provided set, or NO, if his number does not exist in the provided numbers. Then after a few questions Beatrice, totally confused, asks you to help her determine Augustus's secret number.

Given the value of n
in the first line, followed by the a sequence Beatrice's guesses, series of numbers seperated by spaces and Agustus's responses, or Beatrice's plea for HELP. When Beatrice calls for help, provide a list of all the remaining possible secret numbers, in ascending order, separated by a space.

``` .py
n = int(input())
numbers = [i for i in range(1, n+1)]
while True:
    try:
        guess = input().split()
        if guess[0] == "HELP":
            print(*numbers)
            break
        else:
            guess = [int(i) for i in guess]
            answer = input()
            if answer == "YES":
                numbers = [i for i in numbers if i in guess]
            else:
                numbers = [i for i in numbers if i not in guess]
    except EOFError:
        break
```
![](Images/Snakify/10.6.jpg)

## Polyglots 

Each student at a certain school speaks a number of languages. We need to determine which languges are spoken by all the students, which languages are spoken by at least one student.

Given, the number of students, and then for each student given the number of languages they speak followed by the name of each language spoken, find and print the number of languages spoken by all the students, followed by a list the languages by name, then print the number of languages spoken by at least one student, followed by the list of the languages by name. Print the languages in alphabetical order.

``` .py
s = [{input() for j in range(int(input()))} for i in range(int(input()))]
lall, lone = set.intersection(*s), set.union(*s)
print(len(lall), *sorted(lall), sep='\n')
print(len(lone), *sorted(lone), sep='\n')
```
![](Images/Snakify/10.7.jpg)

## Number of occurrences 

The text is given in a single line. For each word of the text count the number of its occurrences before it.

A word is a sequence of non-whitespace characters. Two consecutive words are separated by one or more spaces. Punctiation marks are a part of a word, by this definition. 

``` .py
words = input().split()
for i in range(len(words)):
    print(words[:i].count(words[i]), end=' ')
```
![](Images/Snakify/11.1.jpg)

## Dictionary of synonyms 

You are given a dictionary consisting of word pairs. Every word is a synonym the other word in its pair. All the words in the dictionary are different.

After the dictionary there's one more word given. Find a synonym for him.

``` .py
n = int(input())
d = {}
for i in range(n):
    k, v = input().split()
    d[k] = v
    d[v] = k
print(d[input()])
```
![](Images/Snakify/11.2.jpg)

## Elections in the USA 

As you know, the president of USA is elected not by direct vote, but through a two-step voting. First elections are held in each state and determine the winner of elections in that state. Thereafter, the state election is going: in this election, every state has a certain the number of votes — the number of electors from that state. In practice, all the electors from the state of voted in accordance with the results of the vote within a state.

The first line contains the number of records. After that, each entry contains the name of the candidate and the number of votes they got in one of the states. Count the total results of the elections: sum the number of votes for each candidate. Print candidates in the alphabetical order.

``` .py
n = int(input())
d = {}
for i in range(n):
    name, votes = input().split()
    votes = int(votes)
    if name in d:
        d[name] += votes
    else:
        d[name] = votes
for name in sorted(d):
    print(name, d[name])
```
![](Images/Snakify/11.3.jpg)

## The most frequent word 

 Given the text: the first line contains the number of lines, then given the lines of words. Print the word in the text that occurs most often. If there are many such words, print the one that is less in the alphabetical order.

``` .py
l = int(input())
s = []
for i in range(l):
    s += input().split()
d = {}
for i in s:
    d[i] = d.get(i, 0) + 1
m = max(d.values())
for i in sorted(d):
    if d[i] == m:
        print(i)
        break
```
![](Images/Snakify/11.4.jpg)

## Access rights 

The virus attacked the filesystem of the supercomputer and broke the control of access rights to the files. For each file there is a known set of operations which may be applied to it:

    write W,
    read R,
    execute X. 

The first line contains the number N — the number of files contained in the filesystem. The following N lines contain the file names and allowed operations with them, separated by spaces. The next line contains an integer M — the number of operations to the files. In the last M lines specify the operations that are requested for files. One file can be requested many times.

You need to recover the control over the access rights to the files. For each request your program should return OK if the requested operation is valid or Access denied if the operation is invalid.

``` .py
permissions = {}
n = int(input())
for _ in range(n):
     s = input().split()
     permissions[s[0]] = set(s[1:])
for _ in range(int(input())):
     perm, file = input().split()
     if perm == 'read':
         perm = 'R'
     if perm == 'write':
         perm = 'W'
     if perm == 'execute':
         perm = 'X'
     if perm in permissions[file]:
         print('OK')
     else:
         print('Access denied')
```
![](Images/Snakify/11.5.jpg)

## Countries and cities 

 Given a list of countries and cities of each country. Then given the names of the cities. For each city specify the country in which it is located.

``` .py
n = int(input())
d = {}
for i in range(n):
    country, *cities = input().split()
    for city in cities:
        d[city] = country
m = int(input())
for i in range(m):
    print(d[input()])
```
![](Images/Snakify/11.6.jpg)

## Frequency analysis 

Given a number n, followed by n lines of text, print all words encountered in the text, one per line. The words should be sorted in descending order according to their number of occurrences in the text, and all words with the same frequency should be printed in lexicographical order.

Hint. After you create a dictionary of the words and their frequencies, you would like to sort it according to the frequencies. This can be achieved if you create a list whose elements are tuples of two elements: the frequency of occurrence of a word and the word itself. For example, [(2, 'hi'), (1, 'what'), (3, 'is')]. Then the standard list sort will sort a list of tuples, with the tuples compared by the first element, and if these are equal, by the second element. This is nearly what is required in the problem.

``` .py
counter = {}
for i in range(int(input())):
    line = input().split()
    for word in line:
        counter[word] = counter.get(word, 0) + 1

for i in sorted(counter.items(), key=lambda x:(-x[1],x[0])): 
    print(i[0])
```
![](Images/Snakify/11.7.jpg)

## English-Latin dictionary 

One day, going through old books in the attic, a student Bob found English-Latin dictionary. By that time he spoke English fluently, and his dream was to learn Latin. So finding the dictionary was just in time.

Unfortunately, full-fledged language studying process requires also another type of dictionary: Latin-English. For lack of a better way he decided to make a second dictionary using the first one.

As you know, the dictionary consists of words, each of which contains multiple translations. For each Latin word that appears anywhere in the dictionary, Bob has to find all its translations (that is, all English words, for which our Latin word is among its translations), and take them and only them as the translations of this Latin word.

Help him to create a Latin-English.

The first line contains a single integer N — the number of English words in the dictionary. Followed by N dictionary entries. Each entry is contained on a separate line, which contains first the English word, then a hyphen surrounded by spaces and then comma-separated list with the translations of this English word in Latin. All the words consist only of lowercase English letters. The translations are sorted in lexicographical order. The order of English words in the dictionary is also lexicographic.

Print the corresponding Latin-English dictionary in the same format. In particular, the first word line should be the lexicographically minimal translation of the Latin word, then second in that order, etc. Inside the line the English words should be sorted also lexicographically. 

``` .py
n = int(input())
ld = dict()
for i in range(n):
    ew, lw = input().split(" - ")
    lws = lw.split(", ")
    for w in lws:
        if w in ld:
            ld[w].append(ew)
        else:
            ld[w] = [ew]
print(len(ld))
for lw in sorted(ld):
    print(lw, " - ", ", ".join(ld[lw]))
```
![](Images/Snakify/11.8.jpg)

## TEMPLATE_TITLE

TEMPLATE_STATEMENT

``` .py
TEMPLATE_SCRIPT
```
![](Images/Snakify/x.x.jpg)

I did it, after so many hours, I did it. Now I can rest