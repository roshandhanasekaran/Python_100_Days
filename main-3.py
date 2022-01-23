# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# import random
# num_item = len(names)
# Random_choice = random.randint(0, num_item - 1)
# person_who_will_pay = names[Random_choice]
# print(f"the person who will ay is {person_who_will_pay}")

import random
char = len(names)
random_choice = random.randint(0,char -1)
bill_payer = names[random_choice]
print(f"the person who has to pay the bil is {bill_payer}")