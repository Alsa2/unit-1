# Task 4
Task 1.4 : [HL] Given a list of names of students in the format lastname, firstname, create a program that assigns an email address and a locker to each student and saves the results in a file in the format lastname, firstname, email, locker
Dictionnary of students
```.py
import random
import sys
import os


Names = dict()
Names["Trump"] = "Donald"
Names["Obama"] = "Barack"
Names["Clinton"] = "Bill"
Names["Bush"] = "George"
Names["Reagan"] = "Ronald"
Names["Carter"] = "Jimmy"
Names["Ford"] = "Gerald"
Names["Nixon"] = "Richard"
Names["Johnson"] = "Lyndon"
Names["Kennedy"] = "John"
Names["Eisenhower"] = "Dwight"
Names["Truman"] = "Harry"
Names["Roosevelt"] = "Franklin"
Names["Coolidge"] = "Calvin"
Names["Hoover"] = "Herbert"




LastName = ['Trump', 'Obama', 'Clinton', 'Bush', 'Reagan', 'Carter', 'Ford', 'Nixon', 'Johnson', 'Kennedy', 'Eisenhower', 'Truman', 'Roosevelt', 'Coolidge', 'Hoover']
with open('studentdatabase.txt', 'w') as f:
    pass



for ln in LastName:
    temprandomlocker = random.randint(1,2400)
    final = (f"{ln}, {Names[ln]}, {Names[ln]}.{ln}@uwcisak.jp, locker {temprandomlocker}"),
    with open('studentdatabase.txt', 'a') as f:
        f.write(str(final))
        f.write("\n")
        f.close()
```
### Example output
```
('Trump, Donald, Donald.Trump@uwcisak.jp, locker 151',)
('Obama, Barack, Barack.Obama@uwcisak.jp, locker 2271',)
('Clinton, Bill, Bill.Clinton@uwcisak.jp, locker 2118',)
('Bush, George, George.Bush@uwcisak.jp, locker 619',)
('Reagan, Ronald, Ronald.Reagan@uwcisak.jp, locker 842',)
('Carter, Jimmy, Jimmy.Carter@uwcisak.jp, locker 845',)
('Ford, Gerald, Gerald.Ford@uwcisak.jp, locker 16',)
('Nixon, Richard, Richard.Nixon@uwcisak.jp, locker 1146',)
('Johnson, Lyndon, Lyndon.Johnson@uwcisak.jp, locker 254',)
('Kennedy, John, John.Kennedy@uwcisak.jp, locker 296',)
('Eisenhower, Dwight, Dwight.Eisenhower@uwcisak.jp, locker 264',)
('Truman, Harry, Harry.Truman@uwcisak.jp, locker 1586',)
('Roosevelt, Franklin, Franklin.Roosevelt@uwcisak.jp, locker 1444',)
('Coolidge, Calvin, Calvin.Coolidge@uwcisak.jp, locker 2029',)
('Hoover, Herbert, Herbert.Hoover@uwcisak.jp, locker 799',)
```
