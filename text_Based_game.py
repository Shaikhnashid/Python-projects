print("Welcome to the Haunted Mansion")
print("You are distant Family Member of a rich millionaire who has just passed  way,leaving this mansion to you")
print("As the newfound Owner, you decide to pay a visit to mansion")
print("The house is dated ,creaky,and falling apart,You Walk in the front door")
print("Do you want enter the living room or the dining room?")


roomChoice = input(">")
if roomChoice== "living room":
    print("You Enter the Living room")
    print("As you Walk in,you see a sleeping pitbul guarding some gold jwelery.")
    print("Do you want to steal the jwellery?")

    pitChoice = input(">")

    if pitChoice == "yes":
        print("you attempt to steal a jwellery,but it  wakes up and rips you to shreds.")
        print("you are now dead")
    elif pitChoice == "no":
        print("you decide to not to steal the jwellery of dog")
        print("you turn arouind and leave the house safely")
    else:
        print("Invalid Choice. please Enter Yes or No")

elif roomChoice == "dining room":
    print("you choose to go into the dining room")
    print("As you walk in, you see a shiny vase on the table.")
    print("Do you want to open the vase?")

    vaseChoice = input(">")
    if vaseChoice == "yes":
        print("you open the vase finds a piles of bones!")
    elif vaseChoice == "no":
        print("You decide to not to open the tiny vase")
        print("As you turn to leave, You hear a cracking sound coming from the corner.")
        print("A dark figure with a glowing red eyes launches at you, knocking you uncconcious.")
        print("You wake up in youR bed. It was all dream.")
    else:
        print("Invalid choice Please enter Yes or No")
else:
    print("Invalid Entry")