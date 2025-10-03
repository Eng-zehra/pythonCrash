# # 
number=int(input("Enter number To Check if its Possitive or Negative "))
if(number==0):
    print(number,"Is Zero")
elif(number>0):
    print(number,"Is Positive number")
else:
    print(number,"IS Negative ")

# #legible age
age=int(input("Enter Your Age "))
if(age>=18):
    print("Eligible to vote")
else:print("Not eligible")
#discount
bill=int(input("Bill amount: "))
if(bill>=1000):
    discount=bill*0.2
    result=bill-discount
elif(bill>=500):
    discount=bill*0.2
    result=bill-discount
else:
    discount=bill*0.2
    result=bill-discount
print("Final amount after discount:", result)

# #Tricky

num1=int(input("Enter number 1 "))
num2=int(input("Enter number 2 "))
num3=int(input("Enter number 3 "))
if(num1>=num2 and num1>=num3):
    print(num1,"One Is The Max")
elif(num2>=num1 and num2>=num3):
    print(num2,"Two IS THE MAX")
elif(num3>=num2 and num3>=num1):
    print(num3,"Three IS The Max")
else:
    print("All numbers are Same")

# #divisble 2 and 4
num=int(input("Enter a number: "))
if(num %2==0 and num %4==0):
    print(num ,"is divible by 2 and 4")
else:print(num,"is not divisible by 2 and 4")

year=int(input("Enter a year leap or not"))
if(year % 400==0 ):
    print(year,"LEAP YEAR")
elif(year%100==0):
    print(year,"is not leap year")
elif(year%4==0):
     print(year,"LEAP YEAR")
else:("is NOT a Leap Yea")

#2
score=int(input("Enter a year leap or not"))
if(score<=90 and score<=100):
    print("A")
elif(score>80):
    print("B")
elif(score>70 and score<80):
    print("C")
elif(score>60 and score<70):
    print("D")
else:print("Fail")

#q3
balance = 5000
withdraw = int(input("Enter withdraw amount: "))

if withdraw > balance:
    print("Insufficient funds")
elif withdraw % 100 != 0:
    print("Invalid amount, enter in multiples of 100")
else:
    balance -= withdraw
    print("Transaction successful! Remaining balance:", balance)


#q4
lenth1=10
lenth2=10
lenth3=11
if(lenth1==lenth2 and lenth1==lenth3 and lenth2==lenth3):
    print("Equilateral")
elif(lenth1==lenth2 or lenth1==lenth3 or lenth2==lenth3):
    print("Isosceles")
else:
    print("Scalene")
#password cheker

