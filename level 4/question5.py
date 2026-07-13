# count spaces in string.
def spaces_count(text): 
    count=0
    for x in message:
        if x == " ":
            count += 1
    return(count)  

message=input("enter your message=")
result=spaces_count(message)
print(result)