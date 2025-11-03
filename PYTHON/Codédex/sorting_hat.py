# This program sorts a user into a Hogwarts house based on their answers to questions.

#[VAR] :: Initialize house point counters!
gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0

#[INPUT] :: Question 1!
quest = int(input("Q1) Do you like Dawn or Dusk? \n1) Dawn\n2) Dusk\n\n> "))

#[COND] :: Allocate points based on answer!
if quest == 1:
  gryffindor += 1
  ravenclaw += 1
elif quest == 2:
  hufflepuff += 1
  slytherin += 1
else:
  print("Wrong input")

#[INPUT] :: Question 2!
prompt = """\nQ2) When I'm dead, I want people to remember me as:
1) The Good
2) The Great
3) The Wise
4) The Bold

> """
quest = int(input(prompt))

#[COND] :: Allocate points based on answer!
if quest == 1:
  hufflepuff += 2
elif quest == 2:
  slytherin += 2
elif quest == 3:
  ravenclaw += 2
elif quest == 4:
  gryffindor += 2
else: 
  print("Wrong Input.")

#[INPUT] :: Question 3!
prompt = """\nQ3) Which kind of instrument most pleases your ear?
1) The violin
2) The trumpet
3) The piano
4) The drum

> """

quest = int(input(prompt))

#[COND] :: Allocate points based on answer!
if quest == 1:
  slytherin += 4
elif quest == 2:
  hufflepuff += 4
elif quest == 3:
  ravenclaw += 4
elif quest == 4:
  gryffindor += 4
else: 
  print("Wrong Input.")

#[EXEC] :: Display house points!
print(f"Gryffindor: {gryffindor} points.")
print(f"Slytherin: {slytherin} points.")
print(f"Hufflepuff: {hufflepuff} points.")
print(f"Ravenclaw: {ravenclaw} points.")