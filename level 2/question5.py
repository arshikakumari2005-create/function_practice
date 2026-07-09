# create a function that takes numbers/word as input and check if it is palindrome.
def palindrome(number_word):
    copy=number_word
    reverse = copy[::-1]
    if number_word == reverse:
        print("yes it's palindrome ")
    else:
        print("no it's not palindrome ")


num_word=input("enter number/word=").lower()
palindrome(num_word)
     
    
