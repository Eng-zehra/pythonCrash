import random
number=random.randint(0,10)
guest=int(input("Enter Your guesting number: "))
if(guest==number):
    print("Congratulations you got it " ,guest)
elif(guest<number):
    print(f"Guess Too Low   {guest}")
elif(guest>number):
    print(f"Guess too hight {guest}")
else:print("opps its not")