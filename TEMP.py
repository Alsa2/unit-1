import re
x = str(input())
if x == "":
    print("Empty String")
    exit()
wordcount = (len(re.findall(r'\w+',x)))
x = x.split()
for item in x:
    item = str(item)
    #lw is the length of the word
    lw = int(len(item))
    #the inter variable is the number of times the word in the word
    inter = str(lw -2)
    if lw < 3:
        print(item)
    else:
        str = item
        len = len(str)
        fc = str[:1]
        lc = str[len-1:len]
        print("".join([fc, inter, lc]))
