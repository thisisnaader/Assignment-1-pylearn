#input

a = int(input("enter the frist side's size: "))
b = int(input("enter the second side's size: "))
c = int(input("enter the third side's size: "))

#process


if (a + b >= c) and (a + c >= b) and (b + c >= a) :
    result = "YES"
else:
    result = "NO"

#output

print(result)