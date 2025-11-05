# This program prints a random fun fact.

#[LIBRARIES]
import random

#[VAR] :: A random number between 0 and 5!
num = random.randint(0, 5)

#[COND] :: Print a fun fact based on the random number.
if num == 0:
  print("Flamingos turn pink from eating shrimp")
elif num == 1:
  print("The only food that does\'t spoil is honey.")
elif num == 2:
  print("Shrimp can only swim backwards.")
elif num == 3:
  print("A taste bud\'s life span is about 10 days.")
elif num == 4:
  print("It is impossible to sneeze while sleeping.")
elif num == 5:
  print("It is illegal to sing off-key in North Carolina.")
