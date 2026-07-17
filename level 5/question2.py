# print the student with the highest marks.
def dict_student(student_info):

    highest=max(student.values())
    for name,marks in student.items():
        if marks == highest:
            print(f"{name}:{marks}")
 
student={"Arshika":89,"ravi":79,"rohan":81,"aman":45} 
dict_student(student)
    
      
