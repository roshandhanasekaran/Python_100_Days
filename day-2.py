#DataTypes

#Subscription 
print("helloWorld"[4])

name_char = len(input("Whats is your name?"))
new_name_char= str(name_char)
print("length of my name is "+ new_name_char  )

#challenge

two_digit_number = input("Type a two digit number: ")
print (int(two_digit_number[0]) + int(two_digit_number[1]))


#BMI calculator 

weight = input("enter your weight in kg: ")
height = input("enter your height in m: ")

final_height = float(height)*float(height)
final_weight =int(weight)
BMI= int(final_weight / final_height)
print("bmi is" +" "+ str(BMI))