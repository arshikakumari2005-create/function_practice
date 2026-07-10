# create a function that takes Fahrenheit as input and fahrenheit into celsius.
def fahrenheit(f):
    celsius=(f - 32)* 5/9
    return celsius

fahren=float(input("enter fahrenheit="))
result=fahrenheit(fahren)   
print(f"{fahren}F = {result}C")  