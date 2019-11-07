'''
QUIZ MASTER PROJECT
-------------------
The criteria for the project are on the website. Make sure you test this quiz with 
two of your student colleagues before you run it by your instructor.
'''

score = 0
quiz = 0
print()
print("Welcome to Peggy's Riddle Quiz!")
print()
print()

quiz += 1
q1 = input("What goes through a door, but never goes in and never comes out? \n A. Keys \n B. A Doorknob \n C. Air \n D. A Keyhole \n  ")
if q1.lower() == "a keyhole" or q1.lower() == "d":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The right answer is: D. A Keyhole")
print()

quiz += 1
q2 = input("What is it that no man ever did see, which never was, but always is to be? \n A. The Future \n B. Tomorrow \n C. Death \n D. Time \n   ")
if q2.lower() == "tomorrow" or q2.lower() == "b":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The right answer is: B. Tomorrow")
print()

quiz += 1
q3 = input("What is it that has a neck but no head, and two arms but no hands? \n A. A Clock \n B. A Tripod \n C. A Shirt \n D. A Barbie doll with no hands and head \n  ")
print()
if q3.lower() == "c" or q3.lower() == "a shirt":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The right answer is: C. A Shirt ")
print()

quiz += 1
q4 = input("I can't be felt, can't be heard or smelt. I lie behind stars and under hills, and empty the empty holes I fill. What am I? \n A. Darkness  \n B. A Black hole \n C. Space \n D. A vortex \n   ")
if q4.lower() == "a" or q4.lower() == "darkness":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The right answer is:  A. Darkness")
print()

quiz += 1
q5 = input("What is it that when given, you'll almost always have either two or more, or none? \n A. Socks \n B. The equation: 2 + x \n C. Friends \n D. A choice \n   ")
if q5.lower() == "a choice" or q5.lower() == "d":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The right answer is: D. A choice")
print()

quiz += 1
q6 = input("I am heavy and hard to pick up, but backwards I am not. What am I? \n A. A Stone \n B. A container filled with something \n C. A Ton \n D. Anything in zero gravity \n   ")
if q6.lower() == "c" or q6.lower() == "a ton" or q6.lower() == "ton":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The right answer is: C. A Ton")
print()

quiz += 1
q7 = input(" A red House is made from red bricks. A blue house is made from blue bricks. What is a green house made of? \n A. Wood \n B. Glass \n C. Mud \n D. Green bricks \n   ")
if q7.lower() == "b" or q7.lower() == "glass":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The right answer is: B. Glass ")
print()

quiz += 1
q8 = input("I am the beginnig of everything, the end of everywhere. I'm the beginning of eternity, the end of time and space. What am I? \n A. Death \n B. No such thing exisist \n C. The letter e \n D. The universe \n   ")
if q8.lower() == "c" or q8.lower() == "e" or q8.lower() == "the letter e ":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The right answer is: C. The letter e ")

quiz += 1
q9 = input("Complete the sequence. \n 89, 144, 233, 377, ?? \n \n A. 987 \n B. 610 \n C. 754 \n D. 466 \n   ")
if q9.lower() == "b" or q9.lower() == 610:
    print("Correct!")
    score += 1
else:
    print("Incorrect! The right answer is: B. 610. It is the next number in the Fibonacci Sequence!")


total = 100*(score/quiz)

if total >= 93.00:
    print("Your grade is:", total, "(A) \n Wow, brilliant!")
if total >= 90.00 and total <= 92.99:
    print("Your grade is:", total, "(A-) \n Wow, brilliant!")
if total >= 87.00 and total <= 89.99:
    print("Your grade is:", total, "(B+) \n Good Job!")
if total >= 83.00 and total <= 86.99:
    print("Your grade is:", total, "(B) \n Good Job!")
if total >= 80.00 and total <= 82.99:
    print("Your grade is:", total, "(B-) \n Well done.")
if total >= 77.00 and total <= 79.99:
    print("Your grade is:", total, "(C+) \n Well done.")
if total >= 73.00 and total <= 76.99:
    print("Your grade is:", total, "(C) \n Not bad.")
if total >= 70.00 and total <= 72.99:
    print("Your grade is:", total, "(C-) \n Not bad.")
if total >= 67.00 and total <= 69.99:
    print("Your grade is:", total, "(D+) \n You should brush up on your riddle solving skills...")
if total >= 60.00 and total <= 66.99:
    print("Your grade is:", total, "(D) \n You should brush up on your riddle solving skills... ")
if total >= 0.00 and total <= 59.99:
    print("Your grade is:", total, "(F) \n Wow... just wow. ")
