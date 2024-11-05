import statistics

#input

name = input("Enter first name of student : ")
lastname = input("Enter last name of student :  ")

a = int(input("first point : "))
b = int(input("second point : "))
c = int(input("third point : "))

#process

avg = statistics.mean([a, b, c])

#output

print("student's academic status :  ")
if avg >= 17:
    print(name, lastname,"\nExcellent student")
elif avg < 17 and avg >= 12:
    print(name, lastname, "\nNormal student")
elif avg < 12:
    print(name, lastname, "\nFailing student")
else:
    print("is not defined")