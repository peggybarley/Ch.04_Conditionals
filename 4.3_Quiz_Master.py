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

q1 = input("What is it that no man ever did see, which never was, but always is to be? \n A. The Future \n B. Tomorrow \n C. Death \n D. Time ")
if q1.lower() == "tomorrow" or q1.lower() == "b":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The right answer is: B. Tomorrow")


q2 = input("What goes through a door but never goes in and never comes out? \n A. Keys \n B. A Doorknob \n C. A Keyhole \n D. Air, It's Everywhere ")
print(score)
if q2.lower() == "a keyhole" or q2.lower() == "c":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The right answer is: C. A Keyhole")


q3 = input("What goes through a door but never goes in and never comes out? \n A. Keys \n B. A Doorknob \n C. A Keyhole \n D. Air, It's Everywhere ")
print(score)
if q3.lower() == "a keyhole" or q3.lower() == "c":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The right answer is: C. A Keyhole")

