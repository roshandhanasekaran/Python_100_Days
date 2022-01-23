#Write your code below this row 👇
num = 0
for game in range(1,101):
  #print(game)
  if game % 5 == 0 and  game% 3==0 :
    print("fizzBuzz")  
  elif game % 5 == 0 :
    print("buzz") 
  elif game% 3==0 :
    print("Fizz")  
  else:
    print(game) 



