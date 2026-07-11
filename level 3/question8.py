# print even number from the list.
def even_num(my_list):
    even_list=[]
    for check in my_list:
        if check % 2 == 0:
            even_list.append(check)
    return even_list
           
my_list=[1,2,3,4,5,6,7,8,9,10]
 
result= even_num(my_list)
print(f"{my_list}\n{result}")
