# take  5 number as input from the user and find the sum of list.
def sum_num(user_list):
    for x in range(5):
       user=int(input("enter num="))
       user_list.append(user)
    # direct sum() use
    return sum(user_list)
      
user_list=[]
result=sum_num(user_list)
print(f"total sum={result}")