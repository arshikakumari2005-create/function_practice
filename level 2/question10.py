# create a function that takes number as input and print the table.
def table_num(num):
    for x in range(1,11):
        table= num * x
        print(f"{num} X {x} = {table}")

num=int(input("enter num"))
table_num(num)
 