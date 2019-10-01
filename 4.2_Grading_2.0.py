'''
GRADING 2.0
-------------------
Copy your Grading 1.0 program and modify it to also print out the letter grade depending on the numerical grade.
If they fail, tell them to "Transfer to Johnston!"
'''

print()
print("Welcome to Peggy's Grade Calculator")
print()
sg = float(input("What is your semester grade?"))
fe = float(input("What is your final exam grade?"))
ew = float(input("What is your exam worth?"))
ew = ew/100
grade = sg*(1-ew) + fe*(ew)
print()

if grade
print("Your final grade is:", grade)