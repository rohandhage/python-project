import random
number=random.randrange(1,101)
userInput=int(input("Enter Your Number:-"))
if userInput>number:
    print("computer Number",number)
    print("Your guess number is too high")
elif number>userInput:
    print("computer Number",number)
    print("Your guess number is too low")
else:
    print("Computer Number",number)
    print("Your guess number is equal")
