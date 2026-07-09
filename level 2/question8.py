# create a function that takes celsius  as input and convert into fahrenheit.
def celsiuc_into_fahrenheit(celsius):

    fahrenheit=(celsius * 9/5)+32
    print("Fahrenheit=",fahrenheit)

celsius=float(input("enter temperature in celsius="))
celsiuc_into_fahrenheit(celsius)
