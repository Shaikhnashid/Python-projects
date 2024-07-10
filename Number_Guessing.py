import random
num=random.randint(1,10)
guess=int(input("Enter the number from 1 to 10 : "))

while guess != num:
     if guess < num:
          print("its too low")
     elif guess > num:
          print("Its too high")

     guess = int(input("Try your luck Again : "))
print(" you guessed Right")         