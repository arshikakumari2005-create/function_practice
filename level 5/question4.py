# Avarge marks
marks={"hindi":89,
       "english":79,
       "math":87}

length=len(marks)
print("length =",length)
sum_marks=sum(marks.values())
print("total marks =",sum_marks)
avg=sum_marks / length
print(f"Avarage marks = {avg}")