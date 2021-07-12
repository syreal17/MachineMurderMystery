################################################################################
# This is a mock up of the game. It's a choose your own adventure
################################################################################

print("Welcome to Machine Murder Mystery!\n")

print("In this game you will gather eyewitness testimony and try to determine")
print("who on the train is the culprit!\n\n")

print("The train has been detained at this stop and no one is being let on or")
print("off besides members of the investigation team, like yourself.")

print("The officer guarding the door to the caboose nods to you as you enter")
print("the car. Once inside you see a woman sitting on a cot.\n")

print("How do you proceed?")
print("1.) Talk to the woman")
print("2.) Move to the next car\n\n")

print("Your choice? (1 or 2) ")
choice = int(input())

if choice == 1:
  print("This would kickstart interaction with the AI as this character")
elif choice == 2:
  print("This would move to the kitchen car and reveal another witness")
else:
  print("This would be an error and would kick user back to the previous")
  print("choice until they pick a possible choice 1 or 2.")