# create a function that takes a numbers as input and check if it is prime.

def prime_no(number):
    if number<=1:
        if number==1:
            print("prime")
        else:
            print(f"{number} is ")    
    elif number>1: 
        count=0  
        for x in range (2,number):
            user % x==0
            count+=1
        if count>=1: 
            print("not prime")
        else:
            print("prime")     

user=int(input("entye no="))
prime_no(user)   
                


  