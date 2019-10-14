'''
QUIZ MASTER PROJECT
-------------------
The criteria for the project are on the website. Make sure you test this quiz with 
two of your student colleagues before you run it by your instructor.
'''

score = 0
print()
print("Welcome to Peggy's Riddle Quiz!")
print()
print()
q1 = str(input("What is it that no man ever did see, which never was, but always is to be? \n A. The Future \n B. Tomorrow \n C. Death \n D. Time "))

if q1.lower == "a" or "the future" or "c" or "death" or "d" or "time":
  print("Incorrect! The right answer is B. Tomorrow")
elif q1.lower == "tomorrow" or "b":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The right answer is; B. Tomorrow")

print(score)

