import math

#input

hour = int(input("Enter the hour of timer: "))
minute = int(input("Enter minute of timer: "))
second = int(input("Enter second of timer: "))

#process

c = (hour * math.pow(60, 2)) + (minute * 60) + second

#output

print("Converting of time by Second is: ",c)