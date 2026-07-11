# function prectice
# print odd number from the list 
def odd_num(my_list):
    odd_list=[]
    for x in my_list:
        if x % 2==1:
            odd_list.append(x)
    return odd_list        


my_list=[1,2,3,4,5,6,7,8,9,10]
result=odd_num(my_list)
print(f"{my_list}\nodd num={result}")    