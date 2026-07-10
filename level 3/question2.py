# take  5 number as input from the user and find the sum of list, but without using sum().
def sum_num(user_list):
    count=0
    for x in range(5):
       user=int(input("enter num="))
       user_list.append(user)
       count+=user
    return count
      
user_list=[]
result=sum_num(user_list)
print(f"total sum={result}")