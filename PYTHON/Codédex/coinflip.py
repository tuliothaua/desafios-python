#[INFO] :: Library
import random

#[VAR] :: Generating a number either 0 or 1
num = random.randint(0, 1)

#[FUNC] :: 50% Heads 50% Tails
if num > 0.5:
  print('Heads')
else:
  print('Tails')