# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  total_hight = 0
  for height in student_heights:
    total_hight += int(height)
  total_avrage_length = 0
  for avrage in student_heights:
    total_avrage_length += 1
avrage = round(total_hight / total_avrage_length)
print(avrage)
#Write your code below this row 👇


 

