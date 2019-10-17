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

q1 = input("What goes through a door but never goes in and never comes out? \n A. Keys \n B. A Doorknob \n C. Air, It's Everywhere \n D. A Keyhole \n  ")
if q1.lower() == "a keyhole" or q1.lower() == "d":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The right answer is: D. A Keyhole")
print()

q2 = input("What is it that no man ever did see, which never was, but always is to be? \n A. The Future \n B. Tomorrow \n C. Death \n D. Time \n   ")
if q2.lower() == "tomorrow" or q2.lower() == "b":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The right answer is: B. Tomorrow")
print()

q3 = input("? \n A. \n B. \n C. \n D. \n  ")
print()
if q3.lower() == " " or q3.lower() == " ":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The right answer is: ")
print()
