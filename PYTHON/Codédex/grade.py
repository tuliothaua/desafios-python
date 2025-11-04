# High School Grade Identifier

#[VAR] :: Getting User Input!
grade = int(input("Enter your grade: "))

#[COND] :: Identifying the Grade!
if grade == 9:
  print("Freshman")
elif grade == 10:
  print("Sophomore")
elif grade == 11:
  print("Junior")
elif grade == 12:
  print("Senior")
else:
  print("TBD")  