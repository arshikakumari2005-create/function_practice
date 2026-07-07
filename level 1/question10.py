# make a function that takes age as input and tell if someone  can vote or not.
def vote(age):
    if age >= 18:
        print(f"age-{age} you are eligible for vote ")
    else:
        print(f"age-{age} sorry, you are not eligible for vote because you are not 18+ ")

age_no=int(input("enter your age= "))
vote(age_no)
