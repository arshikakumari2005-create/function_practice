# convert a string to uppercase without upper().
# ord(),chr()
# a-z=97-122
# A-Z=65-90
# 0-9=48-57

def uppercase(text): 
    word_store=" "
    for x in text:
        if x >='a' and x <='z':
            char_into_no=ord(x) - 32
            no_into_char=chr(char_into_no)
            word_store += no_into_char
    return word_store        


meassage=input("enter message")   
result=uppercase(meassage)
print(f"{meassage} conver in uppercase, ok \n{result}")    


