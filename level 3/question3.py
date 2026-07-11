# create a function and find the average of the list.
def average(user_list):
    length=len(user_list)
    total=sum(user_list) 
    avg=total/length
    return avg

user_list=[]
for x in range(0,5):
    num=int(input("enter num=")) 
    user_list.append(num)
    
result=average(user_list)   
print("Average=",result) 

        