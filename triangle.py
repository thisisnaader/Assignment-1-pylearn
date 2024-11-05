#input

a = int(input("enter the frist side's size: "))
b = int(input("enter the second side's size: "))
c = int(input("enter the third side's size: "))

#process

if (a + b) > c :
    if ((b + c) > a) and ((c + a) > b) :
        result = "YES"
elif (a + c) > b :
        if ((b + c) > a) and ((a + b) > c) :
            result = "YES"
elif (b + c) > a :
        if ((a + b) > c) and ((a + c) > b) :
            result = "YES"
else :
     result = "NO"

#output

print(result)