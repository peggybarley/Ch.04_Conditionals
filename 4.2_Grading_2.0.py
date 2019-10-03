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

if grade >= 93.00:
    print("Your final grade is:", grade, "(A)")
if grade >= 90.00 or grade <= 92.99:
    print("Your final grade is:", grade, "(A-)")
if grade >= 87.00 or grade <= 89.99:
    print("Your final grade is:", grade, "(B+)")
if grade >= 83.00 or grade <= 86.99:
    print("Your final grade is:", grade, "(B)")
if grade >= 80.00 or grade <= 82.99:
    print("Your final grade is:", grade, "(B-)")
if grade >= 77.00 or grade <= 79.99:
    print("Your final grade is:", grade, "(C+)")
if grade >= 73.00 or grade <= 76.99:
    print("Your final grade is:", grade, "(C)")
if grade >= 70.00 or grade <= 72.99:
    print("Your final grade is:", grade, "(C-)")
if grade >= 67.00 or grade <= 69.99:
    print("Your final grade is:", grade, "(D+)")
if grade >= 60.00 or grade <= 66.99:
    print("Your final grade is:", grade, "(D)")
if grade >= 0.00 or grade <= 59.99:
    print("Your final grade is:", grade, "(F)")
    print("Transfer to Johnston!")
