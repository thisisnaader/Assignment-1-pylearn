import math

hour = int(input("Enter the hour of timer: "))
minute = int(input("Enter minute of timer: "))
second = int(input("Enter second of timer: "))

c = (hour * math.pow(60, 2)) + (minute * 60) + second

print("Converting of time is: ",c)