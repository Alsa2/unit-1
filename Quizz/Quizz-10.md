# Quizz 10
### Sl Program

```.py
def powerTen(number: int) -> str:
    """..."""
    lenght_msg = 20
    units = ["unit", "kilo", "mega", "giga", "tera"]
    out = ""
    for power in range(5):
        number = f"{number} {'0'*(3*power)}"
        out += f"{number} {units[power]}\n"
    return out

test1 = powerTen(1)
print(test1)

```

###Hl Program

```.py
input_number = input("Input a number with unit: ")
n = [int(input_number) for input_number in input_number.split() if input_number.isdigit()]
final = []
powers = []
Units = ["Tera", "Giga", "Mega", "Kilo", "Unit", "Milli", "Micro", "Nano", "Pico"]
length_lmsg = 20


def power(n):
    count = 0
    for i in range(-12, 0, 3):
        temp = abs(i // 3)
        number = f"0.{(('000 ') * temp)}{str(n[0])} ".ljust(length_lmsg)
        powers.append(f"{number}{Units[count]}")
        count += 1
    for i in range(0, 15, 3):
        temp = i//3
        number = f"{str(n[0])} {('000 '*temp)} ".ljust(length_lmsg)
        powers.append(f"{number}{Units[count]}")
        count += 1

    return powers

print("\n".join(power(n)))
```
![](../../Images/lesson10-mainscript.png)

 **Fig. 1** My flow diagram

 ![](../../Images/lesson10-definition.png)

 **Fig. 1** My flow diagram definition

 ![](../../Images/quizz-10-proof.png)

 **Fig. 1** Proof