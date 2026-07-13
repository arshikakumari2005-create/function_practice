# create a function and count consonants in a string.
def consonants(user_input):
    count=0
    consonants_count=""
    for check in user_input:
        if check not in "aeiou":
            count+=1
            consonants_count+=check
    return count,consonants_count        


user=input("enter word=")
result=consonants(user)
print(f"consonante={result}")    