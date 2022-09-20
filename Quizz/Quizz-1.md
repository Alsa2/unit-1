#Quizz 1
### Quizz 001 Solution

![](../Images/quiz001.jpg)

 **Fig. 1** This is the solution to the black box
 
 **Fig. 1** shows my solution to quiz 001. The procedure to generate the outputs below are
 
| Input         | Output |
|---------------|--------|
| International | I11l   |
| My            | My     |
| Cat           | C1t    |
| (1b@!)        | (4)    |

### Quizz 001 Script

``` .py
import re
x = str(input())
if x == "":
    print("Empty String")
    exit()
wordcount = (len(re.findall(r'\w+',x)))
x = x.split()
for item in x:
    item = str(item)
    #itemlenght is the length of the word
    itemleght = int(len(item))
    #the inter variable is the number of times the word in the word
    inter = str(itemlenght -2)
    if itemlenght < 3:
        print(item)
    else:
        str = item
        len = len(str)
	#first caracter
        fc = str[:1]
	#last caracter
        lc = str[len-1:len]
        print("".join([fc, inter, lc]))
```
![](../Images/quiz1-flowchart.jpg)
**Fig. 2** FlowChart
![](../Images/quizz1proof.png)
**Fig. 3** Proofs