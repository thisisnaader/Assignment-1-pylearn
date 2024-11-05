#input

a = int(input("enter the frist side's size: "))
b = int(input("enter the second side's size: "))
c = int(input("enter the third side's size: "))

#process


if (a + b <= c) or (a + c <= b) or (b + c <= a) :
    result = "NO"
else:
    result = "YES"

#output

print(result)