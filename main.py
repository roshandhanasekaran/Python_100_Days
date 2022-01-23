# # 🚨 Don't change the code below 👇
# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# print(student_scores)
# # 🚨 Don't change the code above 👆

# #Write your code below this row 👇
# # max function with loops
# highest_score = 0
# for score in student_scores:
#   if score > highest_score:
#     highest_score = score 
# print(highest_score)    
# #min
# lowest_score = student_scores[1]
# for low in student_scores:
#   if low < lowest_score:
#     lowest_score = low 
# print(lowest_score)    
# #max
# highest_score = 0 
# for score in student_scores:
#   if score > highest_score:
#     highest_score = score 
# print(highest_score)    
# #min
# lower_score = student_scores[0] 
# for lower in student_scores:
#   if lower < lower_score:
#     lower_score = lower
#     print(lower_score)
# #sum 
# total_score = 0
# for total in student_scores:
#   total_score = total_score + total
#   print(total_score)

# #count   
# score_index = 0
# for index in student_scores:
#   score_index = score_index + 1
# print(score_index)

#range 
sum_number = 0
for number in range(1,101):
  sum_number = sum_number + number 
print(sum_number)