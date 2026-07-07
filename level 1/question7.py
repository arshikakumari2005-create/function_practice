# make a function that takes a two number as a input and swap them.
def swap(number1,number2):
    temp=number1
    number1=number2
    number2=temp
    return number1,number2
    # shortcut--swap in one line
    number1,number2=number2,number1
num1=int(input("enter no1="))
num2=int(input("enter no2="))
result=swap(num1,num2)
print(f"swapped value = {result}")

