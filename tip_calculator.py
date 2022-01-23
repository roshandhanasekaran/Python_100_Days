#If the bill was $150.00, split between 5 people, with 12% tip. 
print("welcome to the tip calculator ")
bill = input(" What wa sthe total bill")
#Each person should pay (150.00 / 5) * 1.12 = 33.6
each_person_should_pay = (float(bill) / 5 *1.12)
#Format the result to 2 decimal places = 33.60
Tip= round(each_person_should_pay ,2)
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
print(Tip)
#Write your code below this line 👇