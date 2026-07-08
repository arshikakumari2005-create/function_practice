# create a function that takes a string as input and 'count' the 'Vowels'.
def vowels(text):
    vowels_store=""
    vowels_count=0
    for check in text:
        if check in "aeiou":
            vowels_store+=check
            vowels_count+=1
    print("vowels_word=",vowels_store)  
    print("count=",vowels_count)      

word=input("enter word=").lower()
vowels(word) 

# o\p
# enter word=education
# vowels_word= euaio
# count= 5