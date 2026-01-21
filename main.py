from difference import subtract
from integral_quotient import floor_division
from quotient import divide
from remainder import get_remainder
from sum import add
from product import multiply

inp = input("Please type the operation you wish to perform (add|subtract|multiply|divide|Floor_division|remainder)")
i1 = int(input("Please enter the first number: "))
i2 = int(input("Please enter the second number: "))
inp = inp.lower()

if inp=="add":
    print(add(i1,i2))
elif inp=="subtract":
    print(subtract(i1,i2))
elif inp=="multiply":
    print(multiply(i1,i2))
elif inp=="divide":
    print(divide(i1,i2))
elif inp=="floor_division":
    print(floor_division(i1,i2))
elif inp=="remainder":
    print(get_remainder(i1,i2))