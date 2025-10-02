import random
number=random.randint(0,10)
guest=int(input("Enter your guessing number (0-10):"))
if(guest < 0 or guest >10):
    print("Invalid guess! Please choose a number between 0 and 10.")
elif(guest==number):
        print("Congratulations you got it " ,guest)
elif(guest>number):
        print(f"Guess too hight {guest}")
else:print("Guess Too low  ")