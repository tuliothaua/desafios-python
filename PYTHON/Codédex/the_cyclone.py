# This program checks if a user meets the requirements to ride "The Cyclone"

#[VAR] :: cost of ride and height requirement!
cost = 10
height_requirement = 137

#[INPUT] :: get user height and credits
height = int(input("> Type your height: "))
credits = int(input("> How many credits do you have: "))

#[PROCESS & OUTPUT] :: check if user meets both requirements
if height > height_requirement and credits > cost:
  print("\n[Enjoy the ride!]")
elif credits > 10 and height < height_requirement:
  print ("\n[You are not tall enough to ride.]")
elif height > height_requirement and credits < cost:
  print("\n[You don't have enough credits.]")
else:
  print("\n[You have not met either requirement]")