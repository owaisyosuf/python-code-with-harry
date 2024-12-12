# write a program to calculate grade of student

english=int(input("enter your marks in english : "))
urdu=int(input("enter your marks in urdu : "))
math=int(input("enter your marks in math : "))

total_marks=300
mark_obtained=english+urdu+math
percentage=(mark_obtained/total_marks)*100

# print(round(percentage + "%" , 2))
if percentage <=100 and percentage>=90:
  print("your grade is 'A' " )
elif percentage <90 and percentage>= 80:
  print("your grade is 'B' " )
elif percentage <80 and percentage>= 70:
  print("your grade is 'C' " )
elif percentage <70 and percentage>= 60:
  print("your grade is 'D' " )
else:
  print("yor are not clear your exams") 