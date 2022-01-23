print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120 :
  print("you are allowed")
  age = int(input("What is your age"))  
  bill =0
  if age < 12 :
    bill = 7
    print("please pay 7$")
  elif age <=18:
    bill = 12
    print("pleease pay 12$")     
  else: 
    bill = 18
    print("pay 18$")
  wants_photo = input("do you want a photo Y or N")
  if wants_photo == "Y":
    bill= bill +3
    print(f"your total bill is {bill}$")

else:  
    print("you are not allowed")