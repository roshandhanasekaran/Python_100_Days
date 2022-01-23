# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

BMI = weight / (height * height)
BMI_ADV = (round(BMI))
if BMI_ADV == 18:
  print(f"Your BMI is {BMI_ADV}, you are underweight ")
elif BMI_ADV == 22 :
   print(f" Your BMI is {BMI_ADV},you have a normal weight")  
elif BMI_ADV == 28 :
    print(f"Your BMI is {BMI_ADV},you are slightly overweight ")  
elif BMI_ADV == 33 :
   print(f"Your BMI is {BMI_ADV},you are obese")  
elif BMI_ADV == 40 :
  print(f"Your BMI is {BMI},you are linically obese")  
