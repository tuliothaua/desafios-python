# This Program simulates a Magic 8 Ball!

#[INFO] :: Importing the Random Module!
import random

#[INFO] :: Generating a random number between 1 and 9
num = random.randint(1, 9)

#[FUNC] :: Getting the User's Question and Providing an Answer!
print("- [Welcome to the Magic 8 Ball!] -")
question = input("> Type a question: ")
answer = "Unknown"

# [COND] :: Determining the Answer Based on the Random Number!
if num == 1:
  answer = "Yes - definitely."
elif num == 2:
  answer = "It is decidedly so."
elif num == 3:
  answer = "Without a doubt."
elif num == 4:
  answer = "Reply hazy, try again."
elif num == 5:
  answer = "Ask again later."
elif num == 6:
  answer = "Better not tell you now."
elif num == 7:
  answer = "My sources say no."
elif num == 8:
  answer = "Outlook not so good."
elif num == 9:
  answer = "Very doubtful."
else:
  answer = "Unknown"

# [EXEC] :: Spitting the Question and Answer on the Screen!
print(f"\n[Question]: {question}")
print(f"\n[Magic 8 Ball]: {answer}")