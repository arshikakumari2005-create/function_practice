# cerate a function that takes numbers as input and print fibonacci series.
def fibonacci(term):
    a=0
    b=1
    for i in range(term):
        print(a,end=" ")
        # why we use print(a,end=" ")---> print + same line + space 
        # display--0 1 1 2 3 👍🏻
        next=a+b
        a=b
        b=next

num=int(input("enter number of terms="))
fibonacci(num) 
