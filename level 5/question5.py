# search student marks
student={"arshika":85.80,
         "rohan":78.0,
         "aman":56.0,
         "raman":79.60,
         "suman":81.0,}
user=input("enter name for search marks=").lower()
for key,value in student.items():
    if key == user:
        print(f"student name ={key} and marks ={value}")            
        