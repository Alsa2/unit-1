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
with open('studentdirectory.txt', 'w') as f:
    pass



for ln in LastName:
    templockernum = random.randint(1,2400)
    final = (f"{ln}, {Names[ln]}, {Names[ln]}.{ln}@uwcisak.jp, locker {templockernum}"),
    with open('studentdirectory.txt', 'a') as f:
        f.write(str(final))
        f.write("\n")
        f.close()