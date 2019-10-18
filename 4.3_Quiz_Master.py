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

q3 = input("What is it that has a neck but no head, and two arms but no hands? \n A. A Clock \n B. A Tripod \n C. A Shirt \n D. A Barbie doll with no hands and head \n  ")
print()
if q3.lower() == "c" or q3.lower() == "a shirt":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The right answer is: C. A Shirt ")
print()

q4 = input("I can't be felt, can't be heard or smelt. I lie behind stars and under hills, and empty the empty holes I fill. What am I? \n A. Darkness  \n B.  \n C.  \n D.  \n   ")
if q4.lower() == "a" or q4.lower() == "darkness":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The right answer is:  A. Darkness")
print()

q5 = input("What is it that when given one, you'll almost always have either two or more, or none? \n A.  \n B.  \n C.  \n D. A choice \n   ")
if q5.lower() == " " or q5.lower() == " ":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The right answer is: ")
print()

q6 = input("I've never been afraid but I've become petrified. I can't make a bird but I can make a bat. I can't live in a house but I would die to have one ? \n A.  \n B.  \n C.  \n D.  \n   ")
if q6.lower() == " " or q6.lower() == " ":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The right answer is: ")
print()

q7 = input("? \n A.  \n B.  \n C.  \n D.  \n   ")
if q7.lower() == " " or q7.lower() == " ":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The right answer is: ")
print()

q8 = input("? \n A.  \n B.  \n C.  \n D.  \n   ")
if q8.lower() == " " or q8.lower() == " ":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The right answer is: ")
print()