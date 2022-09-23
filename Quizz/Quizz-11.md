# Quizz 11
### Sl and Hl Program

```.py
#creating the function
def bestMonth(month: int, year: int) -> None:
    #calculate the number of days of the month
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        days = 31
    elif month == 4 or month == 6 or month == 9 or month == 11:
        days = 30
    elif month == 2:
        if year % 4 == 0:
            days = 29
        else:
            days = 28
    else:
        print("Invalid month")
        return
    #calculate the first day of the month
    
    if month == 1 or month == 2:
        month += 12
        year -= 1
    firstDay = (1 + 2 * month + 3 * (month + 1) // 5 + year + year // 4 - year // 100 + year // 400) % 7

    

    print()
    #create a array with months name
    months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
    #print the month name
    month = (month % 12)
    if month == 1:
        print(months[month], year + 1)
    else:
        print(months[month - 1], year)
    #print the days of the week
    print("Mo Tu We Th Fr Sa Su")
    print("   " * firstDay, end = "")
    #print the days of the month
    for i in range(1, days + 1):
        if i < 10:
            print(" " + str(i), end = " ")
        else:
            print(i, end = " ")
        if (i + firstDay) % 7 == 0:
            print()
    print()
    return ("")
    

out = bestMonth(1, 2006)
print(out)
    


```
### Flowchart
It's in the Photo folders, the name is quizz11-flowchart.pdf
(i coulnt't convert it to png (too low quality to see something), so i uploaded it as pdf)

### Proof

```
December 2022
Mo Tu We Th Fr Sa Su
          1  2  3  4 
 5  6  7  8  9 10 11 
12 13 14 15 16 17 18 
19 20 21 22 23 24 25 
26 27 28 29 30 31 



February 2006
Mo Tu We Th Fr Sa Su
                   1 
 2  3  4  5  6  7  8 
 9 10 11 12 13 14 15 
16 17 18 19 20 21 22 
23 24 25 26 27 28 29 
30 31 



September 1945
Mo Tu We Th Fr Sa Su
                1  2 
 3  4  5  6  7  8  9 
10 11 12 13 14 15 16 
17 18 19 20 21 22 23 
24 25 26 27 28 29 30
```