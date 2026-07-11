# find the largest number in list without using max().
def largest_num(user_list):
    largest = user_list[0]
    for x in user_list:
        if x > largest:
            largest = x
    return largest 

user_list=[31,45,8,19,34,67,3,98,44]
result=largest_num(user_list)
print(f"{user_list}\nlargest num = {result}")
      

