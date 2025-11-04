# Food Rating System

#[VAR] :: Getting User Input!
rating = float(input("⭐⭐⭐⭐⭐\nHow many stars this restaurant deserve?\n> "))

#[COND] :: Rating the Food!
if rating > 4.5:
  print("Extraordinary")
elif rating > 4:
  print("Excellent")
elif rating > 3:
  print("Good")
elif rating > 2:
  print("Fair")
else: 
  print("Poor")